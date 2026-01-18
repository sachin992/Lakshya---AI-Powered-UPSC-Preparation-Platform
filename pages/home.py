
import streamlit as st

def show():
    st.markdown("""
    <h1 style='text-align: center; color: #0052cc;'>Welcome to Dalvoy</h1>
    <p style='text-align: center; font-size: 18px; color: #666;'>Master UPSC with AI-Powered Learning</p>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🚀 Quick Start")
        if st.button("⚡ UPSC GPT", use_container_width=True, key="qs_gpt"):
            st.session_state.current_page = "upsc_gpt"
            st.rerun()
        if st.button("📰 Current Affairs", use_container_width=True, key="qs_ca"):
            st.session_state.current_page = "current_affairs"
            st.rerun()
    
    with col2:
        st.markdown("### 📚 Practice")
        if st.button("📝 Test Generator", use_container_width=True, key="qs_test"):
            st.session_state.current_page = "test_generator"
            st.rerun()
        if st.button("🧩 UPSC Puzzle", use_container_width=True, key="qs_puzzle"):
            st.session_state.current_page = "upsc_puzzle"
            st.rerun()
    
    with col3:
        st.markdown("### ✅ Evaluate")
        if st.button("📋 Mains Evaluator", use_container_width=True, key="qs_eval"):
            st.session_state.current_page = "mains_evaluator"
            st.rerun()
        if st.button("🗺️ AI Maps", use_container_width=True, key="qs_maps"):
            st.session_state.current_page = "ai_maps"
            st.rerun()