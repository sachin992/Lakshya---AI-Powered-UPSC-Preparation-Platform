


import streamlit as st
from streamlit_option_menu import option_menu
import login
from pages import (
    home, upsc_gpt, current_affairs, mains_evaluator,
    test_generator, upsc_puzzle, dashboard
)
import os
import sqlite3

# ==================== DATABASE INITIALIZATION ====================
def init_app_database():
    """Initialize database on app startup"""
    try:
        conn = sqlite3.connect("lakshya_users.db")
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                password_hash TEXT NOT NULL,
                bpsc_attempt TEXT,
                commitment_4hrs BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Database initialization error: {e}")
        return False

# Initialize database at startup
if not init_app_database():
    st.error("Failed to initialize database")
    st.stop()

# Page config
st.set_page_config(
    page_title="Lakhsya - UPSC Preparation", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        header[data-testid="stHeader"] {
            display: none;
        }
        
        .main .block-container {
            max-width: 100%;
            padding-top: 1rem;
        }
        
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
        }
        
        [data-testid="collapsedControl"] {
            display: block !important;
            visibility: visible !important;
            z-index: 9999 !important;
        }
        
        [data-testid="collapsedControl"] button {
            display: block !important;
            visibility: visible !important;
            padding: 10px 15px !important;
            background-color: #0052cc !important;
            color: white !important;
            border: none !important;
            border-radius: 5px !important;
            cursor: pointer !important;
            font-size: 20px !important;
            font-weight: bold !important;
        }
        
        [data-testid="collapsedControl"] button:hover {
            background-color: #003d99 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "username" not in st.session_state:
    st.session_state.username = ""
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# URL-based routing
query_params = st.query_params

# Check if URL contains a page parameter
if "page" in query_params:
    requested_page = query_params["page"]
    st.session_state.current_page = requested_page

# Page mapping
page_mapping = {
    "home": home.show,
    "upsc_gpt": upsc_gpt.show,
    "current_affairs": current_affairs.show,
    "mains_evaluator": mains_evaluator.show,
    "test_generator": test_generator.show,
    "upsc_puzzle": upsc_puzzle.show,
    "dashboard": dashboard.show,
}

# LOGIN PAGE
if not st.session_state.logged_in:
    login.show_login()

# MAIN APP - After Login
else:
    # Sidebar Menu - Common for all pages
    with st.sidebar:
        st.markdown(f"<h3>👋 Hi, {st.session_state.username}!</h3>", unsafe_allow_html=True)
        st.divider()
        
        # Menu options
        menu_options = ["Home", "UPSC GPT", "Test Generator", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard"]
        
        # Find current index
        current_index = 0
        for i, option in enumerate(menu_options):
            if option.lower().replace(" ", "_") == st.session_state.current_page:
                current_index = i
                break
        
        selected = option_menu(
            menu_title="Menu",
            options=menu_options,
            icons=["house", "lightning-charge", "file-text", "pencil-square", "newspaper", "puzzle", "speedometer"],
            menu_icon="cast",
            default_index=current_index,
            key="sidebar_menu",
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f9fa"},
                "icon": {"color": "#0052cc", "font-size": "20px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#0052cc"}
            }
        )
        
        page_name = selected.lower().replace(" ", "_")
        st.session_state.current_page = page_name
        
        # Update URL when menu item is clicked
        st.query_params["page"] = page_name
        
        st.divider()
        if st.button("🚪 Logout", use_container_width=True, key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.user_id = None
            st.query_params.clear()
            st.rerun()

    # Route to different pages
    if st.session_state.current_page in page_mapping:
        page_mapping[st.session_state.current_page]()
    else:
        # Default to home if page not found
        st.session_state.current_page = "home"
        st.query_params["page"] = "home"
        st.rerun()