import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime



# Page config
st.set_page_config(page_title="Dalvoy - UPSC Preparation", layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "upsc_gpt"
if "username" not in st.session_state:
    st.session_state.username = ""

# LOGIN PAGE
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: #0052cc;'>🎓 Dalvoy</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>Master UPSC with AI-Powered Learning</p>", unsafe_allow_html=True)
        
        st.divider()
        
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.markdown("### Login to Your Account")
            email = st.text_input("Email", placeholder="your@email.com", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login", use_container_width=True, type="primary", key="login_btn"):
                if email and password:
                    st.session_state.logged_in = True
                    st.session_state.username = email.split('@')[0]
                    st.success(f"Welcome {st.session_state.username}!")
                    st.rerun()
                else:
                    st.error("Please enter email and password")
        
        with tab2:
            st.markdown("### Create New Account")
            new_email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
            new_password = st.text_input("Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
            
            if st.button("Sign Up", use_container_width=True, type="primary", key="signup_btn"):
                if new_email and new_password and confirm_password:
                    if new_password == confirm_password:
                        st.session_state.logged_in = True
                        st.session_state.username = new_email.split('@')[0]
                        st.success(f"Account created! Welcome {st.session_state.username}!")
                        st.rerun()
                    else:
                        st.error("Passwords don't match!")
                else:
                    st.error("Please fill all fields")

# MAIN APP - After Login
else:
    # Sidebar Menu - Common for all pages
    with st.sidebar:
        st.markdown(f"<h3>👋 Hi, {st.session_state.username}!</h3>", unsafe_allow_html=True)
        st.divider()
        
        selected = option_menu(
            menu_title="Menu",
            options=["UPSC GPT", "Test Generator", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
            icons=["lightning-charge", "file-text", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
            menu_icon="cast",
            default_index=0,
            key="sidebar_menu"
        )
        
        st.session_state.current_page = selected.lower().replace(" ", "_")
        
        st.divider()
        if st.button("🚪 Logout", use_container_width=True, key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()
  
    # ==================== UPSC GPT PAGE ====================
    if st.session_state.current_page == "upsc_gpt":
       

        

        # Page config
        st.set_page_config(page_title="Dalvoy - UPSC GPT", layout="wide")

        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "show_feedback_modal" not in st.session_state:
            st.session_state.show_feedback_modal = False
        if "rating" not in st.session_state:
            st.session_state.rating = 0
        if "feedback_text" not in st.session_state:
            st.session_state.feedback_text = ""

        # Sidebar Menu
        with st.sidebar:
            st.markdown("### Menu")
            selected = option_menu(
                menu_title="",
                options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
                icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
                menu_icon="cast",
                default_index=0,
            )
            
            st.divider()
            st.markdown("### Conversation")
            if st.button("+ New Chat", use_container_width=True, key="new_chat_btn"):
                st.session_state.messages = []

            st.divider()
            if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
                pass

        # Top Header with options
        col1, col2, col3, col4 = st.columns([3, 0.5, 0.5, 1])

        with col1:
            st.markdown("## UPSC GPT")

        with col2:
            if st.button("📄", help="Text Mode", use_container_width=True, key="text_mode_btn"):
                pass

        with col3:
            if st.button("🌐", help="Language", use_container_width=True, key="lang_btn"):
                pass

        with col4:
            if st.button("📝 Give Feedback", use_container_width=True, key="give_feedback_btn"):
                st.session_state.show_feedback_modal = True

        st.divider()

        # Main Chat Area
        st.markdown("### What can I help with?")

        # Suggested questions
        st.markdown("**Choose a mode:**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("TEXT", use_container_width=True, type="primary", key="text_choice_btn"):
                pass
        with col2:
            if st.button("AUDIO", use_container_width=True, key="audio_choice_btn"):
                pass

        st.markdown("**Suggested questions**")

        suggested_questions = [
            "Give previous year prelims questions on lakes",
            "Explain the concept of Federalism",
            "Give me top foreign policy current affairs",
            "Create a 30-day study plan for UPSC Prelims"
        ]

        for idx, question in enumerate(suggested_questions):
            if st.button(f"❓ {question}", use_container_width=True, key=f"suggested_q_{idx}"):
                st.session_state.messages.append({"role": "user", "content": question})
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"I'll help you with: {question}\n\n[Response content will appear here]"
                })

        # Chat messages display
        if st.session_state.messages:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Chat input
        st.divider()
        col1, col2 = st.columns([6, 1])

        with col1:
            user_input = st.text_input("Ask anything...", placeholder="Ask anything...", label_visibility="collapsed", key="chat_input")

        with col2:
            if st.button("➤", use_container_width=True, type="primary", key="send_btn"):
                if user_input:
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": f"Response to: {user_input}\n\n[This is a sample response]"
                    })

        # Feedback Modal - Only displayed when show_feedback_modal is True
        if st.session_state.show_feedback_modal:
            @st.dialog("Share Your Feedback", width="medium")
            def show_feedback_form():
                st.markdown("**Rate this conversation**")
                
                # Rating Section with stars
                rating_cols = st.columns(5)
                
                for i in range(5):
                    with rating_cols[i]:
                        star_value = i + 1
                        if st.button("⭐", key=f"star_{star_value}", use_container_width=True):
                            st.session_state.rating = star_value
                
                # Display selected rating
                if st.session_state.rating > 0:
                    st.markdown(f"**You rated: {st.session_state.rating} / 5 stars**")
                
                st.divider()
                
                # Feedback Text Area
                st.markdown("**Tell us more (optional)**")
                feedback_text = st.text_area(
                    "Tell us more",
                    value=st.session_state.feedback_text,
                    placeholder="What did you like or dislike about this conversation?",
                    height=120,
                    label_visibility="collapsed",
                    key="feedback_textarea"
                )
                st.session_state.feedback_text = feedback_text
                
                # Character count
                st.caption(f"{len(feedback_text)}/500 characters")
                
                st.divider()
                
                # Buttons
                col_btn1, col_btn2 = st.columns([1, 1])
                with col_btn1:
                    if st.button("Cancel", use_container_width=True, key="cancel_feedback_btn"):
                        st.session_state.show_feedback_modal = False
                        st.session_state.rating = 0
                        st.session_state.feedback_text = ""
                
                with col_btn2:
                    if st.button("Submit", use_container_width=True, type="primary", key="submit_feedback_btn"):
                        if st.session_state.rating > 0 or st.session_state.feedback_text:
                            st.success("✅ Thank you for your feedback!")
                            feedback_data = {
                                "rating": st.session_state.rating,
                                "feedback": st.session_state.feedback_text,
                                "timestamp": datetime.now()
                            }
                            st.session_state.show_feedback_modal = False
                            st.session_state.rating = 0
                            st.session_state.feedback_text = ""
                        else:
                            st.warning("Please provide at least a rating or feedback")
            
            show_feedback_form()

    # ==================== CURRENT AFFAIRS PAGE ====================
    elif st.session_state.current_page == "current_affairs":


        import streamlit as st
        from streamlit_option_menu import option_menu
        from datetime import datetime, timedelta
        import calendar

        # Page config
        st.set_page_config(page_title="Dalvoy - Current Affairs", layout="wide")

        # Initialize session state
        if "selected_language" not in st.session_state:
            st.session_state.selected_language = "English"
        if "selected_date" not in st.session_state:
            st.session_state.selected_date = datetime.now().date()
        if "selected_prelims_topics" not in st.session_state:
            st.session_state.selected_prelims_topics = []
        if "selected_mains_topics" not in st.session_state:
            st.session_state.selected_mains_topics = []
        if "prelims_expanded" not in st.session_state:
            st.session_state.prelims_expanded = True
        if "mains_expanded" not in st.session_state:
            st.session_state.mains_expanded = False

        # Category structure
        prelims_categories = [
            "Geography",
            "Environment",
            "Science And Technology",
            "International Relations",
            "Government Schemes",
            "Art And Culture"
        ]

        mains_categories = {
            "GS1": ["GS1-Indian Heritage And Culture", "GS1-History", "GS1-Geography", "GS1-Society"],
            "GS2": ["GS2-Polity And Constitution", "GS2-Governance"],
            "GS3": ["GS3-Economy", "GS3-Infrastructure", "GS3-Security"],
            "GS4": ["GS4-Ethics", "GS4-Integrity"]
        }

        # Sample current affairs data
        sample_affairs = [
            {
                "title": "Quick Commerce Firms Halt 10-Minute Delivery",
                "description": "Quick commerce platforms like Blinkit and Zepto have decided to stop offering 10-minute delivery services following intervention...",
                "tags": ["Economy", "GS2-Social Justice"],
                "date": "January 14, 2026"
            },
            {
                "title": "RBI Proposes Reopening UCB Licenses, Favors Large Societies",
                "description": "The RBI is considering reopening the licensing window for Urban Co-operative Banks (UCBs), but proposes prioritizing larger co-...",
                "tags": ["Economy", "GS3-Economy"],
                "date": "January 14, 2026"
            },
            {
                "title": "New Environmental Policy Framework Announced",
                "description": "Government announces comprehensive environmental policy addressing climate change and sustainable development...",
                "tags": ["Environment", "GS1-Geography"],
                "date": "January 13, 2026"
            }
        ]

        # Sidebar Menu
        with st.sidebar:
            st.markdown("### Menu")
            selected = option_menu(
                menu_title="",
                options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
                icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
                menu_icon="cast",
                default_index=4,
            )
            
            st.divider()
            if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
                pass

        # Top Language Selection
        col1, col2 = st.columns([5, 1])

        with col2:
            lang_col1, lang_col2 = st.columns(2)
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

        st.divider()

        # Main Content
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("## Current Affairs")
            
            # Affairs Cards
            for affair in sample_affairs:
                with st.container():
                    col_tag1, col_tag2, col_date = st.columns([1, 2, 1])
                    
                    with col_tag1:
                        st.markdown(f'<span style="background-color: #c8e6c9; color: #2e7d32; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 500;">{affair["tags"][0]}</span>', unsafe_allow_html=True)
                    
                    with col_tag2:
                        st.markdown(f'<span style="background-color: #ffe0b2; color: #e65100; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 500; margin-left: 8px;">{affair["tags"][1]}</span>', unsafe_allow_html=True)
                    
                    with col_date:
                        st.markdown(f'<div style="text-align: right; color: #999; font-size: 12px;">{affair["date"]}</div>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h3 style="color: #1e40af; margin: 12px 0 8px 0;">{affair["title"]}</h3>', unsafe_allow_html=True)
                    st.markdown(f'<p style="color: #666; margin: 0;">{affair["description"]}</p>', unsafe_allow_html=True)
                    st.divider()

        # Right Sidebar - Filters and Calendar
        with col2:
            # Calendar Section
            st.markdown("### Calendar")
            
            # Month/Year Navigation
            cal_col1, cal_col2, cal_col3 = st.columns([0.5, 2, 0.5])
            
            with cal_col1:
                if st.button("◀", key="prev_month_btn", use_container_width=True):
                    current_date = st.session_state.selected_date
                    first_day = current_date.replace(day=1)
                    prev_month = first_day - timedelta(days=1)
                    st.session_state.selected_date = prev_month
            
            with cal_col2:
                # Month and Year selector
                months = ["January", "February", "March", "April", "May", "June", 
                        "July", "August", "September", "October", "November", "December"]
                current_month = st.session_state.selected_date.month
                current_year = st.session_state.selected_date.year
                
                month_col, year_col = st.columns(2)
                with month_col:
                    selected_month_name = st.selectbox(
                        "Month",
                        months,
                        index=current_month - 1,
                        label_visibility="collapsed",
                        key="month_select"
                    )
                    selected_month = months.index(selected_month_name) + 1
                
                with year_col:
                    selected_year = st.selectbox(
                        "Year",
                        [2025, 2026, 2027],
                        index=2 if current_year == 2026 else (0 if current_year == 2025 else 1),
                        label_visibility="collapsed",
                        key="year_select"
                    )
                
                # Update selected date
                if selected_month != current_month or selected_year != current_year:
                    st.session_state.selected_date = st.session_state.selected_date.replace(
                        month=selected_month, 
                        year=selected_year,
                        day=1
                    )
            
            with cal_col3:
                if st.button("▶", key="next_month_btn", use_container_width=True):
                    current_date = st.session_state.selected_date
                    last_day = calendar.monthrange(current_date.year, current_date.month)[1]
                    next_month = current_date.replace(day=last_day) + timedelta(days=1)
                    st.session_state.selected_date = next_month
            
            # Calendar Grid
            cal_date = st.session_state.selected_date
            month_calendar = calendar.monthcalendar(cal_date.year, cal_date.month)
            
            # Days of week header
            days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            day_cols = st.columns(7)
            for i, day in enumerate(days):
                with day_cols[i]:
                    st.markdown(f'<p style="text-align: center; font-weight: bold; color: #1e40af; margin: 0; font-size: 12px;">{day}</p>', unsafe_allow_html=True)
            
            # Calendar days - one row per week
            for week_idx, week in enumerate(month_calendar):
                week_cols = st.columns(7)
                for day_col_idx, day in enumerate(week):
                    with week_cols[day_col_idx]:
                        if day == 0:
                            st.markdown("")
                        else:
                            is_selected = day == st.session_state.selected_date.day and \
                                        cal_date.month == st.session_state.selected_date.month and \
                                        cal_date.year == st.session_state.selected_date.year
                            
                            # Use unique key for each day
                            button_key = f"cal_day_{week_idx}_{day_col_idx}_{cal_date.year}_{cal_date.month}_{day}"
                            
                            if is_selected:
                                st.button(
                                    str(day),
                                    key=button_key,
                                    use_container_width=True,
                                    type="primary"
                                )
                            else:
                                if st.button(
                                    str(day),
                                    key=button_key,
                                    use_container_width=True
                                ):
                                    st.session_state.selected_date = cal_date.replace(day=day)
            
            st.divider()
            
            # Categories Section
            st.markdown("### Categories")
            
            # Prelims Section
            if st.button("Prelims", key="prelims_toggle", use_container_width=True):
                st.session_state.prelims_expanded = not st.session_state.prelims_expanded
            
            if st.session_state.prelims_expanded:
                for category in prelims_categories:
                    st.checkbox(
                        category,
                        value=category in st.session_state.selected_prelims_topics,
                        key=f"prelims_{category}",
                        on_change=lambda cat=category: (
                            st.session_state.selected_prelims_topics.append(cat)
                            if cat not in st.session_state.selected_prelims_topics
                            else st.session_state.selected_prelims_topics.remove(cat)
                        )
                    )
            
            st.divider()
            
            # Mains Section
            if st.button("Mains", key="mains_toggle", use_container_width=True):
                st.session_state.mains_expanded = not st.session_state.mains_expanded
            
            if st.session_state.mains_expanded:
                for gs_type, categories in mains_categories.items():
                    with st.expander(gs_type, expanded=False):
                        for category in categories:
                            st.checkbox(
                                category,
                                value=category in st.session_state.selected_mains_topics,
                                key=f"mains_{category}",
                                on_change=lambda cat=category: (
                                    st.session_state.selected_mains_topics.append(cat)
                                    if cat not in st.session_state.selected_mains_topics
                                    else st.session_state.selected_mains_topics.remove(cat)
                                )
                            )
            
            st.divider()
            
            # Apply Filter Button
            if st.button("Apply Filter", use_container_width=True, type="primary", key="apply_filter_btn"):
                st.success("✅ Filters applied! Current affairs updated.")
            
            # Clear Filters Button
            if st.button("Clear Filters", use_container_width=True, key="clear_filter_btn"):
                st.session_state.selected_prelims_topics = []
                st.session_state.selected_mains_topics = []
                st.success("✅ Filters cleared!")
    
    # ==================== MAINS EVALUATOR PAGE ====================
    elif st.session_state.current_page == "mains_evaluator":
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
    
    # ==================== UPSC PUZZLE PAGE ====================
    elif st.session_state.current_page == "upsc_puzzle":
                
        import streamlit as st
        from streamlit_option_menu import option_menu
        import random

        # Page config
        st.set_page_config(page_title="Dalvoy - UPSC Puzzle", layout="wide")

        # Initialize session state
        if "puzzle_page" not in st.session_state:
            st.session_state.puzzle_page = "quiz_type"
        if "quiz_type" not in st.session_state:
            st.session_state.quiz_type = None
        if "selected_category" not in st.session_state:
            st.session_state.selected_category = None
        if "selected_difficulty" not in st.session_state:
            st.session_state.selected_difficulty = None
        if "show_question_modal" not in st.session_state:
            st.session_state.show_question_modal = False
        if "current_question" not in st.session_state:
            st.session_state.current_question = None
        if "score" not in st.session_state:
            st.session_state.score = 0
        if "attempts_left" not in st.session_state:
            st.session_state.attempts_left = 15
        if "questions_found" not in st.session_state:
            st.session_state.questions_found = 0
        if "grid_revealed" not in st.session_state:
            st.session_state.grid_revealed = set()
        if "selected_answer" not in st.session_state:
            st.session_state.selected_answer = None
        if "show_instructions" not in st.session_state:
            st.session_state.show_instructions = False

        # Categories based on quiz type
        categories = {
            "General Studies": [
                "History & Culture",
                "Geography",
                "Polity & Governance",
                "Economics",
                "Environment & Ecology",
                "Science & Technology",
                "Security & International Relations",
                "All General Studies"
            ],
            "CSAT": [
                "All CSAT Questions"
            ]
        }

        # Sample questions database
        questions_db = {
            "History & Culture": {
                "Beginner": [
                    {"q": "Who was the first President of India?", "year": "Prelims 2018", "options": ["A) Dr. Rajendra Prasad", "B) Dr. S. Radhakrishnan", "C) C. Rajagopalachari", "D) Sardar Vallabhbhai Patel"], "correct": "A"},
                    {"q": "In which year did India gain independence?", "year": "Prelims 2019", "options": ["A) 1945", "B) 1947", "C) 1950", "D) 1952"], "correct": "B"},
                ],
                "Intermediate": [
                    {"q": "The term 'two-state solution' is sometimes mentioned in the news in the context of the affairs of", "year": "Prelims 2018", "options": ["A) China", "B) Israel", "C) Iraq", "D) Yemen"], "correct": "B"},
                ],
                "Advanced": [
                    {"q": "Which dynasty ruled India for the longest period?", "year": "Prelims 2020", "options": ["A) Maurya", "B) Gupta", "C) Mughal", "D) British"], "correct": "C"},
                ]
            },
            "All CSAT Questions": {
                "Beginner": [
                    {"q": "In some code, letters P, Q, R, S, T represent numbers 4, 5, 10, 12, 15. It is not known which letter represents which number. If Q - S = 2S and T = R + S + 3, then what is the value of P + R - T?", "year": "Prelims 2024", "options": ["A) 1", "B) 2", "C) 3", "D) Cannot be determined due to insufficient data"], "correct": "A"},
                    {"q": "If all Roses are Flowers and all Flowers fade, which statement is true?", "year": "Prelims 2023", "options": ["A) All Roses fade", "B) Some Roses fade", "C) No Roses fade", "D) Cannot be determined"], "correct": "A"},
                ],
                "Intermediate": [
                    {"q": "A person walks 10m north, then 20m east, then 10m south. How far is the person from the starting point?", "year": "Prelims 2024", "options": ["A) 20m", "B) 30m", "C) 40m", "D) 50m"], "correct": "A"},
                ],
                "Advanced": [
                    {"q": "In a group of 100 people, 60 speak English and 50 speak Hindi. How many people speak both languages?", "year": "Prelims 2023", "options": ["A) 10", "B) 15", "C) 20", "D) Cannot be determined"], "correct": "A"},
                ]
            }
        }

        # Sidebar Menu
        with st.sidebar:
            st.markdown("### Menu")
            selected = option_menu(
                menu_title="",
                options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
                icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
                menu_icon="cast",
                default_index=5,
            )
            
            st.divider()
            if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
                pass

        # PAGE 1: Quiz Type Selection
        if st.session_state.puzzle_page == "quiz_type":
            st.markdown("<h1 style='text-align: center; color: #1e40af;'>UPSC PYQ Question Sweeper</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-size: 16px;'>Test your UPSC knowledge with this unique quiz-puzzle game using real Previous Year Questions!</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #666;'>Find hidden question blocks by using clues that show how many question blocks are nearby.</p>", unsafe_allow_html=True)
            if st.button("ⓘ How to Play", key="how_to_play_btn", help="Show game instructions"):
                st.session_state.show_instructions = True
            
            if "show_instructions" in st.session_state and st.session_state.show_instructions:
                with st.expander("Hide Instructions", expanded=True):
                    st.markdown("### Game Rules:")
                    st.markdown("• Click on blocks to reveal what's underneath")
                    st.markdown("• Numbers show how many question blocks are adjacent to that cell")
                    st.markdown("• Right-click to flag potential question blocks")
                    st.markdown("• When you find a question block, answer the UPSC question to earn points")
                    st.markdown("• You have limited attempts - use them wisely!")
                    st.markdown("• Find all question blocks to win")
            st.divider()
            st.markdown("<h2 style='text-align: center; color: #1e40af;'>Choose Paper Type</h2>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("General Studies\n\nHistory, Geography, Polity & More", use_container_width=True, key="gs_btn", help="General Studies Questions"):
                    st.session_state.quiz_type = "General Studies"
                    st.session_state.puzzle_page = "category"
                    st.rerun()
            
            with col2:
                if st.button("CSAT\n\nQuantitative Aptitude & Reasoning", use_container_width=True, key="csat_btn", help="CSAT Questions"):
                    st.session_state.quiz_type = "CSAT"
                    st.session_state.puzzle_page = "category"
                    st.rerun()

        # PAGE 2: Category Selection
        elif st.session_state.puzzle_page == "category":
            if st.button("← Back to Question Types", key="back_to_types_btn"):
                st.session_state.puzzle_page = "quiz_type"
                st.session_state.quiz_type = None
                st.rerun()
            
            st.markdown(f"<h2 style='text-align: center; color: #1e40af;'>{st.session_state.quiz_type}</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #666;'>Select a category to start playing</p>", unsafe_allow_html=True)
            st.divider()
            
            cats = categories[st.session_state.quiz_type]
            
            if st.session_state.quiz_type == "CSAT":
                col1, col2, col3 = st.columns([1, 1.5, 1])
                with col2:
                    if st.button(cats[0], use_container_width=True, key="cat_0"):
                        st.session_state.selected_category = cats[0]
                        st.session_state.puzzle_page = "difficulty"
                        st.rerun()
            else:
                cols = st.columns(3)
                for idx, cat in enumerate(cats):
                    col_idx = idx % 3
                    with cols[col_idx]:
                        if st.button(cat, use_container_width=True, key=f"cat_{idx}"):
                            st.session_state.selected_category = cat
                            st.session_state.puzzle_page = "difficulty"
                            st.rerun()

        # PAGE 3: Difficulty Selection
        elif st.session_state.puzzle_page == "difficulty":
            if st.button("← Back to Question Types", key="back_to_types_btn2"):
                st.session_state.puzzle_page = "quiz_type"
                st.session_state.quiz_type = None
                st.session_state.selected_category = None
                st.rerun()
            
            st.markdown(f"<h2 style='text-align: center; color: #1e40af;'>{st.session_state.quiz_type}</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #666;'>Select a category to start playing</p>", unsafe_allow_html=True)
            
            cat_col1, cat_col2, cat_col3 = st.columns(3)
            with cat_col2:
                st.button(st.session_state.selected_category, use_container_width=True, disabled=True, key="selected_cat")
            
            st.divider()
            st.markdown("<h3 style='text-align: center; color: #1e40af;'>Select Difficulty</h3>", unsafe_allow_html=True)
            
            difficulty_cols = st.columns(3)
            difficulty_levels = [
                ("Beginner", "5×5 Grid\n6 Questions"),
                ("Intermediate", "6×6 Grid\n8 Questions"),
                ("Advanced", "8×8 Grid\n12 Questions")
            ]
            
            for idx, (level, desc) in enumerate(difficulty_levels):
                with difficulty_cols[idx]:
                    if st.button(f"{level}\n\n{desc}", use_container_width=True, key=f"diff_{level}"):
                        st.session_state.selected_difficulty = level
                        st.session_state.puzzle_page = "game"
                        if level == "Beginner":
                            st.session_state.grid_size = 5
                            st.session_state.total_questions = 6
                        elif level == "Intermediate":
                            st.session_state.grid_size = 6
                            st.session_state.total_questions = 8
                        else:
                            st.session_state.grid_size = 8
                            st.session_state.total_questions = 12
                        st.rerun()

        # PAGE 4: Game Grid
        elif st.session_state.puzzle_page == "game":
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"<h3 style='margin: 0;'>UPSC PYQ Question Sweeper</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin: 0; color: #666; font-size: 14px;'>{st.session_state.selected_category} - {st.session_state.selected_difficulty} Level</p>", unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"<h4 style='text-align: right; color: #1e40af;'>Score: {st.session_state.score}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: right;'>ⓘ</p>", unsafe_allow_html=True)
            
            st.divider()
            
            grid_size = st.session_state.grid_size
            question_positions = set(random.sample(range(grid_size * grid_size), st.session_state.total_questions))
            
            cols = st.columns(grid_size)
            
            for i in range(grid_size * grid_size):
                col_idx = i % grid_size
                
                if col_idx == 0 and i > 0:
                    cols = st.columns(grid_size)
                
                with cols[col_idx]:
                    cell_key = f"cell_{i}"
                    
                    if i in st.session_state.grid_revealed:
                        question_num = len([q for q in st.session_state.grid_revealed if q < i]) + 1
                        st.button(str(question_num), key=cell_key, use_container_width=True, disabled=True)
                    elif i in question_positions:
                        if st.button("?", key=cell_key, use_container_width=True, help="Click to reveal question"):
                            st.session_state.grid_revealed.add(i)
                            st.session_state.current_question = {
                                "title": "UPSC Question",
                                "year": "Prelims 2018",
                                "text": 'The term "two-state solution" is sometimes mentioned in the news in the context of the affairs of',
                                "options": ["A) China", "B) Israel", "C) Iraq", "D) Yemen"]
                            }
                            st.session_state.show_question_modal = True
                            st.rerun()
                    else:
                        st.button("", key=cell_key, use_container_width=True, disabled=True)
            
            st.divider()
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col1:
                st.markdown(f"<p style='color: #666;'>{st.session_state.attempts_left} attempts left</p>", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"<p style='text-align: center; color: #ff9800;'>{st.session_state.total_questions - len(st.session_state.grid_revealed)} questions to find</p>", unsafe_allow_html=True)
            
            with col3:
                if st.button("🔄 Restart", use_container_width=True, key="restart_btn"):
                    st.session_state.puzzle_page = "quiz_type"
                    st.session_state.quiz_type = None
                    st.session_state.selected_category = None
                    st.session_state.selected_difficulty = None
                    st.session_state.score = 0
                    st.session_state.attempts_left = 15
                    st.session_state.questions_found = 0
                    st.session_state.grid_revealed = set()
                    st.rerun()
            
            # Question Modal
            if st.session_state.show_question_modal and st.session_state.current_question:
                @st.dialog("UPSC Question", width="medium")
                def show_question():
                    q = st.session_state.current_question
                    
                    st.markdown(f"**{q['title']}**")
                    st.markdown(f"*{q['year']}*")
                    st.divider()
                    
                    st.markdown(q['text'])
                    st.divider()
                    
                    for idx, option in enumerate(q['options']):
                        if st.button(option, use_container_width=True, key=f"opt_{idx}_{option}"):
                            st.session_state.selected_answer = option
                    
                    st.divider()
                    
                    submit_col1, submit_col2 = st.columns([1, 1])
                    
                    with submit_col1:
                        if st.button("Submit Answer", use_container_width=True, key="submit_ans_btn"):
                            if st.session_state.selected_answer:
                                st.success("✅ Correct Answer!")
                                st.session_state.score += 10
                                st.session_state.attempts_left -= 1
                                st.session_state.questions_found += 1
                                st.session_state.show_question_modal = False
                                st.session_state.selected_answer = None
                                import time
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.warning("Please select an answer first")
                    
                    with submit_col2:
                        if st.button("Close", use_container_width=True, key="close_modal_btn"):
                            st.session_state.show_question_modal = False
                            st.session_state.selected_answer = None
                            st.rerun()
                
                show_question()
    
    # ==================== AI MAPS PAGE ====================

    
    # ==================== HOME PAGE ====================
    elif st.session_state.current_page == "home":
        st.markdown("""
        <h1 style='text-align: center; color: #0052cc;'>Welcome to GoUPSC</h1>
        <p style='text-align: center; font-size: 18px; color: #666;'>Master UPSC with AI-Powered Learning</p>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### 🚀 Quick Start")
            st.button("UPSC GPT", use_container_width=True, key="qs_gpt")
            st.button("Current Affairs", use_container_width=True, key="qs_ca")
        
        with col2:
            st.markdown("### 📚 Practice")
            st.button("Test Generator", use_container_width=True, key="qs_test")
            st.button("UPSC Puzzle", use_container_width=True, key="qs_puzzle")
        
        with col3:
            st.markdown("### ✅ Evaluate")
            st.button("Mains Evaluator", use_container_width=True, key="qs_eval")
          
    
    # ==================== DASHBOARD PAGE ====================
    elif st.session_state.current_page == "dashboard":
        st.markdown("## 📊 Dashboard")
        st.info("Your learning progress and statistics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tests Completed", "12")
        with col2:
            st.metric("Avg Score", "72%")
        with col3:
            st.metric("Study Hours", "48")
    else:
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