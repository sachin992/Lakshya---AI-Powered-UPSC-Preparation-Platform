
# import streamlit as st
# from streamlit_option_menu import option_menu
# def show():
    


#     # Page config
#     # st.set_page_config(page_title="Dalvoy - Mains Evaluator", layout="wide")

#     # Initialize session state
#     if "selected_paper" not in st.session_state:
#         st.session_state.selected_paper = None
#     if "selected_marks" not in st.session_state:
#         st.session_state.selected_marks = None
#     if "selected_mode" not in st.session_state:
#         st.session_state.selected_mode = None
#     if "selected_language" not in st.session_state:
#         st.session_state.selected_language = "English"
#     if "question_text" not in st.session_state:
#         st.session_state.question_text = ""
#     if "uploaded_files" not in st.session_state:
#         st.session_state.uploaded_files = []

#     # Paper options
#     paper_options = [
#         "General Studies Paper I",
#         "General Studies Paper II",
#         "General Studies Paper III",
#         "General Studies Paper IV - Theory",
#         "General Studies Paper IV - Case Studies",
#         "Essay Paper",
#         "Optional - Humanities",
#         "Optional - Technical"
#     ]



#     # Top Header with tabs
#     col1, col2 = st.columns([2, 1])

#     with col1:
#         st.markdown("## Mains Evaluator")

#     with col2:
#         eval_col1, eval_col2 = st.columns(2)
#         with eval_col1:
#             if st.button("📋 Mains Evaluator", use_container_width=True, type="primary", key="mains_eval_btn"):
#                 pass
#         with eval_col2:
#             if st.button("📦 Bulk Evaluator", use_container_width=True, key="bulk_eval_btn"):
#                 pass

#     st.divider()

#     # Main Content
#     col1, col2 = st.columns([2.5, 1.5])

#     with col1:
#         # Paper Type & Language Section
#         st.markdown("### 🎯 Paper Type & Language")
        
#         st.markdown("**Evaluation Language:**")
#         lang_col1, lang_col2, lang_col3 = st.columns([1, 1, 2])
        
#         with lang_col1:
#             if st.button("English", use_container_width=True, 
#                         type="primary" if st.session_state.selected_language == "English" else "secondary",
#                         key="lang_english_btn"):
#                 st.session_state.selected_language = "English"
        
#         with lang_col2:
#             if st.button("हिंदी", use_container_width=True,
#                         type="primary" if st.session_state.selected_language == "हिंदी" else "secondary",
#                         key="lang_hindi_btn"):
#                 st.session_state.selected_language = "हिंदी"
        
#         with lang_col3:
#             st.button("All Languages Supported - Click Here", use_container_width=True, key="all_lang_btn")
        
#         st.divider()
        
#         st.markdown("**Select Paper:**")
#         selected_paper = st.selectbox(
#             "Select a paper",
#             paper_options,
#             index=paper_options.index(st.session_state.selected_paper) if st.session_state.selected_paper in paper_options else 0,
#             label_visibility="collapsed",
#             key="paper_select"
#         )
        
#         if selected_paper != st.session_state.selected_paper:
#             st.session_state.selected_paper = selected_paper
        
#         st.divider()
        
#         # Question Marks Section
#         st.markdown("### 📊 Question Marks")
#         marks_col1, marks_col2, marks_col3 = st.columns(3)
        
#         with marks_col1:
#             if st.button("10 marks", use_container_width=True,
#                         type="primary" if st.session_state.selected_marks == 10 else "secondary",
#                         key="marks_10_btn"):
#                 st.session_state.selected_marks = 10
        
#         with marks_col2:
#             if st.button("15 marks", use_container_width=True,
#                         type="primary" if st.session_state.selected_marks == 15 else "secondary",
#                         key="marks_15_btn"):
#                 st.session_state.selected_marks = 15
        
#         with marks_col3:
#             if st.button("20 marks", use_container_width=True,
#                         type="primary" if st.session_state.selected_marks == 20 else "secondary",
#                         key="marks_20_btn"):
#                 st.session_state.selected_marks = 20
        
#         st.divider()
        
#         # Evaluator Mode Section
#         st.markdown("### ✅ How do you want your evaluator to be?")
#         mode_col1, mode_col2 = st.columns(2)
        
