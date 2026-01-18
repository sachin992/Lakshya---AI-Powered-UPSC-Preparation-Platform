
import streamlit as st

def show():
    st.markdown("## 📊 Dashboard")
    st.info("Your learning progress and statistics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tests Completed", "12")
    with col2:
        st.metric("Avg Score", "72%")
    with col3:
        st.metric("Study Hours", "48")