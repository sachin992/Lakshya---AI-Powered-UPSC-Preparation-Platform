import streamlit as st
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="Dalvoy - Mains Evaluator", layout="wide")

# Initialize session state
if "selected_paper" not in st.session_state:
    st.session_state.selected_paper = None
if "selected_marks" not in st.session_state:
    st.session_state.selected_marks = None
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = None
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "English"
if "question_text" not in st.session_state:
    st.session_state.question_text = ""
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Paper options
paper_options = [
    "General Studies Paper I",
    "General Studies Paper II",
    "General Studies Paper III",
    "General Studies Paper IV - Theory",
    "General Studies Paper IV - Case Studies",
    "Essay Paper",
    "Optional - Humanities",
    "Optional - Technical"
]

# Sidebar Menu
with st.sidebar:
    st.markdown("### Menu")
    selected = option_menu(
        menu_title="",
        options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
        icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
        menu_icon="cast",
        default_index=3,
    )
    
    st.divider()
    st.markdown("### Mains History")
    if st.button("+ New Evaluation", use_container_width=True, key="new_eval_btn"):
        st.session_state.selected_paper = None
        st.session_state.selected_marks = None
        st.session_state.selected_mode = None
        st.session_state.question_text = ""
        st.session_state.uploaded_files = []

    st.divider()
    if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
        pass

# Top Header with tabs
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Mains Evaluator")

with col2:
    eval_col1, eval_col2 = st.columns(2)
    with eval_col1:
        if st.button("📋 Mains Evaluator", use_container_width=True, type="primary", key="mains_eval_btn"):
            pass
    with eval_col2:
        if st.button("📦 Bulk Evaluator", use_container_width=True, key="bulk_eval_btn"):
            pass

st.divider()

# Main Content
col1, col2 = st.columns([2.5, 1.5])