#         with mode_col1:
#             if st.button("🎯 Hard", use_container_width=True,
#                         type="primary" if st.session_state.selected_mode == "Hard" else "secondary",
#                         key="mode_hard_btn"):
#                 st.session_state.selected_mode = "Hard"
        
#         with mode_col2:
#             if st.button("⭐ Easy", use_container_width=True,
#                         type="primary" if st.session_state.selected_mode == "Easy" else "secondary",
#                         key="mode_easy_btn"):
#                 st.session_state.selected_mode = "Easy"
        
#         st.divider()
        
#         # Question Section
#         st.markdown("### 📝 Question (Optional)")
#         question_text = st.text_area(
#             "Enter the question here (optional - AI can read from uploaded images)",
#             value=st.session_state.question_text,
#             placeholder="Enter the question here (optional - AI can read from uploaded images)",
#             height=80,
#             label_visibility="collapsed",
#             key="question_textarea"
#         )
#         st.session_state.question_text = question_text
        
#         st.divider()
        
#         # Upload Answer Sheets Section
#         st.markdown("### 📤 Upload Answer Sheets")
        
#         uploaded_files = st.file_uploader(
#             "Click to upload or drag & drop",
#             type=["jpg", "jpeg", "png", "pdf"],
#             accept_multiple_files=True,
#             key="file_uploader"
#         )
        
#         if uploaded_files:
#             st.session_state.uploaded_files = uploaded_files
#             st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
#             st.caption("Supports JPG, PNG, PDF (Max 25 files, 20MB each)")
#         else:
#             st.info("Supports JPG, PNG, PDF (Max 25 files, 20MB each)")
        
#         st.divider()
        
#         # Action Buttons
#         button_col1, button_col2 = st.columns([1.5, 1])
        
#         with button_col1:
#             if st.button("🚀 Evaluate Answer (standard)", use_container_width=True, type="primary", key="evaluate_btn"):
#                 if st.session_state.selected_paper and st.session_state.selected_marks and st.session_state.selected_mode:
#                     st.success("✅ Evaluation started!")
#                 else:
#                     st.warning("⚠️ Please select paper, marks, and evaluator mode")
        
#         with button_col2:
#             if st.button("🔄 Reset All", use_container_width=True, key="reset_btn"):
#                 st.session_state.selected_paper = None
#                 st.session_state.selected_marks = None
#                 st.session_state.selected_mode = None
#                 st.session_state.question_text = ""
#                 st.session_state.uploaded_files = []
        
#         st.divider()
        
#         # Disclaimer Section
#         with st.expander("📋 Disclaimer", expanded=False):
#             st.markdown("""
#             This evaluator uses AI to assess answers. While we strive for accuracy, 
#             please note that AI evaluation may not be 100% accurate. Use this as a 
#             learning tool and refer to official answer keys for final assessment.
#             """)

#     # Right Sidebar - Current Selection
#     with col2:
#         st.markdown("### 📋 Current Selection")
        
#         selection_data = {
#             "Paper": st.session_state.selected_paper or "Not Selected",
#             "Marks": f"{st.session_state.selected_marks} marks" if st.session_state.selected_marks else "Not Selected",
#             "Mode": st.session_state.selected_mode or "Not Selected",
#             "Language": st.session_state.selected_language
#         }
        
#         for label, value in selection_data.items():
#             st.markdown(f"**{label}:**")
#             if label == "Paper" and st.session_state.selected_paper:
#                 st.markdown(f"<div style='color: #0066cc; font-weight: 500;'>{value}</div>", unsafe_allow_html=True)
#             elif label == "Mode" and st.session_state.selected_mode:
#                 color = "#ff6b6b" if st.session_state.selected_mode == "Hard" else "#4CAF50"
#                 st.markdown(f"<div style='color: {color}; font-weight: 500;'>{value}</div>", unsafe_allow_html=True)
#             elif label == "Language" and st.session_state.selected_language:
#                 st.markdown(f"<div style='color: #ff6b35;'>{value}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div style='color: #666;'>{value}</div>", unsafe_allow_html=True)
#             st.divider()
        
