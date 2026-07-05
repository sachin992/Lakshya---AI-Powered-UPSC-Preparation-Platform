import json
import os
import tempfile
from typing import Any, Dict, Literal, Optional, TypedDict

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.vectorstores import FAISS
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from app.core.config import settings


class ChatState(TypedDict):
    messages: list[BaseMessage]


_THREAD_RETRIEVERS: Dict[str, Any] = {}
_THREAD_METADATA: Dict[str, Dict[str, Any]] = {}


def _has_openai_key() -> bool:
    return bool(settings.openai_api_key)


llm = ChatOpenAI(model=settings.openai_model, temperature=0.2) if _has_openai_key() else None
question_llm = ChatOpenAI(model=settings.openai_model, temperature=0.7) if _has_openai_key() else None
embeddings = OpenAIEmbeddings(model=settings.embedding_model) if _has_openai_key() else None
search = DuckDuckGoSearchRun()


def ingest_pdf(filebytes: bytes, thread_id: str, filename: Optional[str] = None) -> Dict[str, Any]:
    if embeddings is None:
        raise ValueError("OPENAI_API_KEY is not configured")

    if not filebytes:
        raise ValueError("No PDF content provided")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(filebytes)
        tmp_path = tmp.name

    try:
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)
        vector_store = FAISS.from_documents(chunks, embeddings)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        _THREAD_RETRIEVERS[str(thread_id)] = retriever
        _THREAD_METADATA[str(thread_id)] = {
            "filename": filename or os.path.basename(tmp_path),
            "documents": len(docs),
            "chunks": len(chunks),
        }
        return _THREAD_METADATA[str(thread_id)]
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass


def thread_has_document(thread_id: str) -> bool:
    return str(thread_id) in _THREAD_RETRIEVERS


def thread_document_metadata(thread_id: str) -> Dict[str, Any]:
    return _THREAD_METADATA.get(str(thread_id), {})


@tool
def rag_tool(query: str, thread_id: Optional[str] = None):
    """Retrieve relevant chunks from the uploaded PDF for the given thread id."""
    retriever = _THREAD_RETRIEVERS.get(str(thread_id))
    if retriever is None:
        return {"error": "No document found for this thread", "query": query}
    result = retriever.invoke(query)
    return {
        "query": query,
        "context": [doc.page_content for doc in result],
        "metadata": [doc.metadata for doc in result],
    }


tools = [rag_tool, search]
tools_by_name = {t.name: t for t in tools}
llm_with_tools = llm.bind_tools(tools) if llm is not None else None


def chat_node(state: ChatState, config=None):
    if llm_with_tools is None:
        raise ValueError("OPENAI_API_KEY is not configured")

    thread_id = None
    if config and isinstance(config, dict):
        thread_id = config.get("configurable", {}).get("thread_id")

    system_message = SystemMessage(
        content=(
            "You are an expert UPSC assistant. Keep responses exam-oriented. "
            "For uploaded PDF-based queries, use rag_tool and include thread_id=" + str(thread_id)
        )
    )

    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [system_message] + messages

    response = llm_with_tools.invoke(messages, config=config)
    return {"messages": [response]}


def tool_node(state: ChatState):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_impl = tools_by_name[tool_call["name"]]
        observation = tool_impl.invoke(tool_call["args"])
        result.append(ToolMessage(content=str(observation), tool_call_id=tool_call["id"]))
    return {"messages": result}


def should_continue(state: ChatState) -> Literal["tools", END]:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END


graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)
graph.set_entry_point("chat_node")
graph.add_conditional_edges("chat_node", should_continue, ["tools", END])
graph.add_edge("tools", "chat_node")
chatbot = graph.compile()


def chat(message: str, thread_id: str) -> str:
    if llm is None:
        raise ValueError("OPENAI_API_KEY is not configured")

    config = {"configurable": {"thread_id": thread_id}}
    response = chatbot.invoke({"messages": [HumanMessage(content=message)]}, config=config)
    return response["messages"][-1].content


def generate_questions(
    exam_type: str,
    paper_type: str,
    num_questions: int,
    question_source: str,
    ca_integration: str,
    preferences: str,
    language: str,
):
    if question_llm is None:
        raise ValueError("OPENAI_API_KEY is not configured")

    prompt = f"""
You are an expert UPSC question setter.
Generate {num_questions} {exam_type} questions for {paper_type}.
Question source: {question_source}
Current affairs integration: {ca_integration}
Language: {language}
Preferences: {preferences or 'None'}
Return valid JSON with key 'questions'.
For Prelims use MCQ with options, correct_answer, explanation, marks.
For Mains use descriptive question, word_limit, key_points, explanation, marks.
"""
    try:
        content = question_llm.invoke([HumanMessage(content=prompt)]).content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        parsed = json.loads(content.strip())
        return parsed.get("questions", [])
    except Exception:
        questions = []
        for i in range(num_questions):
            if exam_type.lower() == "prelims":
                questions.append(
                    {
                        "id": i + 1,
                        "type": "MCQ",
                        "question": f"Sample Prelims Question {i + 1}",
                        "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
                        "correct_answer": "A",
                        "explanation": "Fallback generated question.",
                        "marks": 2,
                    }
                )
            else:
                questions.append(
                    {
                        "id": i + 1,
                        "type": "Descriptive",
                        "question": f"Sample Mains Question {i + 1}",
                        "word_limit": 250,
                        "key_points": ["Introduction", "Body", "Conclusion"],
                        "explanation": "Fallback generated question.",
                        "marks": 10,
                    }
                )
        return questions


def evaluate_mains_answers(thread_id: str, paper: str, marks: int, mode: str, question: str | None = None) -> str:
    prompt = f"""
Paper: {paper}
Marks: {marks}
Mode: {mode}
Question: {question or 'Evaluate based on uploaded answer copy.'}
Evaluate the uploaded UPSC mains answer from thread_id={thread_id}.
Use rag_tool and provide score, strengths, weaknesses, and improvements.
"""
    return chat(prompt, thread_id)
