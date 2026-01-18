

# import streamlit as st
# from streamlit_option_menu import option_menu
# import time
# from datetime import datetime, timedelta
# from final_backend import generate_questions
# import json

# def show():
#     # Page config
#     st.set_page_config(page_title="Dalvoy - Mock Test", layout="wide")

#     # Custom CSS for better styling
#     st.markdown("""
#     <style>
#     .question-nav-btn {
#         width: 50px;
#         height: 50px;
#         border-radius: 8px;
#         margin: 5px;
#         font-weight: bold;
#         font-size: 16px;
#     }
#     .timer-box {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 20px;
#         border-radius: 12px;
#         text-align: center;
#         font-size: 24px;
#         font-weight: bold;
#         margin-bottom: 20px;
#     }
#     .instruction-card {
#         background: white;
#         padding: 30px;
#         border-radius: 12px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         margin: 20px auto;
#         max-width: 800px;
#     }
#     .instruction-item {
#         padding: 12px 0;
#         border-bottom: 1px solid #f0f0f0;
#     }
#     .question-card {
#         background: white;
#         padding: 30px;
#         border-radius: 12px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
#         margin-bottom: 20px;
#     }
#     .option-box {
#         padding: 15px;
#         border: 2px solid #e0e0e0;
#         border-radius: 8px;
#         margin: 10px 0;
#         cursor: pointer;
#         transition: all 0.3s;
#     }
#     .option-box:hover {
#         border-color: #4CAF50;
#         background: #f0f9f0;
#     }
#     .sidebar-timer {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 15px;
#         border-radius: 10px;
#         text-align: center;
#         margin-bottom: 20px;
#     }
#     .question-nav-container {
#         display: flex;
#         flex-wrap: wrap;
#         gap: 10px;
#         margin: 20px 0;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Initialize session state
#     if "exam_type" not in st.session_state:
#         st.session_state.exam_type = "Prelims"
#     if "language" not in st.session_state:
#         st.session_state.language = "English"
#     if "paper_type" not in st.session_state:
#         st.session_state.paper_type = "General Studies (Paper I) - History, Geography, Polity, Economics, etc."
#     if "num_questions" not in st.session_state:
#         st.session_state.num_questions = 5
#     if "question_source" not in st.session_state:
#         st.session_state.question_source = "Mock Questions"
#     if "ca_integration" not in st.session_state:
#         st.session_state.ca_integration = "Off"
#     if "preferences" not in st.session_state:
#         st.session_state.preferences = ""
#     if "test_stage" not in st.session_state:
#         st.session_state.test_stage = "setup"  # setup, loading, instructions, test, results
#     if "questions" not in st.session_state:
#         st.session_state.questions = []
#     if "user_answers" not in st.session_state:
#         st.session_state.user_answers = {}
#     if "test_start_time" not in st.session_state:
#         st.session_state.test_start_time = None
#     if "test_duration" not in st.session_state:
#         st.session_state.test_duration = 0
#     if "time_expired" not in st.session_state:
#         st.session_state.time_expired = False
#     if "current_question" not in st.session_state:
#         st.session_state.current_question = 1
#     if "generation_progress" not in st.session_state:
#         st.session_state.generation_progress = 0

#     # Define paper types based on exam type
#     paper_types = {
#         "Prelims": ["General Studies (Paper I) - History, Geography, Polity, Economics, etc."],
#         "Mains": [
#             "GS1 - Indian Heritage and Culture, History and Geography",
#             "GS2 - Governance, Constitution, Polity, Social Justice, International Relations",
#             "GS3 - Technology, Economic Development, Environment, Security",
#             "GS4 - Ethics, Integrity, Aptitude",
#             "GS4 Case Study",
#             "Optional"
#         ]
#     }

#     # ==================== SETUP STAGE ====================
#     if st.session_state.test_stage == "setup":
#         col1, col2 = st.columns([2, 1])

#         with col1:
#             st.markdown("## Create Your Mock Test")
            
#             # Exam Type
#             st.markdown("### Exam Type")
#             exam_col1, exam_col2 = st.columns(2)
#             with exam_col1:
#                 if st.button("Prelims", use_container_width=True, 
#                             type="primary" if st.session_state.exam_type == "Prelims" else "secondary"):
#                     st.session_state.exam_type = "Prelims"
#                     st.session_state.paper_type = "General Studies (Paper I) - History, Geography, Polity, Economics, etc."
#                     st.rerun()
            
#             with exam_col2:
#                 if st.button("Mains", use_container_width=True,
#                             type="primary" if st.session_state.exam_type == "Mains" else "secondary"):
#                     st.session_state.exam_type = "Mains"
#                     st.session_state.paper_type = "GS1 - Indian Heritage and Culture, History and Geography"
#                     st.rerun()
            
#             # Language
#             st.markdown("### Language")
#             lang_col1, lang_col2 = st.columns(2)
#             with lang_col1:
#                 if st.button("English", use_container_width=True,
#                             type="primary" if st.session_state.language == "English" else "secondary"):
#                     st.session_state.language = "English"
#                     st.rerun()
            
#             with lang_col2:
#                 if st.button("हिंदी", use_container_width=True,
#                             type="primary" if st.session_state.language == "हिंदी" else "secondary"):
#                     st.session_state.language = "हिंदी"
#                     st.rerun()
            
#             # Paper Type
#             st.markdown("### Paper Type")
#             available_papers = paper_types[st.session_state.exam_type]
            
#             selected_paper = st.selectbox(
#                 "Select Paper",
#                 available_papers,
#                 index=0 if st.session_state.paper_type is None or st.session_state.paper_type not in available_papers else available_papers.index(st.session_state.paper_type),
#                 label_visibility="collapsed",
#                 key="paper_select"
#             )
            
#             if selected_paper != st.session_state.paper_type:
#                 st.session_state.paper_type = selected_paper
#                 st.rerun()
            
#             # Number of Questions
#             st.markdown("### Number of Questions")
#             num_questions = st.slider("", min_value=1, max_value=50, value=st.session_state.num_questions, step=1, key="num_q")
#             st.session_state.num_questions = num_questions
            
#             # Calculate test duration
#             if st.session_state.exam_type == "Prelims":
#                 duration_minutes = num_questions * 2
#             else:
#                 duration_minutes = num_questions * 15
            
#             st.caption(f"Test Duration: {duration_minutes} minutes | {num_questions} questions")
            
#             # Question Source
#             st.markdown("### Question Source")
#             source_col1, source_col2, source_col3 = st.columns(3)
#             with source_col1:
#                 if st.button("Mock Questions", use_container_width=True,
#                             type="primary" if st.session_state.question_source == "Mock Questions" else "secondary"):
#                     st.session_state.question_source = "Mock Questions"
#                     st.rerun()
            
#             with source_col2:
#                 if st.button("Previous Year Questions", use_container_width=True,
#                             type="primary" if st.session_state.question_source == "Previous Year Questions" else "secondary"):
#                     st.session_state.question_source = "Previous Year Questions"
#                     st.rerun()
            
#             with source_col3:
#                 if st.button("Mixed (Mocks & PYQs)", use_container_width=True,
#                             type="primary" if st.session_state.question_source == "Mixed (Mocks & PYQs)" else "secondary"):
#                     st.session_state.question_source = "Mixed (Mocks & PYQs)"
#                     st.rerun()
            
#             # Current Affairs Integration
#             st.markdown("### Current Affairs Integration")
#             ca_col1, ca_col2 = st.columns(2)
#             with ca_col1:
#                 if st.button("On", use_container_width=True,
#                             type="primary" if st.session_state.ca_integration == "On" else "secondary",
#                             key="ca_on_btn"):
#                     st.session_state.ca_integration = "On"
#                     st.rerun()
            
#             with ca_col2:
#                 if st.button("Off", use_container_width=True,
#                             type="primary" if st.session_state.ca_integration == "Off" else "secondary",
#                             key="ca_off_btn"):
#                     st.session_state.ca_integration = "Off"
#                     st.rerun()
            