#         # Files Uploaded Count
#         if st.session_state.uploaded_files:
#             st.markdown(f"### 📎 Files Uploaded")
#             st.success(f"✅ {len(st.session_state.uploaded_files)} file(s) ready for evaluation")
#             for file in st.session_state.uploaded_files:
#                 st.caption(f"📄 {file.name}")
#         else:
#             st.info("📤 Upload answer sheets to proceed")
        
#         st.divider()
#         st.info("💡 Select all options and upload answer sheets to evaluate")




# import streamlit as st
# import uuid
# from streamlit_option_menu import option_menu
# from langchain_core.messages import HumanMessage
# from langchain_core.messages import AIMessage
# # 🔗 Import backend evaluator
# from final_backend import IngestPDF, chatbot


# def show():

#     # ---------------------------
#     # Session State Initialization
#     # ---------------------------
#     if "thread_id" not in st.session_state:
#         st.session_state.thread_id = str(uuid.uuid4())

#     if "selected_paper" not in st.session_state:
#         st.session_state.selected_paper = None
#     if "selected_marks" not in st.session_state:
#         st.session_state.selected_marks = None
#     if "selected_mode" not in st.session_state:
#         st.session_state.selected_mode = None
#     if "selected_language" not in st.session_state:
#         st.session_state.selected_language = "English"
#     if "question_text" not in st.session_state:
#         st.session_state.question_text = ""
#     if "uploaded_files" not in st.session_state:
#         st.session_state.uploaded_files = []
#     if "evaluation_result" not in st.session_state:
#         st.session_state.evaluation_result = None

#     # ---------------------------
#     # Paper Options
#     # ---------------------------
#     paper_options = [
#         "General Studies Paper I",
#         "General Studies Paper II",
#         "General Studies Paper III",
#         "General Studies Paper IV - Theory",
#         "General Studies Paper IV - Case Studies",
#         "Essay Paper",
#         "Optional - Humanities",
#         "Optional - Technical"
#     ]

#     # ---------------------------
#     # Header
#     # ---------------------------
#     col1, col2 = st.columns([2, 1])
#     with col1:
#         st.markdown("## 📝 Mains Evaluator")
#     with col2:
#         st.button("📦 Bulk Evaluator", use_container_width=True)

#     st.divider()

#     # ---------------------------
#     # Main Layout
#     # ---------------------------
#     col1, col2 = st.columns([2.5, 1.5])

#     # ===========================
#     # LEFT PANEL
#     # ===========================
#     with col1:

#         # Language Selection
#         st.markdown("### 🌐 Evaluation Language")
#         lang_col1, lang_col2 = st.columns(2)

#         with lang_col1:
#             if st.button(
#                 "English",
#                 use_container_width=True,
#                 type="primary" if st.session_state.selected_language == "English" else "secondary",
#             ):
#                 st.session_state.selected_language = "English"

#         with lang_col2:
#             if st.button(
#                 "हिंदी",
#                 use_container_width=True,
#                 type="primary" if st.session_state.selected_language == "हिंदी" else "secondary",
#             ):
#                 st.session_state.selected_language = "हिंदी"

#         st.divider()

#         # Paper Selection
#         st.markdown("### 📄 Select Paper")
#         st.session_state.selected_paper = st.selectbox(
#             "Paper",
#             paper_options,
#             index=paper_options.index(st.session_state.selected_paper)
#             if st.session_state.selected_paper in paper_options
#             else 0,
#             label_visibility="collapsed",
#         )

#         st.divider()

#         # Marks Selection
#         st.markdown("### 📊 Question Marks")
#         marks_col1, marks_col2, marks_col3 = st.columns(3)

#         with marks_col1:
#             if st.button("10 marks", use_container_width=True,
#                          type="primary" if st.session_state.selected_marks == 10 else "secondary"):
#                 st.session_state.selected_marks = 10

#         with marks_col2:
#             if st.button("15 marks", use_container_width=True,
#                          type="primary" if st.session_state.selected_marks == 15 else "secondary"):
#                 st.session_state.selected_marks = 15

#         with marks_col3:
#             if st.button("20 marks", use_container_width=True,
#                          type="primary" if st.session_state.selected_marks == 20 else "secondary"):
#                 st.session_state.selected_marks = 20

#         st.divider()

#         # Evaluator Mode
#         st.markdown("### 🎯 Evaluator Strictness")
#         mode_col1, mode_col2 = st.columns(2)