with col1:
    # Paper Type & Language Section
    st.markdown("### 🎯 Paper Type & Language")
    
    st.markdown("**Evaluation Language:**")
    lang_col1, lang_col2, lang_col3 = st.columns([1, 1, 2])
    
    with lang_col1:
        if st.button("English", use_container_width=True, 
                     type="primary" if st.session_state.selected_language == "English" else "secondary",
                     key="lang_english_btn"):
            st.session_state.selected_language = "English"
    
    with lang_col2:
        if st.button("हिंदी", use_container_width=True,
                     type="primary" if st.session_state.selected_language == "हिंदी" else "secondary",
                     key="lang_hindi_btn"):
            st.session_state.selected_language = "हिंदी"
    
    with lang_col3:
        st.button("All Languages Supported - Click Here", use_container_width=True, key="all_lang_btn")
    
    st.divider()
    
    st.markdown("**Select Paper:**")
    selected_paper = st.selectbox(
        "Select a paper",
        paper_options,
        index=paper_options.index(st.session_state.selected_paper) if st.session_state.selected_paper in paper_options else 0,
        label_visibility="collapsed",
        key="paper_select"
    )
    
    if selected_paper != st.session_state.selected_paper:
        st.session_state.selected_paper = selected_paper
    
    st.divider()
    
    # Question Marks Section
    st.markdown("### 📊 Question Marks")
    marks_col1, marks_col2, marks_col3 = st.columns(3)
    
    with marks_col1:
        if st.button("10 marks", use_container_width=True,
                     type="primary" if st.session_state.selected_marks == 10 else "secondary",
                     key="marks_10_btn"):
            st.session_state.selected_marks = 10
    
    with marks_col2:
        if st.button("15 marks", use_container_width=True,
                     type="primary" if st.session_state.selected_marks == 15 else "secondary",
                     key="marks_15_btn"):
            st.session_state.selected_marks = 15
    
    with marks_col3:
        if st.button("20 marks", use_container_width=True,
                     type="primary" if st.session_state.selected_marks == 20 else "secondary",
                     key="marks_20_btn"):
            st.session_state.selected_marks = 20
    
    st.divider()
    
    # Evaluator Mode Section
    st.markdown("### ✅ How do you want your evaluator to be?")
    mode_col1, mode_col2 = st.columns(2)
    
    with mode_col1:
        if st.button("🎯 Hard", use_container_width=True,
                     type="primary" if st.session_state.selected_mode == "Hard" else "secondary",
                     key="mode_hard_btn"):
            st.session_state.selected_mode = "Hard"
    
    with mode_col2:
        if st.button("⭐ Easy", use_container_width=True,
                     type="primary" if st.session_state.selected_mode == "Easy" else "secondary",
                     key="mode_easy_btn"):
            st.session_state.selected_mode = "Easy"
    
    st.divider()
    
    # Question Section
    st.markdown("### 📝 Question (Optional)")
    question_text = st.text_area(
        "Enter the question here (optional - AI can read from uploaded images)",
        value=st.session_state.question_text,
        placeholder="Enter the question here (optional - AI can read from uploaded images)",
        height=80,
        label_visibility="collapsed",
        key="question_textarea"
    )
    st.session_state.question_text = question_text
    
    st.divider()
    
    # Upload Answer Sheets Section
    st.markdown("### 📤 Upload Answer Sheets")
    
    uploaded_files = st.file_uploader(
        "Click to upload or drag & drop",
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    if uploaded_files:
        st.session_state.uploaded_files = uploaded_files
        st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
        st.caption("Supports JPG, PNG, PDF (Max 25 files, 20MB each)")
    else:
        st.info("Supports JPG, PNG, PDF (Max 25 files, 20MB each)")
    
    st.divider()
    
    # Action Buttons
    button_col1, button_col2 = st.columns([1.5, 1])
    
    with button_col1:
        if st.button("🚀 Evaluate Answer (standard)", use_container_width=True, type="primary", key="evaluate_btn"):
            if st.session_state.selected_paper and st.session_state.selected_marks and st.session_state.selected_mode:
                st.success("✅ Evaluation started!")
            else:
                st.warning("⚠️ Please select paper, marks, and evaluator mode")
    
    with button_col2:
        if st.button("🔄 Reset All", use_container_width=True, key="reset_btn"):
            st.session_state.selected_paper = None
            st.session_state.selected_marks = None
            st.session_state.selected_mode = None
            st.session_state.question_text = ""
            st.session_state.uploaded_files = []
    
    st.divider()
    
    # Disclaimer Section
    with st.expander("📋 Disclaimer", expanded=False):
        st.markdown("""
        This evaluator uses AI to assess answers. While we strive for accuracy, 
        please note that AI evaluation may not be 100% accurate. Use this as a 
        learning tool and refer to official answer keys for final assessment.
        """)

# Right Sidebar - Current Selection
with col2:
    st.markdown("### 📋 Current Selection")
    
    selection_data = {
        "Paper": st.session_state.selected_paper or "Not Selected",
        "Marks": f"{st.session_state.selected_marks} marks" if st.session_state.selected_marks else "Not Selected",
        "Mode": st.session_state.selected_mode or "Not Selected",
        "Language": st.session_state.selected_language
    }
    
    for label, value in selection_data.items():
        st.markdown(f"**{label}:**")
        if label == "Paper" and st.session_state.selected_paper:
            st.markdown(f"<div style='color: #0066cc; font-weight: 500;'>{value}</div>", unsafe_allow_html=True)
        elif label == "Mode" and st.session_state.selected_mode:
            color = "#ff6b6b" if st.session_state.selected_mode == "Hard" else "#4CAF50"
            st.markdown(f"<div style='color: {color}; font-weight: 500;'>{value}</div>", unsafe_allow_html=True)
        elif label == "Language" and st.session_state.selected_language:
            st.markdown(f"<div style='color: #ff6b35;'>{value}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='color: #666;'>{value}</div>", unsafe_allow_html=True)
        st.divider()
    
    # Files Uploaded Count
    if st.session_state.uploaded_files:
        st.markdown(f"### 📎 Files Uploaded")
        st.success(f"✅ {len(st.session_state.uploaded_files)} file(s) ready for evaluation")
        for file in st.session_state.uploaded_files:
            st.caption(f"📄 {file.name}")
    else:
        st.info("📤 Upload answer sheets to proceed")
    
    st.divider()
    st.info("💡 Select all options and upload answer sheets to evaluate")