#             # Specific Preferences
#             st.markdown("### Specific Preferences (Optional)")
#             preferences = st.text_area(
#                 "Enter preferences",
#                 value=st.session_state.preferences,
#                 placeholder="e.g., 'focus on economic policies post-2020', 'environmental governance in urban areas'",
#                 height=80,
#                 label_visibility="collapsed",
#                 key="prefs_area"
#             )
#             st.session_state.preferences = preferences
            
#             # Generate Test Button
#             st.divider()
#             if st.button("🎯 Generate Test", use_container_width=True, type="primary"):
#                 st.session_state.test_stage = "loading"
#                 st.session_state.generation_progress = 0
#                 st.rerun()

#         # Right Sidebar - Test Summary
#         with col2:
#             st.markdown("### 📋 Test Summary")
            
#             if st.session_state.exam_type == "Prelims":
#                 paper_display = "GS1"
#             else:
#                 full_paper = st.session_state.paper_type
#                 if full_paper:
#                     paper_display = full_paper.split(" - ")[0].split(" Case")[0]
#                 else:
#                     paper_display = "N/A"
            
#             summary_data = {
#                 "Language": st.session_state.language,
#                 "Exam Type": st.session_state.exam_type,
#                 "Paper Type": paper_display,
#                 "Questions": f"{st.session_state.num_questions}",
#                 "Source": st.session_state.question_source,
#                 "Current Affairs": st.session_state.ca_integration
#             }
            
#             for key, value in summary_data.items():
#                 st.markdown(f"**{key}:**")
#                 st.markdown(f"<div style='margin-left: 10px;'>{value}</div>", unsafe_allow_html=True)
#                 st.divider()
            
#             st.info("💡 Click \"Generate Test\" to create your personalized mock test")

#     # ==================== LOADING STAGE ====================
#     elif st.session_state.test_stage == "loading":
#         st.markdown("<br><br><br>", unsafe_allow_html=True)
        
#         # Center content
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col2:
#             # Spinning loader animation
#             st.markdown("""
#             <div style="text-align: center;">
#                 <div style="margin: 40px auto;">
#                     <div style="border: 8px solid #f3f3f3; border-top: 8px solid #3498db; 
#                                 border-radius: 50%; width: 80px; height: 80px; 
#                                 animation: spin 1s linear infinite; margin: 0 auto;">
#                     </div>
#                 </div>
#                 <style>
#                 @keyframes spin {
#                     0% { transform: rotate(0deg); }
#                     100% { transform: rotate(360deg); }
#                 }
#                 </style>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("# Live Test Generation in Progress")
#             st.markdown(f"### Generating {st.session_state.num_questions} questions via Question Engine...")
            
#             # Progress bar
#             progress_placeholder = st.empty()
            
#             # Simulate progress and generate questions
#             for i in range(10):
#                 st.session_state.generation_progress = (i + 1) * 10
#                 progress_placeholder.progress(st.session_state.generation_progress / 100, 
#                                              text=f"{st.session_state.generation_progress}% Complete")
#                 time.sleep(0.3)
            
#             # Actually generate questions
#             questions = generate_questions(
#                 exam_type=st.session_state.exam_type,
#                 paper_type=st.session_state.paper_type,
#                 num_questions=st.session_state.num_questions,
#                 question_source=st.session_state.question_source,
#                 ca_integration=st.session_state.ca_integration,
#                 preferences=st.session_state.preferences,
#                 language=st.session_state.language
#             )
            
#             if questions:
#                 st.session_state.questions = questions
#                 st.session_state.user_answers = {}
#                 st.session_state.time_expired = False
#                 st.session_state.current_question = 1
                
#                 # Calculate duration
#                 if st.session_state.exam_type == "Prelims":
#                     st.session_state.test_duration = st.session_state.num_questions * 2
#                 else:
#                     st.session_state.test_duration = st.session_state.num_questions * 15
                
#                 progress_placeholder.progress(1.0, text="100% Complete")
#                 time.sleep(0.5)
#                 st.session_state.test_stage = "instructions"
#                 st.rerun()
#             else:
#                 st.error("Failed to generate questions. Please try again.")
#                 time.sleep(2)
#                 st.session_state.test_stage = "setup"
#                 st.rerun()

#     # ==================== INSTRUCTIONS STAGE ====================
#     elif st.session_state.test_stage == "instructions":
#         st.markdown("<br><br>", unsafe_allow_html=True)
        
#         # Center the instruction card
#         col1, col2, col3 = st.columns([1, 3, 1])
        
#         with col2:
#             st.markdown(f"""
#             <div class="instruction-card">
#                 <h2>🎯 {st.session_state.exam_type} Test Instructions</h2>
#                 <br>
#                 <div class="instruction-item">
#                     <strong>1.</strong> Each question carries equal marks with no negative marking in this practice test
#                 </div>
#                 <div class="instruction-item">
#                     <strong>2.</strong> Select the most appropriate answer for each question
#                 </div>
#                 <div class="instruction-item">
#                     <strong>3.</strong> Review your answers before final submission
#                 </div>
#                 <div class="instruction-item">
#                     <strong>4.</strong> Use proper time management throughout the test
#                 </div>
#                 <div class="instruction-item">
#                     <strong>5.</strong> Test will auto submit if the timer ends
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("<br>", unsafe_allow_html=True)
            
#             # Center the button
#             col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
#             with col_btn2:
#                 if st.button("⚡ Attempt Test", use_container_width=True, type="primary"):
#                     st.session_state.test_start_time = datetime.now()
#                     st.session_state.test_stage = "test"
#                     st.rerun()

#     # ==================== TEST STAGE ====================
#     elif st.session_state.test_stage == "test":
#         # Calculate remaining time
#         elapsed = datetime.now() - st.session_state.test_start_time
#         total_seconds = st.session_state.test_duration * 60
#         remaining_seconds = max(0, total_seconds - int(elapsed.total_seconds()))
        
#         mins, secs = divmod(remaining_seconds, 60)
        
#         # Check if time expired
#         if remaining_seconds == 0 and not st.session_state.time_expired:
#             st.session_state.time_expired = True
#             st.session_state.test_stage = "results"
#             st.rerun()
        
#         # Sidebar with timer and navigation
#         with st.sidebar:
#             st.markdown("### ⏱️ Questions")
            
#             # Timer
#             st.markdown(f"""
#             <div class="sidebar-timer">
#                 <div style="font-size: 14px; margin-bottom: 5px;">⏳ Time Remaining</div>
#                 <div style="font-size: 28px; font-weight: bold;">{mins:02d}:{secs:02d}</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("#### QUESTIONS")
            
#             # Question navigation buttons
#             cols = st.columns(5)
#             for idx, q in enumerate(st.session_state.questions):
#                 col_idx = idx % 5
#                 with cols[col_idx]:
#                     is_answered = q['id'] in st.session_state.user_answers
#                     is_current = st.session_state.current_question == q['id']
                    
#                     button_type = "primary" if is_current else ("secondary" if not is_answered else "secondary")
                    
#                     if st.button(
#                         str(q['id']),
#                         key=f"nav_q_{q['id']}",
#                         use_container_width=True,
#                         type=button_type
#                     ):
#                         st.session_state.current_question = q['id']
#                         st.rerun()
                    
#                     # Show indicator
#                     if is_answered:
#                         st.markdown("<div style='text-align:center; color:green; font-size:20px;'>✓</div>", unsafe_allow_html=True)
            
#             st.divider()
            
#             # Submit button in sidebar
#             if st.button("✅ Submit Test", use_container_width=True, type="primary"):
#                 st.session_state.test_stage = "results"
#                 st.rerun()
        
#         # Main content area
#         current_q = next((q for q in st.session_state.questions if q['id'] == st.session_state.current_question), None)
        
#         if current_q:
#             # Question header
#             st.markdown(f"""
#             <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
#                         color: white; padding: 15px 25px; border-radius: 10px; margin-bottom: 20px;">
#                 <h2 style="margin: 0;">Question {current_q['id']}</h2>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Question card
#             st.markdown(f"""
#             <div class="question-card">
#                 <p style="font-size: 18px; line-height: 1.6; color: #333;">
#                     {current_q['question']}
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("### Select your answer:")
#             st.markdown("<br>", unsafe_allow_html=True)
            