#         with mode_col1:
#             if st.button("Hard", use_container_width=True,
#                          type="primary" if st.session_state.selected_mode == "Hard" else "secondary"):
#                 st.session_state.selected_mode = "Hard"

#         with mode_col2:
#             if st.button("Easy", use_container_width=True,
#                          type="primary" if st.session_state.selected_mode == "Easy" else "secondary"):
#                 st.session_state.selected_mode = "Easy"

#         st.divider()

#         # Question Input
#         st.markdown("### 📝 Question (Optional)")
#         st.session_state.question_text = st.text_area(
#             "Question",
#             placeholder="Enter the UPSC question (optional)",
#             height=80,
#             label_visibility="collapsed",
#         )

#         st.divider()

#         # File Upload
#         st.markdown("### 📤 Upload Answer PDF")
#         uploaded_files = st.file_uploader(
#             "Upload PDF",
#             type=["pdf"],
#             accept_multiple_files=True,
#         )

#         if uploaded_files:
#             st.session_state.uploaded_files = uploaded_files

#             for file in uploaded_files:
#                 IngestPDF(
#                     filebytes=file.read(),
#                     thread_id=st.session_state.thread_id,
#                     filename=file.name,
#                 )

#             st.success(f"✅ {len(uploaded_files)} PDF(s) ingested successfully")

#         st.divider()

#         # Evaluate Button
#         if st.button("🚀 Evaluate Answer", use_container_width=True, type="primary"):

#             if not st.session_state.uploaded_files:
#                 st.warning("⚠️ Please upload at least one PDF")
#                 return

#             if not (
#                 st.session_state.selected_paper
#                 and st.session_state.selected_marks
#                 and st.session_state.selected_mode
#             ):
#                 st.warning("⚠️ Select paper, marks & evaluator mode")
#                 return

#             with st.spinner("🧠 Evaluating like a UPSC examiner..."):

#                 user_prompt = f"""
# Paper: {st.session_state.selected_paper}
# Marks: {st.session_state.selected_marks}
# Evaluator Mode: {st.session_state.selected_mode}
# Language: {st.session_state.selected_language}

# Question:
# {st.session_state.question_text or "Evaluate based on uploaded answer copy."}

# Evaluate the uploaded answer strictly as per UPSC mains standards.
# """



#             final_response = None

#             events = chatbot.stream(
#                 {
#                     "messages": [HumanMessage(content=user_prompt)]
#                 },
#                 config={
#                     "configurable": {
#                         "thread_id": st.session_state.thread_id
#                     }
#                 }
#             )

#             for event in events:
#                 if "messages" in event:
#                     last_msg = event["messages"][-1]
#                     if isinstance(last_msg, AIMessage) and last_msg.content:
#                         final_response = last_msg.content
#                         print(final_response)

#             st.session_state.evaluation_result = final_response

#         print("Hello World",st.session_state.evaluation_result)
#         # Show Result
#         if st.session_state.evaluation_result:
#             st.divider()
#             st.markdown("## 🧾 Examiner Feedback")
#             st.markdown(st.session_state.evaluation_result)

#     # ===========================
#     # RIGHT PANEL (SUMMARY)
#     # ===========================
#     with col2:
#         st.markdown("### 📋 Current Selection")

#         st.markdown(f"**Paper:** {st.session_state.selected_paper or 'Not Selected'}")
#         st.markdown(f"**Marks:** {st.session_state.selected_marks or 'Not Selected'}")
#         st.markdown(f"**Mode:** {st.session_state.selected_mode or 'Not Selected'}")
#         st.markdown(f"**Language:** {st.session_state.selected_language}")

#         st.divider()

#         if st.session_state.uploaded_files:
#             st.success(f"📎 {len(st.session_state.uploaded_files)} file(s) ready")
#             for f in st.session_state.uploaded_files:
#                 st.caption(f"📄 {f.name}")
#         else:
#             st.info("📤 Upload answer PDF to proceed")



import streamlit as st
import uuid
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

# 🔗 Backend imports
from final_backend import (
    chatbot,
    IngestPDF,
    thread_document_metadata,
)

    # ==========================
    # Utilities
    # ==========================
    
