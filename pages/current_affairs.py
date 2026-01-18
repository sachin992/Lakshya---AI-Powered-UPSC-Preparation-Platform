import streamlit as st
from datetime import datetime, timedelta
import calendar

def show():
    # REMOVE st.set_page_config() - it's already in app.py
    # REMOVE the sidebar menu - it's already in app.py
    
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