#             if current_q['type'] == 'MCQ':
#                 # Get previous answer
#                 prev_answer = st.session_state.user_answers.get(current_q['id'])
                
#                 # Display options as radio buttons
#                 for key, value in current_q['options'].items():
#                     col1, col2 = st.columns([0.05, 0.95])
                    
#                     with col1:
#                         if st.checkbox("", key=f"opt_{current_q['id']}_{key}", value=(prev_answer == key), label_visibility="collapsed"):
#                             # Uncheck other options
#                             st.session_state.user_answers[current_q['id']] = key
#                             st.rerun()
                    
#                     with col2:
#                         is_selected = prev_answer == key
#                         border_color = "#4CAF50" if is_selected else "#e0e0e0"
#                         bg_color = "#f0f9f0" if is_selected else "white"
                        
#                         st.markdown(f"""
#                         <div style="padding: 15px; border: 2px solid {border_color}; 
#                                     background: {bg_color}; border-radius: 8px; margin-bottom: 15px;">
#                             <strong>{key})</strong> {value}
#                         </div>
#                         """, unsafe_allow_html=True)
            
#             else:  # Descriptive
#                 st.caption(f"📝 Word Limit: {current_q.get('word_limit', 250)} words")
#                 prev_answer = st.session_state.user_answers.get(current_q['id'], "")
                
#                 answer = st.text_area(
#                     "Your Answer:",
#                     value=prev_answer,
#                     height=300,
#                     key=f"q_{current_q['id']}_answer",
#                     placeholder="Write your answer here..."
#                 )
                
#                 if answer:
#                     st.session_state.user_answers[current_q['id']] = answer
#                     word_count = len(answer.split())
                    
#                     if word_count > current_q.get('word_limit', 250):
#                         st.warning(f"⚠️ Word Count: {word_count} (Exceeds limit!)")
#                     else:
#                         st.info(f"📊 Word Count: {word_count}/{current_q.get('word_limit', 250)}")
            
#             # Navigation buttons
#             st.markdown("<br><br>", unsafe_allow_html=True)
#             col_prev, col_spacer, col_next = st.columns([1, 2, 1])
            
#             with col_prev:
#                 if st.session_state.current_question > 1:
#                     if st.button("← Previous", use_container_width=True):
#                         st.session_state.current_question -= 1
#                         st.rerun()
            
#             with col_next:
#                 if st.session_state.current_question < len(st.session_state.questions):
#                     if st.button("Next →", use_container_width=True, type="primary"):
#                         st.session_state.current_question += 1
#                         st.rerun()
#                 else:
#                     if st.button("Submit Test ✓", use_container_width=True, type="primary"):
#                         st.session_state.test_stage = "results"
#                         st.rerun()
        
#         # Auto-refresh for timer
#         if remaining_seconds > 0:
#             time.sleep(1)
#             st.rerun()

#     # ==================== RESULTS STAGE ====================
#     elif st.session_state.test_stage == "results":
#         st.markdown("## 🎓 Test Results & Analysis")
        
#         # Calculate score
#         if st.session_state.exam_type == "Prelims":
#             total_marks = sum(q['marks'] for q in st.session_state.questions)
#             scored_marks = 0
#             correct_count = 0
#             wrong_count = 0
#             unanswered_count = 0
            
#             for q in st.session_state.questions:
#                 user_ans = st.session_state.user_answers.get(q['id'])
#                 if user_ans is None:
#                     unanswered_count += 1
#                 elif user_ans == q['correct_answer']:
#                     scored_marks += q['marks']
#                     correct_count += 1
#                 else:
#                     wrong_count += 1
            
#             # Score card
#             col1, col2, col3, col4 = st.columns(4)
            
#             with col1:
#                 st.metric("Total Score", f"{scored_marks}/{total_marks}")
#             with col2:
#                 st.metric("✅ Correct", correct_count)
#             with col3:
#                 st.metric("❌ Wrong", wrong_count)
#             with col4:
#                 st.metric("⭕ Unanswered", unanswered_count)
            
#             percentage = (scored_marks / total_marks * 100) if total_marks > 0 else 0
#             st.progress(percentage / 100)
#             st.markdown(f"### Percentage: {percentage:.2f}%")
            
#             if percentage >= 80:
#                 st.success("🌟 Excellent Performance!")
#             elif percentage >= 60:
#                 st.info("👍 Good Performance!")
#             elif percentage >= 40:
#                 st.warning("📚 Average Performance")
#             else:
#                 st.error("💪 Needs Improvement")
        
#         else:  # Mains
#             total_marks = sum(q['marks'] for q in st.session_state.questions)
#             answered_count = len(st.session_state.user_answers)
#             unanswered_count = len(st.session_state.questions) - answered_count
            
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("Total Marks", total_marks)
#             with col2:
#                 st.metric("Answered", answered_count)
#             with col3:
#                 st.metric("Unanswered", unanswered_count)
            
#             st.info("📝 Mains answers require manual evaluation. Review the answer key below.")
        
#         st.divider()
        
#         # Detailed Analysis
#         st.markdown("## 📊 Detailed Analysis")
        
#         for q in st.session_state.questions:
#             user_ans = st.session_state.user_answers.get(q['id'])
            
#             if q['type'] == 'MCQ':
#                 is_correct = user_ans == q.get('correct_answer')
#                 status = "✅ Correct" if is_correct else ("❌ Wrong" if user_ans else "⭕ Unanswered")
                
#                 with st.expander(f"Question {q['id']}: {status}", expanded=False):
#                     st.markdown(f"**Question ({q['marks']} marks):**")
#                     st.markdown(q['question'])
#                     st.markdown("**Options:**")
#                     for key, value in q['options'].items():
#                         st.markdown(f"{key}. {value}")
                    
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         if user_ans == q['correct_answer']:
#                             st.success(f"**Your Answer:** {user_ans} ✅")
#                         elif user_ans:
#                             st.error(f"**Your Answer:** {user_ans} ❌")
#                         else:
#                             st.warning("**Your Answer:** Not Answered")
                    
#                     with col2:
#                         st.info(f"**Correct Answer:** {q['correct_answer']}")
                    
#                     st.markdown("**Explanation:**")
#                     st.markdown(q['explanation'])
            
#             else:  # Descriptive
#                 with st.expander(f"Question {q['id']}: {'✅ Answered' if user_ans else '⭕ Unanswered'}", expanded=False):
#                     st.markdown(f"**Question ({q['marks']} marks):**")
#                     st.markdown(q['question'])
                    
#                     if user_ans:
#                         st.markdown("**Your Answer:**")
#                         st.text_area("", value=user_ans, height=150, disabled=True, key=f"result_{q['id']}")
#                         st.caption(f"Word Count: {len(user_ans.split())}/{q.get('word_limit', 250)}")
#                     else:
#                         st.warning("**Your Answer:** Not Answered")
                    
#                     st.markdown("**Key Points to Cover:**")
#                     if 'key_points' in q:
#                         for point in q['key_points']:
#                             st.markdown(f"- {point}")
                    
#                     st.markdown("**Explanation:**")
#                     st.markdown(q.get('explanation', 'Focus on structure and depth.'))
        
#         st.divider()
        
#         # Action buttons
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             if st.button("🔄 Take New Test", use_container_width=True, type="primary"):
#                 st.session_state.test_stage = "setup"
#                 st.session_state.questions = []
#                 st.session_state.user_answers = {}
#                 st.session_state.current_question = 1
#                 st.rerun()
        
#         with col2:
#             if st.button("📥 Download Report", use_container_width=True):
#                 st.info("Report download coming soon!")
        
#         with col3:
#             if st.button("📊 View Analytics", use_container_width=True):
#                 st.info("Analytics coming soon!")