def show():    
    def generate_thread_id():
        return str(uuid.uuid4())


    # ==========================
    # Session Initialization
    # ==========================
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = generate_thread_id()

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []

    if "evaluation_result" not in st.session_state:
        st.session_state.evaluation_result = ""

    if "ingested_docs" not in st.session_state:
        st.session_state.ingested_docs = {}

    thread_key = st.session_state.thread_id
    thread_docs = st.session_state.ingested_docs.setdefault(thread_key, {})

    # ==========================
    # UI Header
    # ==========================
    st.markdown("## 📝 UPSC Mains Answer Evaluator")
    st.caption(f"Thread ID: `{thread_key}`")
    st.divider()

    # ==========================
    # Inputs
    # ==========================
    paper = st.selectbox(
        "Select Paper",
        [
            "GS Paper I",
            "GS Paper II",
            "GS Paper III",
            "GS Paper IV",
            "Essay",
            "Optional",
        ],
    )

    marks = st.selectbox("Marks", [10, 15, 20])
    mode = st.radio("Evaluator Mode", ["Hard", "Easy"], horizontal=True)

    question = st.text_area(
        "Question (optional)",
        placeholder="Enter the UPSC question here (optional)",
        height=80,
    )

    # ==========================
    # PDF Upload (REFERENCE MATCH)
    # ==========================
    st.subheader("📤 Upload Answer PDF")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        accept_multiple_files=False,
    )

    if uploaded_pdf:
        if uploaded_pdf.name in thread_docs:
            st.info("PDF already indexed for this evaluation")
        else:
            with st.status("Indexing PDF…", expanded=True) as status:
                summary = IngestPDF(
                    uploaded_pdf.getvalue(),
                    thread_id=thread_key,
                    filename=uploaded_pdf.name,
                )
                thread_docs[uploaded_pdf.name] = summary
                status.update(
                    label="✅ PDF Indexed Successfully",
                    state="complete",
                    expanded=False,
                )

    doc_meta = thread_document_metadata(thread_key)
    if doc_meta:
        st.caption(
            f"📄 Using `{doc_meta.get('filename')}` | "
            f"Pages: {doc_meta.get('documents')} | "
            f"Chunks: {doc_meta.get('chunks')}"
        )

    st.divider()

    # ==========================
    # Evaluation Trigger
    # ==========================
    if st.button("🚀 Evaluate Answer", type="primary", use_container_width=True):

        if not thread_docs:
            st.warning("⚠️ Please upload a PDF before evaluation")
            st.stop()

        prompt = f"""
    Paper: {paper}
    Marks: {marks}
    Evaluator Mode: {mode}

    Question:
    {question or "Evaluate based on uploaded answer copy."}

    Evaluate the uploaded answer strictly as per UPSC mains standards.
    """

        CONFIG = {
            "configurable": {"thread_id": thread_key},
            "metadata": {"thread_id": thread_key},
            "run_name": "mains_evaluation",
        }

        st.subheader("🧠 Examiner Evaluation")

        with st.chat_message("assistant"):
            status_holder = {"box": None}

            def stream_evaluation():
                for msg, meta in chatbot.stream(
                    {"messages": [HumanMessage(content=prompt)]},
                    config=CONFIG,
                    stream_mode="messages",
                ):
                    # Tool status display
                    if isinstance(msg, ToolMessage):
                        tool_name = getattr(msg, "name", "tool")
                        if status_holder["box"] is None:
                            status_holder["box"] = st.status(
                                f"🔧 Using `{tool_name}`",
                                expanded=True,
                            )
                        else:
                            status_holder["box"].update(
                                label=f"🔧 Using `{tool_name}`",
                                state="running",
                                expanded=True,
                            )

                    # Stream only assistant content
                    if isinstance(msg, AIMessage):
                        yield msg.content

            final_text = st.write_stream(stream_evaluation)

            if status_holder["box"] is not None:
                status_holder["box"].update(
                    label="✅ Evaluation Completed",
                    state="complete",
                    expanded=False,
                )

        st.session_state.evaluation_result = final_text

    # ==========================
    # Final Output (Persisted)
    # ==========================
    if st.session_state.evaluation_result:
        st.divider()
        st.markdown("## 📊 Final Examiner Feedback")
        st.markdown(st.session_state.evaluation_result)
