import streamlit as st
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="Dalvoy - Mock Test", layout="wide")

# Initialize session state
if "exam_type" not in st.session_state:
    st.session_state.exam_type = "Prelims"
if "language" not in st.session_state:
    st.session_state.language = "English"
if "paper_type" not in st.session_state:
    st.session_state.paper_type = None
if "num_questions" not in st.session_state:
    st.session_state.num_questions = 5
if "question_source" not in st.session_state:
    st.session_state.question_source = "Mock Questions"
if "ca_integration" not in st.session_state:
    st.session_state.ca_integration = "Off"
if "preferences" not in st.session_state:
    st.session_state.preferences = ""

# Define paper types based on exam type
paper_types = {
    "Prelims": ["General Studies (Paper I) - History, Geography, Polity, Economics, etc."],
    "Mains": [
        "GS1 - Indian Heritage and Culture, History and Geography",
        "GS2 - Governance, Constitution, Polity, Social Justice, International Relations",
        "GS3 - Technology, Economic Development, Environment, Security",
        "GS4 - Ethics, Integrity, Aptitude",
        "GS4 Case Study",
        "Optional"
    ]
}

# Sidebar Menu
with st.sidebar:
    st.markdown("### Menu")
    selected = option_menu(
        menu_title="",
        options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
        icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
        menu_icon="cast",
        default_index=1,
    )
    
    st.divider()
    st.markdown("### Test History")
    if st.button("+ New Test", use_container_width=True):
        st.info("New test created!")
    
    st.divider()
    if st.button("❓ Not Satisfied?"):
        pass

# Main Content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Create Your Mock Test")
    
    # Exam Type
    st.markdown("### Exam Type")
    exam_col1, exam_col2 = st.columns(2)
    with exam_col1:
        if st.button("Prelims", use_container_width=True, 
                     type="primary" if st.session_state.exam_type == "Prelims" else "secondary"):
            st.session_state.exam_type = "Prelims"
            st.session_state.paper_type = "General Studies (Paper I) - History, Geography, Polity, Economics, etc."
            st.rerun()
    
    with exam_col2:
        if st.button("Mains", use_container_width=True,
                     type="primary" if st.session_state.exam_type == "Mains" else "secondary"):
            st.session_state.exam_type = "Mains"
            st.session_state.paper_type = None
            st.rerun()
    
    # Language
    st.markdown("### Language")
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        if st.button("English", use_container_width=True,
                     type="primary" if st.session_state.language == "English" else "secondary"):
            st.session_state.language = "English"
            st.rerun()
    
    with lang_col2:
        if st.button("हिंदी", use_container_width=True,
                     type="primary" if st.session_state.language == "हिंदी" else "secondary"):
            st.session_state.language = "हिंदी"
            st.rerun()
    
    # Paper Type
    st.markdown("### Paper Type")
    available_papers = paper_types[st.session_state.exam_type]
    
    selected_paper = st.selectbox(
        "Select Paper",
        available_papers,
        index=0 if st.session_state.paper_type is None or st.session_state.paper_type not in available_papers else available_papers.index(st.session_state.paper_type),
        label_visibility="collapsed",
        key="paper_select"
    )
    
    if selected_paper != st.session_state.paper_type:
        st.session_state.paper_type = selected_paper
        st.rerun()
    
    # Number of Questions
    st.markdown("### Number of Questions")
    num_questions = st.slider("", min_value=1, max_value=100, value=st.session_state.num_questions, step=1, key="num_q")
    st.session_state.num_questions = num_questions
    st.caption(f"Max {num_questions} questions")
    
    # Question Source
    st.markdown("### Question Source")
    source_col1, source_col2, source_col3 = st.columns(3)
    with source_col1:
        if st.button("Mock Questions", use_container_width=True,
                     type="primary" if st.session_state.question_source == "Mock Questions" else "secondary"):
            st.session_state.question_source = "Mock Questions"
            st.rerun()
    
    with source_col2:
        if st.button("Previous Year Questions", use_container_width=True,
                     type="primary" if st.session_state.question_source == "Previous Year Questions" else "secondary"):
            st.session_state.question_source = "Previous Year Questions"
            st.rerun()
    
    with source_col3:
        if st.button("Mixed (Mocks & PYQs)", use_container_width=True,
                     type="primary" if st.session_state.question_source == "Mixed (Mocks & PYQs)" else "secondary"):
            st.session_state.question_source = "Mixed (Mocks & PYQs)"
            st.rerun()
    
    # Current Affairs Integration
    st.markdown("### Current Affairs Integration")
    ca_col1, ca_col2 = st.columns(2)
    with ca_col1:
        if st.button("On", use_container_width=True,
                     type="primary" if st.session_state.ca_integration == "On" else "secondary",
                     key="ca_on_btn"):
            st.session_state.ca_integration = "On"
            st.rerun()
    
    with ca_col2:
        if st.button("Off", use_container_width=True,
                     type="primary" if st.session_state.ca_integration == "Off" else "secondary",
                     key="ca_off_btn"):
            st.session_state.ca_integration = "Off"
            st.rerun()
    
    # Specific Preferences
    st.markdown("### Specific Preferences (Optional)")
    preferences = st.text_area(
        "Enter preferences",
        value=st.session_state.preferences,
        placeholder="e.g., 'focus on economic policies post-2020', 'environmental governance in urban areas', 'questions requiring critical analysis'",
        height=80,
        label_visibility="collapsed",
        key="prefs_area"
    )
    st.session_state.preferences = preferences
    
    # Generate Test Button
    st.divider()
    if st.button("🎯 Generate Test", use_container_width=True, type="primary"):
        st.success("Mock test generated successfully!")
        st.balloons()

# Right Sidebar - Test Summary
with col2:
    st.markdown("### Test Summary")
    
    # Extract paper type display
    if st.session_state.exam_type == "Prelims":
        paper_display = "GS1"
    else:
        # Extract just the GS code from the full paper type name
        full_paper = st.session_state.paper_type
        if full_paper:
            paper_display = full_paper.split(" - ")[0].split(" Case")[0] if " - " in full_paper or " Case" in full_paper else full_paper.split()[0]
        else:
            paper_display = "N/A"
    
    # Build summary data
    summary_data = {
        "Language": st.session_state.language,
        "Exam Type": st.session_state.exam_type,
        "Paper Type": paper_display,
        "Number of Questions": f"{st.session_state.num_questions} / {st.session_state.num_questions}",
        "Question Source": st.session_state.question_source,
        "Current Affairs Integration": st.session_state.ca_integration
    }
    
    for key, value in summary_data.items():
        st.markdown(f"**{key}:**")
        st.markdown(f"<div style='margin-left: 10px;'>{value}</div>", unsafe_allow_html=True)
        st.divider()
    
    st.info("💡 Click \"Generate Test\" to create your personalized mock test")