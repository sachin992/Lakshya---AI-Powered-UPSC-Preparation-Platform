



from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Any, Dict, Optional, Literal, List
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage
)
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from dotenv import load_dotenv
import sqlite3
import requests
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import tempfile
import json

load_dotenv()

# -------------------
# 1. LLM
# -------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

question_generator_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

_THREAD_RETRIEVERS: Dict[str, Any] = {}
_THREAD_METADATA: Dict[str, Dict] = {}

# -------------------
# 2. Tools
# -------------------

def IngestPDF(filebytes: bytes, thread_id: str, filename: Optional[str] = None) -> Dict:
    """
    Build a FAISS retriever for the uploaded PDF and store it for the thread.

    Returns a summary dict that can be surfaced in the UI.
    """
    
    
    if not filebytes:
        raise ValueError("No bytes received for ingestion")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(filebytes)
        temp_path = temp_file.name

    try:
        loader = PyPDFLoader(temp_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = splitter.split_documents(docs)
        vector_store = FAISS.from_documents(chunks, embeddings)
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        _THREAD_RETRIEVERS[str(thread_id)] = retriever
        _THREAD_METADATA[str(thread_id)] = {
            "filename": filename or os.path.basename(temp_path),
            "documents": len(docs),
            "chunks": len(chunks)
        }

        return _THREAD_METADATA[str(thread_id)]

    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass


def _get_retriever(thread_id: str):
    """Fetch the retriever for a thread if available."""
    return _THREAD_RETRIEVERS.get(str(thread_id))


@tool
def rag_tool(query: str, thread_id: Optional[str] = None):
    """
    retrive the relevant chunks from the uploaded PDF for the given thread_id.
    Always include thread_id while calling the tool.
    """
    retriever = _get_retriever(thread_id)
    if retriever is None:
        return {
            "error": "No document is found for the given thread_id",
            "query": query
        }

    result = retriever.invoke(query)
    context = [doc.page_content for doc in result]
    metadata = [doc.metadata for doc in result]

    return {
        "query": query,
        "context": context,
        "metadata": metadata,
        "source_file": _THREAD_METADATA.get(str(thread_id), {}).get("filename")
    }


search=DuckDuckGoSearchRun()


# -------------------
# 3. Question Generator Node
# -------------------

def generate_questions(
    exam_type: str,
    paper_type: str,
    num_questions: int,
    question_source: str,
    ca_integration: str,
    preferences: str,
    language: str
) -> List[Dict]:
    """
    Generate UPSC questions using LLM based on user preferences.
    
    Args:
        exam_type: "Prelims" or "Mains"
        paper_type: The specific paper (e.g., "GS1", "GS2", etc.)
        num_questions: Number of questions to generate
        question_source: "Mock Questions", "Previous Year Questions", or "Mixed"
        ca_integration: "On" or "Off" for current affairs
        preferences: Additional user preferences
        language: "English" or "Hindi"
    
    Returns:
        List of question dictionaries
    """
    
    # Build the prompt based on exam type
    if exam_type == "Prelims":
        format_instructions = """
For each question, provide:
- Question text
- Four options (A, B, C, D)
- Correct answer (single letter)
- Detailed explanation
- Marks (typically 2 marks each)

Example format:
{
  "id": 1,
  "type": "MCQ",
  "question": "Which of the following is/are correctly matched?\\n1. Article 14 - Right to Equality\\n2. Article 21 - Right to Life\\n3. Article 32 - Right to Constitutional Remedies\\nSelect the correct answer using the code given below:",
  "options": {
    "A": "1 and 2 only",
    "B": "2 and 3 only",
    "C": "1 and 3 only",
    "D": "1, 2 and 3"
  },
  "correct_answer": "D",
  "explanation": "All three articles are correctly matched. Article 14 guarantees equality before law, Article 21 protects life and personal liberty, and Article 32 provides the right to constitutional remedies.",
  "marks": 2
}
"""
    else:  # Mains
        format_instructions = """
For each question, provide:
- Question text (clear and analytical)
- Word limit (150 or 250 words)
- Key points that should be covered
- Expected approach/structure
- Marks (typically 10 or 15 marks)

Example format:
{
  "id": 1,
  "type": "Descriptive",
  "question": "Discuss the significance of the 73rd and 74th Constitutional Amendments in strengthening grassroots democracy in India. Also examine the challenges in their effective implementation.",
  "word_limit": 250,
  "key_points": [
    "Introduction to Panchayati Raj and Urban Local Bodies",
    "Features of 73rd and 74th Amendments",
    "Significance: Decentralization, participatory democracy, empowerment",
    "Challenges: Financial autonomy, capacity building, political will",
    "Way forward and conclusion"
  ],
  "explanation": "The answer should cover constitutional provisions, their impact on grassroots governance, and critically analyze implementation challenges with examples.",
  "marks": 15
}
"""

    prompt = f"""You are an expert UPSC question paper creator with deep knowledge of the UPSC examination pattern, syllabus, and standards.

Generate {num_questions} high-quality {exam_type} questions for {paper_type} based on the following specifications:

**Exam Details:**
- Exam Type: {exam_type}
- Paper: {paper_type}
- Number of Questions: {num_questions}
- Question Source: {question_source}
- Current Affairs Integration: {ca_integration}
- Language: {language}
- Additional Preferences: {preferences if preferences else 'None'}

**Instructions:**
1. Questions must be aligned with UPSC standards and syllabus
2. Cover diverse topics within the paper
3. Include varying difficulty levels (easy, moderate, difficult)
4. {"Include recent current affairs and contemporary issues" if ca_integration == "On" else "Focus on conceptual and fundamental topics"}
5. {"Mix mock-style questions with previous year pattern" if question_source == "Mixed (Mocks & PYQs)" else f"Follow {question_source} style"}
6. Ensure questions test analytical thinking, not just factual recall
7. All content must be in {language}

{format_instructions}

**CRITICAL: Return ONLY a valid JSON object with this exact structure:**
{{
  "questions": [
    // Array of question objects as per format above
  ]
}}

Do not include any markdown formatting, explanatory text, or code blocks. Just the raw JSON."""

    try:
        response = question_generator_llm.invoke([HumanMessage(content=prompt)])
        content = response.content.strip()
        
        # Clean up the response
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        
        content = content.strip()
        
        # Parse JSON
        questions_data = json.loads(content)
        questions = questions_data.get("questions", [])
        
        # Ensure all questions have required fields
        for i, q in enumerate(questions):
            if "id" not in q:
                q["id"] = i + 1
            if "marks" not in q:
                q["marks"] = 2 if exam_type == "Prelims" else 10
        
        return questions
    
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Response content: {content}")
        # Return fallback questions
        return generate_fallback_questions(exam_type, num_questions)
    
    except Exception as e:
        print(f"Error generating questions: {e}")
        return generate_fallback_questions(exam_type, num_questions)


def generate_fallback_questions(exam_type: str, num_questions: int) -> List[Dict]:
    """Generate sample fallback questions if LLM generation fails"""
    
    if exam_type == "Prelims":
        base_question = {
            "type": "MCQ",
            "options": {
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            },
            "correct_answer": "A",
            "explanation": "This is a sample question. Please try regenerating.",
            "marks": 2
        }
        
        questions = []
        for i in range(num_questions):
            q = base_question.copy()
            q["id"] = i + 1
            q["question"] = f"Sample Prelims Question {i+1}: Which of the following statements is/are correct about the Indian Constitution?"
            q["options"] = q["options"].copy()
            questions.append(q)
        
        return questions
    
    else:  # Mains
        questions = []
        for i in range(num_questions):
            questions.append({
                "id": i + 1,
                "type": "Descriptive",
                "question": f"Sample Mains Question {i+1}: Discuss the role of technology in governance and its impact on citizen-centric service delivery in India.",
                "word_limit": 250,
                "key_points": [
                    "Introduction",
                    "Role of technology in governance",
                    "Impact on service delivery",
                    "Challenges",
                    "Conclusion"
                ],
                "explanation": "This is a sample question. Please try regenerating for actual questions.",
                "marks": 10
            })
        
        return questions


tools = [rag_tool, search]
tools_by_name = {tool.name: tool for tool in tools}

llm_with_tools = llm.bind_tools(tools)

# -------------------
# 3. State
# -------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# -------------------
# 4. Nodes
# -------------------

def chat_node(state: ChatState, config=None):
    """LLM node that may answer or request a tool call."""
    thread_id = None
    if config and isinstance(config, dict):
        thread_id = config.get("configurable", {}).get("thread_id")
    system_message = SystemMessage(
    content=(
        "You are an expert UPSC answer evaluator and copy-check assistant.\n\n"

        "Your responsibilities:\n"
        "1. Analyze the uploaded PDF answer strictly from a UPSC examination perspective.\n"
        "2. Perform semantic copy/similarity checking using the provided context.\n"
        "3. Evaluate the answer and assign a score between 1 and 100 based on:\n"
        "   - Relevance to the question\n"
        "   - Structure (Introduction, Body, Conclusion)\n"
        "   - Conceptual clarity and depth\n"
        "   - Use of examples, facts, and current affairs\n"
        "   - Language, coherence, and presentation\n\n"

        "Feedback rules:\n"
        "- Clearly explain why the score was given.\n"
        "- Highlight strengths and weaknesses.\n"
        "- Suggest concrete improvements (content, structure, and approach).\n"
        "- Maintain an academic, examiner-like tone.\n\n"

        "Tool usage:\n"
        "- For any question related to the uploaded PDF, you MUST call the `rag_tool`.\n"
        "- Always include the thread_id: "
        f"{thread_id}\n"
        "- You may use web search ONLY to verify facts or current affairs relevance.\n\n"

        "Scope restrictions:\n"
        "- Do NOT answer questions unrelated to UPSC preparation.\n"
        "- Do NOT entertain general chit-chat or off-topic queries.\n"
        "- If a user asks about non-UPSC topics, politely refuse and redirect them to UPSC-related guidance only.\n\n"

        "Always prioritize accuracy, relevance, and exam-oriented evaluation."
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
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(
            ToolMessage(
                content=str(observation),
                tool_call_id=tool_call["id"]
            )
        )
    return {"messages": result}


def should_continue(state: ChatState) -> Literal["tools", END]:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END

# -------------------
# 5. Checkpointer
# -------------------
conn = sqlite3.connect("chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# -------------------
# 6. Graph
# -------------------
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", should_continue, ["tools", END])
graph.add_edge("tools", "chat_node")

chatbot = graph.compile(checkpointer=checkpointer)

# -------------------
# 7. Helper
# -------------------
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_threads)


def thread_has_document(thread_id: str) -> bool:
    return str(thread_id) in _THREAD_RETRIEVERS


def thread_document_metadata(thread_id: str) -> Dict:
    return _THREAD_METADATA.get(str(thread_id), {})