import streamlit as st
from streamlit_option_menu import option_menu
import time
from datetime import datetime, timedelta
from final_backend import generate_questions
import json
import uuid
def show():
    # Page config
    st.set_page_config(page_title="Dalvoy - Mock Test", layout="wide")

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .question-nav-btn {
        width: 50px;
        height: 50px;
        border-radius: 8px;
        margin: 5px;
        font-weight: bold;
        font-size: 16px;
    }
    .timer-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .instruction-card {
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px auto;
        max-width: 800px;
    }
    .instruction-item {
        padding: 12px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .question-card {
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .option-box {
        padding: 15px;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        margin: 10px 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .option-box:hover {
        border-color: #4CAF50;
        background: #f0f9f0;
    }
    .sidebar-timer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .question-nav-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "exam_type" not in st.session_state:
        st.session_state.exam_type = "Prelims"
    if "language" not in st.session_state:
        st.session_state.language = "English"
    if "paper_type" not in st.session_state:
        st.session_state.paper_type = "General Studies (Paper I) - History, Geography, Polity, Economics, etc."
    if "num_questions" not in st.session_state:
        st.session_state.num_questions = 5
    if "question_source" not in st.session_state:
        st.session_state.question_source = "Mock Questions"
    if "ca_integration" not in st.session_state:
        st.session_state.ca_integration = "Off"
    if "preferences" not in st.session_state:
        st.session_state.preferences = ""
    if "test_stage" not in st.session_state:
        st.session_state.test_stage = "setup"  # setup, loading, instructions, test, results
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}
    if "test_start_time" not in st.session_state:
        st.session_state.test_start_time = None
    if "test_duration" not in st.session_state:
        st.session_state.test_duration = 0
    if "time_expired" not in st.session_state:
        st.session_state.time_expired = False
    if "current_question" not in st.session_state:
        st.session_state.current_question = 1
    if "generation_progress" not in st.session_state:
        st.session_state.generation_progress = 0
    if 'evaluation_result' not in st.session_state:
        st.session_state.evaluation_result = None

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

    # ==================== SETUP STAGE ====================
    if st.session_state.test_stage == "setup":
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
                    st.session_state.paper_type = "GS1 - Indian Heritage and Culture, History and Geography"
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
            num_questions = st.slider("", min_value=1, max_value=50, value=st.session_state.num_questions, step=1, key="num_q")
            st.session_state.num_questions = num_questions
            
            # Calculate test duration
            if st.session_state.exam_type == "Prelims":
                duration_minutes = num_questions * 2
            else:
                duration_minutes = num_questions * 15
            
            st.caption(f"Test Duration: {duration_minutes} minutes | {num_questions} questions")
            
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
                placeholder="e.g., 'focus on economic policies post-2020', 'environmental governance in urban areas'",
                height=80,
                label_visibility="collapsed",
                key="prefs_area"
            )
            st.session_state.preferences = preferences
            
            # Generate Test Button
            st.divider()
            if st.button("🎯 Generate Test", use_container_width=True, type="primary"):
                st.session_state.test_stage = "loading"
                st.session_state.generation_progress = 0
                st.rerun()

        # Right Sidebar - Test Summary
        with col2:
            st.markdown("### 📋 Test Summary")
            
            if st.session_state.exam_type == "Prelims":
                paper_display = "GS1"
            else:
                full_paper = st.session_state.paper_type
                if full_paper:
                    paper_display = full_paper.split(" - ")[0].split(" Case")[0]
                else:
                    paper_display = "N/A"
            
            summary_data = {
                "Language": st.session_state.language,
                "Exam Type": st.session_state.exam_type,
                "Paper Type": paper_display,
                "Questions": f"{st.session_state.num_questions}",
                "Source": st.session_state.question_source,
                "Current Affairs": st.session_state.ca_integration
            }
            
            for key, value in summary_data.items():
                st.markdown(f"**{key}:**")
                st.markdown(f"<div style='margin-left: 10px;'>{value}</div>", unsafe_allow_html=True)
                st.divider()
            
            st.info("💡 Click \"Generate Test\" to create your personalized mock test")

    # ==================== LOADING STAGE ====================
    elif st.session_state.test_stage == "loading":
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        # Center content
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Spinning loader animation
            st.markdown("""
            <div style="text-align: center;">
                <div style="margin: 40px auto;">
                    <div style="border: 8px solid #f3f3f3; border-top: 8px solid #3498db; 
                                border-radius: 50%; width: 80px; height: 80px; 
                                animation: spin 1s linear infinite; margin: 0 auto;">
                    </div>
                </div>
                <style>
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
                </style>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("# Live Test Generation in Progress")
            st.markdown(f"### Generating {st.session_state.num_questions} questions via Question Engine...")
            
            # Progress bar
            progress_placeholder = st.empty()
            
            # Simulate progress and generate questions
            for i in range(10):
                st.session_state.generation_progress = (i + 1) * 10
                progress_placeholder.progress(st.session_state.generation_progress / 100, 
                                             text=f"{st.session_state.generation_progress}% Complete")
                time.sleep(0.3)
            
            # Actually generate questions
            questions = generate_questions(
                exam_type=st.session_state.exam_type,
                paper_type=st.session_state.paper_type,
                num_questions=st.session_state.num_questions,
                question_source=st.session_state.question_source,
                ca_integration=st.session_state.ca_integration,
                preferences=st.session_state.preferences,
                language=st.session_state.language
            )
            
            if questions:
                st.session_state.questions = questions
                st.session_state.user_answers = {}
                st.session_state.time_expired = False
                st.session_state.current_question = 1
                
                # Calculate duration
                if st.session_state.exam_type == "Prelims":
                    st.session_state.test_duration = st.session_state.num_questions * 2
                else:
                    st.session_state.test_duration = st.session_state.num_questions * 15
                
                progress_placeholder.progress(1.0, text="100% Complete")
                time.sleep(0.5)
                st.session_state.test_stage = "instructions"
                st.rerun()
            else:
                st.error("Failed to generate questions. Please try again.")
                time.sleep(2)
                st.session_state.test_stage = "setup"
                st.rerun()

    # ==================== INSTRUCTIONS STAGE ====================
    # elif st.session_state.test_stage == "instructions":
    #     st.markdown("<br><br>", unsafe_allow_html=True)
        
    #     # Center the instruction card
    #     col1, col2, col3 = st.columns([1, 3, 1])
        
    #     with col2:
    #         st.markdown(f"""
    #         <div class="instruction-card">
    #             <h2>🎯 {st.session_state.exam_type} Test Instructions</h2>
    #             <br>
    #             <div class="instruction-item">
    #                 <strong>1.</strong> Each question carries equal marks with no negative marking in this practice test
    #             </div>
    #             <div class="instruction-item">
    #                 <strong>2.</strong> Select the most appropriate answer for each question
    #             </div>
    #             <div class="instruction-item">
    #                 <strong>3.</strong> Review your answers before final submission
    #             </div>
    #             <div class="instruction-item">
    #                 <strong>4.</strong> Use proper time management throughout the test
    #             </div>
    #             <div class="instruction-item">
    #                 <strong>5.</strong> Test will auto submit if the timer ends
    #             </div>
    #         </div>
    #         """, unsafe_allow_html=True)
            
    #         st.markdown("<br>", unsafe_allow_html=True)
            
    #         # Center the button
    #         col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    #         with col_btn2:
    #             if st.button("⚡ Attempt Test", use_container_width=True, type="primary"):
    #                 st.session_state.test_start_time = datetime.now()
    #                 st.session_state.test_stage = "test"
    #                 st.rerun()

# ==================== INSTRUCTIONS STAGE ====================
    elif st.session_state.test_stage == "instructions":
        # Center the instruction card
       # col1, col2, col3 = st.columns([1, 2, 1])
        
        
        # Different instructions for Prelims vs Mains
        if st.session_state.exam_type == "Prelims":
                #     st.markdown("<br><br>", unsafe_allow_html=True)
    
            # Center the instruction card
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col2:
                st.markdown(f"""
                <div class="instruction-card">
                    <h2>🎯 {st.session_state.exam_type} Test Instructions</h2>
                    <br>
                    <div class="instruction-item">
                        <strong>1.</strong> Each question carries equal marks with no negative marking in this practice test
                    </div>
                    <div class="instruction-item">
                        <strong>2.</strong> Select the most appropriate answer for each question
                    </div>
                    <div class="instruction-item">
                        <strong>3.</strong> Review your answers before final submission
                    </div>
                    <div class="instruction-item">
                        <strong>4.</strong> Use proper time management throughout the test
                    </div>
                    <div class="instruction-item">
                        <strong>5.</strong> Test will auto submit if the timer ends
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Center the button
                col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
                with col_btn2:
                    if st.button("⚡ Attempt Test", use_container_width=True, type="primary"):
                        st.session_state.test_start_time = datetime.now()
                        st.session_state.test_stage = "test"
                        st.rerun()
        else:  # Mains
            #     instructions_html = """
            #     <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 25px;">
            #         <div style="display: flex; align-items: center; padding: 12px 0; border-bottom: 1px solid #e0e0e0;">
            #             <span style="background: #4CAF50; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">1</span>
            #             <span style="color: #555;">Write your answers on plain sheets of paper in clear, legible handwriting</span>
            #         </div>
            #         <div style="display: flex; align-items: center; padding: 12px 0; border-bottom: 1px solid #e0e0e0;">
            #             <span style="background: #2196F3; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">2</span>
            #             <span style="color: #555;">Structure your answers with proper introduction, body, and conclusion</span>
            #         </div>
            #         <div style="display: flex; align-items: center; padding: 12px 0; border-bottom: 1px solid #e0e0e0;">
            #             <span style="background: #FF9800; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">3</span>
            #             <span style="color: #555;">Support your arguments with relevant examples and case studies</span>
            #         </div>
            #         <div style="display: flex; align-items: center; padding: 12px 0; border-bottom: 1px solid #e0e0e0;">
            #             <span style="background: #9C27B0; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">4</span>
            #             <span style="color: #555;">Adhere to the word limit specified for each question</span>
            #         </div>
            #         <div style="display: flex; align-items: center; padding: 12px 0; border-bottom: 1px solid #e0e0e0;">
            #             <span style="background: #FF5722; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">5</span>
            #             <span style="color: #555;">Use diagrams, flowcharts, and bullet points where appropriate</span>
            #         </div>
            #         <div style="display: flex; align-items: center; padding: 12px 0;">
            #             <span style="background: #00BCD4; color: white; width: 30px; height: 30px; 
            #                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            #                        margin-right: 15px; font-weight: bold;">6</span>
            #             <span style="color: #555;">After completing the test, use our Mains Answer Evaluator for detailed feedback</span>
            #         </div>
            #     </div>
            #     """
            
            # st.markdown(f"""
            # <div style="background: white; padding: 40px; border-radius: 16px; 
            #             box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-top: 40px;">
            #     <div style="text-align: center; margin-bottom: 30px;">
            #         <div style="font-size: 48px; margin-bottom: 10px;">📝</div>
            #         <h2 style="margin: 0; color: #333;">{st.session_state.exam_type} Test Instructions</h2>
            #     </div>
            #     {instructions_html}
            # </div>
            # """, unsafe_allow_html=True)
            
            # st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col2:
                st.markdown(f"""
                <div class="instruction-card">
                    <h2>🎯 {st.session_state.exam_type} Test Instructions</h2>
                    <br>
                    <div class="instruction-item">
                        <strong>1.</strong> Write your answers on plain sheets of paper in clear, legible handwriting
                    </div>
                    <div class="instruction-item">
                        <strong>2.</strong> Structure your answers with proper introduction, body, and conclusion
                    </div>
                    <div class="instruction-item">
                        <strong>3.</strong> Support your arguments with relevant examples and case studies
                    </div>
                    <div class="instruction-item">
                        <strong>4.</strong> Adhere to the word limit specified for each question
                    </div>
                    <div class="instruction-item">
                        <strong>5.</strong> Use diagrams, flowcharts, and bullet points where appropriate
                    </div>
                     <div class="instruction-item">
                        <strong>5.</strong> After completing the test, use our Mains Answer Evaluator for detailed feedback
                    </div>

                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Center the button
                col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
                with col_btn2:
                    if st.button("⚡ Attempt Test", use_container_width=True, type="primary"):
                        st.session_state.test_start_time = datetime.now()
                        st.session_state.test_stage = "test"
                        st.rerun()


    # ==================== TEST STAGE ====================
    elif st.session_state.test_stage == "test":
        # Calculate remaining time
        elapsed = datetime.now() - st.session_state.test_start_time
        total_seconds = st.session_state.test_duration * 60
        remaining_seconds = max(0, total_seconds - int(elapsed.total_seconds()))
        
        mins, secs = divmod(remaining_seconds, 60)
        
        # Check if time expired
        if remaining_seconds == 0 and not st.session_state.time_expired:
            st.session_state.time_expired = True
            # Route based on exam type
            if st.session_state.exam_type == "Mains":
                st.session_state.test_stage = "mains_upload"
            else:
                st.session_state.test_stage = "results"
            st.rerun()
        
        # Sidebar with timer and navigation
        with st.sidebar:
            st.markdown("### ⏱️ Questions")
            
            # Timer - Display prominently
            timer_color = "red" if remaining_seconds <= 300 else "white"
            st.markdown(f"""
            <div class="sidebar-timer">
                <div style="font-size: 14px; margin-bottom: 5px;">⏳ Time Remaining</div>
                <div style="font-size: 32px; font-weight: bold; color: {timer_color};">{mins:02d}:{secs:02d}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### QUESTIONS")
            
            # Question navigation buttons
            cols = st.columns(5)
            for idx, q in enumerate(st.session_state.questions):
                col_idx = idx % 5
                with cols[col_idx]:
                    is_answered = q['id'] in st.session_state.user_answers
                    is_current = st.session_state.current_question == q['id']
                    
                    button_type = "primary" if is_current else "secondary"
                    
                    if st.button(
                        str(q['id']),
                        key=f"nav_q_{q['id']}",
                        use_container_width=True,
                        type=button_type
                    ):
                        st.session_state.current_question = q['id']
                        st.rerun()
                    
                    # Show indicator
                    if is_answered and not is_current:
                        st.markdown("<div style='text-align:center; color:green; font-size:18px;'>✓</div>", unsafe_allow_html=True)
            
            st.divider()
            
            # Submit button in sidebar
            if st.button("✅ Submit Test", use_container_width=True, type="primary", key="sidebar_submit"):
                # Route based on exam type
                if st.session_state.exam_type == "Mains":
                    st.session_state.test_stage = "mains_upload"
                else:
                    st.session_state.test_stage = "results"
                st.rerun()
        
        # Main content area
        current_q = next((q for q in st.session_state.questions if q['id'] == st.session_state.current_question), None)
        
        if current_q:
            # Question header with type indicator
            question_label = "Mains Question" if st.session_state.exam_type == "Mains" else "Question"
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 15px 25px; border-radius: 10px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2 style="margin: 0;">Question {current_q['id']}</h2>
                    <span style="background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 20px; font-size: 14px;">
                        {question_label}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Question card
            st.markdown(f"""
            <div class="question-card">
                <p style="font-size: 18px; line-height: 1.6; color: #333;">
                    {current_q['question']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display differently for Prelims vs Mains
            if st.session_state.exam_type == "Prelims":
                st.markdown("### Select your answer:")
            else:
                st.markdown(f"<div style='background: #e3f2fd; padding: 10px; border-radius: 5px; margin: 15px 0;'>"
                          f"<strong>📝 Word Limit:</strong> {current_q.get('word_limit', 150)} words | "
                          f"<strong>📊 Marks:</strong> {current_q.get('marks', 10)}</div>", 
                          unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if current_q['type'] == 'MCQ':
                # Get previous answer
                prev_answer = st.session_state.user_answers.get(current_q['id'])
                
                # Create a list of options for radio button
                option_keys = list(current_q['options'].keys())
                option_labels = [f"{k}) {v}" for k, v in current_q['options'].items()]
                
                # Find default index
                default_index = option_keys.index(prev_answer) if prev_answer in option_keys else None
                
                # Radio button selection
                selected = st.radio(
                    "Choose one:",
                    option_labels,
                    index=default_index,
                    key=f"mcq_{current_q['id']}",
                    label_visibility="collapsed"
                )
                
                # Save the selected answer
                if selected:
                    selected_key = selected.split(')')[0]
                    st.session_state.user_answers[current_q['id']] = selected_key
            
            else:  # Descriptive (Mains)
                # Writing Instructions box
                st.markdown("""
                <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <div style="background: #2196F3; color: white; width: 35px; height: 35px; 
                                  border-radius: 8px; display: flex; align-items: center; justify-content: center; 
                                  margin-right: 12px; font-size: 18px;">✍️</div>
                        <h4 style="margin: 0; color: #1976D2;">Writing Instructions</h4>
                    </div>
                    <p style="margin: 0; color: #555; font-size: 14px;">
                        Please write your answers on plain sheets of paper.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                prev_answer = st.session_state.user_answers.get(current_q['id'], "")
                
                st.info("ℹ️ In the actual test, you will write your answer on paper. " +
                       "This text area is for your reference and notes only.")
                
                answer = st.text_area(
                    "Your Answer (Optional - For Reference):",
                    value=prev_answer,
                    height=300,
                    key=f"q_{current_q['id']}_answer",
                    placeholder="You can optionally type your answer here for reference, but remember to write it on paper as per exam instructions..."
                )
                
                if answer:
                    st.session_state.user_answers[current_q['id']] = answer
                    word_count = len(answer.split())
                    
                    if word_count > current_q.get('word_limit', 250):
                        st.warning(f"⚠️ Word Count: {word_count} (Exceeds limit!)")
                    else:
                        st.info(f"📊 Word Count: {word_count}/{current_q.get('word_limit', 250)}")
            
            # Navigation buttons
            st.markdown("<br><br>", unsafe_allow_html=True)
            col_prev, col_spacer, col_next = st.columns([1, 2, 1])
            
            with col_prev:
                if st.session_state.current_question > 1:
                    if st.button("← Previous", use_container_width=True, key="prev_btn"):
                        st.session_state.current_question -= 1
                        st.rerun()
            
            with col_next:
                if st.session_state.current_question < len(st.session_state.questions):
                    if st.button("Next →", use_container_width=True, type="primary", key="next_btn"):
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    button_text = "Submit Test ✓"
                    if st.button(button_text, use_container_width=True, type="primary", key="final_submit"):
                        # Route based on exam type
                        if st.session_state.exam_type == "Mains":
                            st.session_state.test_stage = "mains_upload"
                        else:
                            st.session_state.test_stage = "results"
                        st.rerun()
        
        # Auto-refresh for timer - use a placeholder to trigger refresh
        time_placeholder = st.empty()
        with time_placeholder.container():
            st.markdown(f"<!-- Timer refresh: {remaining_seconds} -->", unsafe_allow_html=True)
        
        if remaining_seconds > 0:
            time.sleep(1)
            st.rerun()

    # ==================== MAINS UPLOAD STAGE ====================
    elif st.session_state.test_stage == "mains_upload":
        st.markdown("## 📝 Mains Answer Evaluation")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            <div style="background: #e3f2fd; padding: 30px; border-radius: 12px; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 64px; margin-bottom: 15px;">✍️</div>
                <h3 style="color: #1976D2; margin-bottom: 15px;">Ready to Get Your Answer Evaluated?</h3>
                <p style="color: #555; font-size: 16px; line-height: 1.6;">
                    Please upload your answer sheets to our dedicated Mains Answer Evaluator<br>
                    for detailed feedback and scoring.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # File uploader
            uploaded_file = st.file_uploader(
                "Upload Answer Sheet (PDF)",
                type=['pdf'],
                help="Upload a PDF file containing your handwritten or typed answers",
                key="mains_pdf_uploader"
            )
            
            if uploaded_file is not None:
                st.session_state.uploaded_pdf = uploaded_file
                st.success(f"✅ File uploaded: {uploaded_file.name}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Show evaluation button
                if st.button("🔍 Evaluate My Answers", use_container_width=True, type="primary"):
                    with st.spinner("Evaluating your answers... This may take a minute."):
                        try:
                            # Import the evaluation function
                            from final_backend import IngestPDF, chatbot
                            from langchain_core.messages import HumanMessage
                            
                            # Create a thread ID for this evaluation
                            thread_id = str(uuid.uuid4())
                            
                            # Ingest the PDF
                            pdf_bytes = uploaded_file.getvalue()
                            metadata = IngestPDF(pdf_bytes, thread_id, uploaded_file.name)
                            
                            # Prepare evaluation prompt with all questions
                            questions_text = "\n\n".join([
                                f"Question {q['id']} ({q['marks']} marks):\n{q['question']}\n"
                                f"Word Limit: {q.get('word_limit', 150)} words"
                                for q in st.session_state.questions
                            ])
                            
                            evaluation_prompt = f"""You are evaluating UPSC Mains answers uploaded as a PDF document. 

Here are the questions that were asked in this test:

{questions_text}

The student has uploaded their answer sheet. Please perform a comprehensive evaluation:

**Step 1: Extract Answers**
Use the rag_tool to extract and read the answers from the uploaded PDF. The thread_id is: {thread_id}

**Step 2: Evaluate Each Answer**
For each question, evaluate based on:
- Content relevance and accuracy (40%)
- Structure and presentation (20%)
- Use of examples and case studies (20%)
- Language and coherence (10%)
- Adherence to word limit (10%)

**Step 3: Provide Detailed Feedback**
For each question provide:
- Score out of total marks (e.g., "Score: 8/10")
- Strengths: What was done well
- Weaknesses: What needs improvement
- Suggestions: Specific recommendations for better answers

**Step 4: Overall Summary**
- Total score across all questions
- Overall performance assessment
- Key strengths and areas for improvement
- Actionable recommendations for future tests

Please structure your response clearly with headings for each question and a final summary section."""
                            
                            # Get evaluation from chatbot
                            config = {"configurable": {"thread_id": thread_id}}
                            response = chatbot.invoke(
                                {"messages": [HumanMessage(content=evaluation_prompt)]},
                                config=config
                            )
                            
                            # Extract the evaluation result
                            evaluation_text = response["messages"][-1].content
                            st.session_state.evaluation_result = evaluation_text
                            
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"Error during evaluation: {str(e)}")
                            st.info("Please try uploading the file again or contact support.")
                            import traceback
                            st.code(traceback.format_exc())
            
            # Show evaluation results if available
            if st.session_state.evaluation_result:
                st.markdown("<br><br>", unsafe_allow_html=True)
                st.markdown("### 📊 Evaluation Results")
                st.markdown("""
                <div style="background: white; padding: 25px; border-radius: 10px; 
                            box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                """, unsafe_allow_html=True)
                
                st.markdown(st.session_state.evaluation_result)
                
                st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            # Navigation buttons
            col_prev, col_next = st.columns(2)
            
            with col_prev:
                if st.button("← Back to Test", use_container_width=True):
                    st.session_state.test_stage = "test"
                    st.rerun()
            
            with col_next:
                if st.button("View Results →", use_container_width=True, type="primary"):
                    st.session_state.test_stage = "results"
                    st.rerun()

    # ==================== RESULTS STAGE ====================
    elif st.session_state.test_stage == "results":
        st.markdown("## 🎓 Test Results & Analysis")
        
        # Calculate score
        if st.session_state.exam_type == "Prelims":
            total_marks = sum(q['marks'] for q in st.session_state.questions)
            scored_marks = 0
            correct_count = 0
            wrong_count = 0
            unanswered_count = 0
            
            for q in st.session_state.questions:
                user_ans = st.session_state.user_answers.get(q['id'])
                if user_ans is None:
                    unanswered_count += 1
                elif user_ans == q['correct_answer']:
                    scored_marks += q['marks']
                    correct_count += 1
                else:
                    wrong_count += 1
            
            # Score card
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Score", f"{scored_marks}/{total_marks}")
            with col2:
                st.metric("✅ Correct", correct_count)
            with col3:
                st.metric("❌ Wrong", wrong_count)
            with col4:
                st.metric("⭕ Unanswered", unanswered_count)
            
            percentage = (scored_marks / total_marks * 100) if total_marks > 0 else 0
            st.progress(percentage / 100)
            st.markdown(f"### Percentage: {percentage:.2f}%")
            
            if percentage >= 80:
                st.success("🌟 Excellent Performance!")
            elif percentage >= 60:
                st.info("👍 Good Performance!")
            elif percentage >= 40:
                st.warning("📚 Average Performance")
            else:
                st.error("💪 Needs Improvement")
        
        else:  # Mains
            total_marks = sum(q['marks'] for q in st.session_state.questions)
            answered_count = len(st.session_state.user_answers)
            unanswered_count = len(st.session_state.questions) - answered_count
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Marks", total_marks)
            with col2:
                st.metric("Questions", len(st.session_state.questions))
            with col3:
                st.metric("Duration", f"{st.session_state.test_duration} mins")
            
            # Show evaluation status
            if st.session_state.evaluation_result:
                st.success("✅ Your answers have been evaluated! Scroll down to see detailed AI feedback.")
            else:
                st.info("📝 Upload your answer sheet to get detailed AI evaluation and feedback.")
        
        st.divider()
        
        # Detailed Analysis
        st.markdown("## 📊 Detailed Analysis")
        
        for q in st.session_state.questions:
            user_ans = st.session_state.user_answers.get(q['id'])
            
            if q['type'] == 'MCQ':
                is_correct = user_ans == q.get('correct_answer')
                status = "✅ Correct" if is_correct else ("❌ Wrong" if user_ans else "⭕ Unanswered")
                
                with st.expander(f"Question {q['id']}: {status}", expanded=False):
                    st.markdown(f"**Question ({q['marks']} marks):**")
                    st.markdown(q['question'])
                    st.markdown("**Options:**")
                    for key, value in q['options'].items():
                        st.markdown(f"{key}. {value}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if user_ans == q['correct_answer']:
                            st.success(f"**Your Answer:** {user_ans} ✅")
                        elif user_ans:
                            st.error(f"**Your Answer:** {user_ans} ❌")
                        else:
                            st.warning("**Your Answer:** Not Answered")
                    
                    with col2:
                        st.info(f"**Correct Answer:** {q['correct_answer']}")
                    
                    st.markdown("**Explanation:**")
                    st.markdown(q['explanation'])
            
            else:  # Descriptive
                with st.expander(f"Question {q['id']}: {q.get('marks', 10)} marks", expanded=False):
                    st.markdown(f"**Question ({q['marks']} marks):**")
                    st.markdown(q['question'])
                    st.caption(f"📝 Word Limit: {q.get('word_limit', 150)} words")
                    
                    if user_ans:
                        st.markdown("**Your Reference Answer:**")
                        st.text_area("", value=user_ans, height=150, disabled=True, key=f"result_{q['id']}")
                        st.caption(f"Word Count: {len(user_ans.split())}/{q.get('word_limit', 250)}")
                    
                    st.markdown("**Key Points to Cover:**")
                    if 'key_points' in q:
                        for point in q['key_points']:
                            st.markdown(f"- {point}")
                    
                    st.markdown("**Approach:**")
                    st.markdown(q.get('explanation', 'Focus on structure, depth, and use relevant examples.'))
        
        # Show AI evaluation for Mains if available
        if st.session_state.exam_type == "Mains" and st.session_state.evaluation_result:
            st.divider()
            st.markdown("## 🤖 AI Evaluation Report")
            st.markdown("""
            <div style="background: #f0f7ff; padding: 25px; border-radius: 10px; 
                        border-left: 5px solid #2196F3;">
            """, unsafe_allow_html=True)
            
            st.markdown(st.session_state.evaluation_result)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.divider()
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Take New Test", use_container_width=True, type="primary"):
                # Reset all relevant session state
                st.session_state.test_stage = "setup"
                st.session_state.questions = []
                st.session_state.user_answers = {}
                st.session_state.current_question = 1
                st.session_state.uploaded_pdf = None
                st.session_state.evaluation_result = None
                st.rerun()
        
        with col2:
            if st.button("📥 Download Report", use_container_width=True):
                st.info("Report download coming soon!")
        
        with col3:
            if st.button("📊 View Analytics", use_container_width=True):
                st.info("Analytics coming soon!")
        
        # Additional button for Mains to go back to upload
        if st.session_state.exam_type == "Mains":
            st.markdown("<br>", unsafe_allow_html=True)
            col_center = st.columns([1, 2, 1])[1]
            with col_center:
                if not st.session_state.evaluation_result:
                    if st.button("📤 Upload Answers for Evaluation", 
                               use_container_width=True, type="secondary"):
                        st.session_state.test_stage = "mains_upload"
                        st.rerun()
                else:
                    if st.button("🔄 Re-evaluate with Different Answers", 
                               use_container_width=True, type="secondary"):
                        st.session_state.uploaded_pdf = None
                        st.session_state.evaluation_result = None
                        st.session_state.test_stage = "mains_upload"
                        st.rerun()



    # ==================== TEST STAGE ====================
    # elif st.session_state.test_stage == "test":
    #     # Calculate remaining time
    #     elapsed = datetime.now() - st.session_state.test_start_time
    #     total_seconds = st.session_state.test_duration * 60
    #     remaining_seconds = max(0, total_seconds - int(elapsed.total_seconds()))
        
    #     mins, secs = divmod(remaining_seconds, 60)
        
    #     # Check if time expired
    #     if remaining_seconds == 0 and not st.session_state.time_expired:
    #         st.session_state.time_expired = True
    #         st.session_state.test_stage = "results"
    #         st.rerun()
        
    #     # Sidebar with timer and navigation
    #     with st.sidebar:
    #         st.markdown("### ⏱️ Questions")
            
    #         # Timer - Display prominently
    #         timer_color = "red" if remaining_seconds <= 300 else "white"
    #         st.markdown(f"""
    #         <div class="sidebar-timer">
    #             <div style="font-size: 14px; margin-bottom: 5px;">⏳ Time Remaining</div>
    #             <div style="font-size: 32px; font-weight: bold; color: {timer_color};">{mins:02d}:{secs:02d}</div>
    #         </div>
    #         """, unsafe_allow_html=True)
            
    #         st.markdown("#### QUESTIONS")
            
    #         # Question navigation buttons
    #         cols = st.columns(5)
    #         for idx, q in enumerate(st.session_state.questions):
    #             col_idx = idx % 5
    #             with cols[col_idx]:
    #                 is_answered = q['id'] in st.session_state.user_answers
    #                 is_current = st.session_state.current_question == q['id']
                    
    #                 button_type = "primary" if is_current else "secondary"
                    
    #                 if st.button(
    #                     str(q['id']),
    #                     key=f"nav_q_{q['id']}",
    #                     use_container_width=True,
    #                     type=button_type
    #                 ):
    #                     st.session_state.current_question = q['id']
    #                     st.rerun()
                    
    #                 # Show indicator
    #                 if is_answered and not is_current:
    #                     st.markdown("<div style='text-align:center; color:green; font-size:18px;'>✓</div>", unsafe_allow_html=True)
            
    #         st.divider()
            
    #         # Submit button in sidebar
    #         if st.button("✅ Submit Test", use_container_width=True, type="primary", key="sidebar_submit"):
    #             st.session_state.test_stage = "results"
    #             st.rerun()
        
    #     # Main content area
    #     current_q = next((q for q in st.session_state.questions if q['id'] == st.session_state.current_question), None)
        
    #     if current_q:
    #         # Question header
    #         st.markdown(f"""
    #         <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    #                     color: white; padding: 15px 25px; border-radius: 10px; margin-bottom: 20px;">
    #             <h2 style="margin: 0;">Question {current_q['id']}</h2>
    #         </div>
    #         """, unsafe_allow_html=True)
            
    #         # Question card
    #         st.markdown(f"""
    #         <div class="question-card">
    #             <p style="font-size: 18px; line-height: 1.6; color: #333;">
    #                 {current_q['question']}
    #             </p>
    #         </div>
    #         """, unsafe_allow_html=True)
            
    #         st.markdown("### Select your answer:")
    #         st.markdown("<br>", unsafe_allow_html=True)
            
    #         if current_q['type'] == 'MCQ':
    #             # Get previous answer
    #             prev_answer = st.session_state.user_answers.get(current_q['id'])
                
    #             # Create a list of options for radio button
    #             option_keys = list(current_q['options'].keys())
    #             option_labels = [f"{k}) {v}" for k, v in current_q['options'].items()]
                
    #             # Find default index
    #             default_index = option_keys.index(prev_answer) if prev_answer in option_keys else None
                
    #             # Radio button selection
    #             selected = st.radio(
    #                 "Choose one:",
    #                 option_labels,
    #                 index=default_index,
    #                 key=f"mcq_{current_q['id']}",
    #                 label_visibility="collapsed"
    #             )
                
    #             # Save the selected answer
    #             if selected:
    #                 selected_key = selected.split(')')[0]
    #                 st.session_state.user_answers[current_q['id']] = selected_key
            
    #         else:  # Descriptive
    #             st.caption(f"📝 Word Limit: {current_q.get('word_limit', 250)} words")
    #             prev_answer = st.session_state.user_answers.get(current_q['id'], "")
                
    #             answer = st.text_area(
    #                 "Your Answer:",
    #                 value=prev_answer,
    #                 height=300,
    #                 key=f"q_{current_q['id']}_answer",
    #                 placeholder="Write your answer here..."
    #             )
                
    #             if answer:
    #                 st.session_state.user_answers[current_q['id']] = answer
    #                 word_count = len(answer.split())
                    
    #                 if word_count > current_q.get('word_limit', 250):
    #                     st.warning(f"⚠️ Word Count: {word_count} (Exceeds limit!)")
    #                 else:
    #                     st.info(f"📊 Word Count: {word_count}/{current_q.get('word_limit', 250)}")
            
    #         # Navigation buttons
    #         st.markdown("<br><br>", unsafe_allow_html=True)
    #         col_prev, col_spacer, col_next = st.columns([1, 2, 1])
            
    #         with col_prev:
    #             if st.session_state.current_question > 1:
    #                 if st.button("← Previous", use_container_width=True, key="prev_btn"):
    #                     st.session_state.current_question -= 1
    #                     st.rerun()
            
    #         with col_next:
    #             if st.session_state.current_question < len(st.session_state.questions):
    #                 if st.button("Next →", use_container_width=True, type="primary", key="next_btn"):
    #                     st.session_state.current_question += 1
    #                     st.rerun()
    #             else:
    #                 if st.button("Submit Test ✓", use_container_width=True, type="primary", key="final_submit"):
    #                     st.session_state.test_stage = "results"
    #                     st.rerun()
        
    #     # Auto-refresh for timer - use a placeholder to trigger refresh
    #     time_placeholder = st.empty()
    #     with time_placeholder.container():
    #         st.markdown(f"<!-- Timer refresh: {remaining_seconds} -->", unsafe_allow_html=True)
        
    #     if remaining_seconds > 0:
    #         time.sleep(1)
    #         st.rerun()

    # # ==================== RESULTS STAGE ====================
    # elif st.session_state.test_stage == "results":
    #     st.markdown("## 🎓 Test Results & Analysis")
        
    #     # Calculate score
    #     if st.session_state.exam_type == "Prelims":
    #         total_marks = sum(q['marks'] for q in st.session_state.questions)
    #         scored_marks = 0
    #         correct_count = 0
    #         wrong_count = 0
    #         unanswered_count = 0
            
    #         for q in st.session_state.questions:
    #             user_ans = st.session_state.user_answers.get(q['id'])
    #             if user_ans is None:
    #                 unanswered_count += 1
    #             elif user_ans == q['correct_answer']:
    #                 scored_marks += q['marks']
    #                 correct_count += 1
    #             else:
    #                 wrong_count += 1
            
    #         # Score card
    #         col1, col2, col3, col4 = st.columns(4)
            
    #         with col1:
    #             st.metric("Total Score", f"{scored_marks}/{total_marks}")
    #         with col2:
    #             st.metric("✅ Correct", correct_count)
    #         with col3:
    #             st.metric("❌ Wrong", wrong_count)
    #         with col4:
    #             st.metric("⭕ Unanswered", unanswered_count)
            
    #         percentage = (scored_marks / total_marks * 100) if total_marks > 0 else 0
    #         st.progress(percentage / 100)
    #         st.markdown(f"### Percentage: {percentage:.2f}%")
            
    #         if percentage >= 80:
    #             st.success("🌟 Excellent Performance!")
    #         elif percentage >= 60:
    #             st.info("👍 Good Performance!")
    #         elif percentage >= 40:
    #             st.warning("📚 Average Performance")
    #         else:
    #             st.error("💪 Needs Improvement")
        
    #     else:  # Mains
    #         total_marks = sum(q['marks'] for q in st.session_state.questions)
    #         answered_count = len(st.session_state.user_answers)
    #         unanswered_count = len(st.session_state.questions) - answered_count
            
    #         col1, col2, col3 = st.columns(3)
    #         with col1:
    #             st.metric("Total Marks", total_marks)
    #         with col2:
    #             st.metric("Answered", answered_count)
    #         with col3:
    #             st.metric("Unanswered", unanswered_count)
            
    #         st.info("📝 Mains answers require manual evaluation. Review the answer key below.")
        
    #     st.divider()
        
    #     # Detailed Analysis
    #     st.markdown("## 📊 Detailed Analysis")
        
    #     for q in st.session_state.questions:
    #         user_ans = st.session_state.user_answers.get(q['id'])
            
    #         if q['type'] == 'MCQ':
    #             is_correct = user_ans == q.get('correct_answer')
    #             status = "✅ Correct" if is_correct else ("❌ Wrong" if user_ans else "⭕ Unanswered")
                
    #             with st.expander(f"Question {q['id']}: {status}", expanded=False):
    #                 st.markdown(f"**Question ({q['marks']} marks):**")
    #                 st.markdown(q['question'])
    #                 st.markdown("**Options:**")
    #                 for key, value in q['options'].items():
    #                     st.markdown(f"{key}. {value}")
                    
    #                 col1, col2 = st.columns(2)
    #                 with col1:
    #                     if user_ans == q['correct_answer']:
    #                         st.success(f"**Your Answer:** {user_ans} ✅")
    #                     elif user_ans:
    #                         st.error(f"**Your Answer:** {user_ans} ❌")
    #                     else:
    #                         st.warning("**Your Answer:** Not Answered")
                    
    #                 with col2:
    #                     st.info(f"**Correct Answer:** {q['correct_answer']}")
                    
    #                 st.markdown("**Explanation:**")
    #                 st.markdown(q['explanation'])
            
    #         else:  # Descriptive
    #             with st.expander(f"Question {q['id']}: {'✅ Answered' if user_ans else '⭕ Unanswered'}", expanded=False):
    #                 st.markdown(f"**Question ({q['marks']} marks):**")
    #                 st.markdown(q['question'])
                    
    #                 if user_ans:
    #                     st.markdown("**Your Answer:**")
    #                     st.text_area("", value=user_ans, height=150, disabled=True, key=f"result_{q['id']}")
    #                     st.caption(f"Word Count: {len(user_ans.split())}/{q.get('word_limit', 250)}")
    #                 else:
    #                     st.warning("**Your Answer:** Not Answered")
                    
    #                 st.markdown("**Key Points to Cover:**")
    #                 if 'key_points' in q:
    #                     for point in q['key_points']:
    #                         st.markdown(f"- {point}")
                    
    #                 st.markdown("**Explanation:**")
    #                 st.markdown(q.get('explanation', 'Focus on structure and depth.'))
        
    #     st.divider()
        
    #     # Action buttons
    #     col1, col2, col3 = st.columns(3)
        
    #     with col1:
    #         if st.button("🔄 Take New Test", use_container_width=True, type="primary"):
    #             st.session_state.test_stage = "setup"
    #             st.session_state.questions = []
    #             st.session_state.user_answers = {}
    #             st.session_state.current_question = 1
    #             st.rerun()
        
    #     with col2:
    #         if st.button("📥 Download Report", use_container_width=True):
    #             st.info("Report download coming soon!")
        
    #     with col3:
    #         if st.button("📊 View Analytics", use_container_width=True):
    #             st.info("Analytics coming soon!")


