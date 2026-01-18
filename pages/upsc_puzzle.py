import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu
import random
def show():
        
  

    # Page config
    # st.set_page_config(page_title="Dalvoy - UPSC Puzzle", layout="wide")

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
    # with st.sidebar:
    #     st.markdown("### Menu")
    #     selected = option_menu(
    #         menu_title="",
    #         options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
    #         icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
    #         menu_icon="cast",
    #         default_index=5,
    #     )
        
    #     st.divider()
    #     if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
    #         pass

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