
# import streamlit as st
# from datetime import datetime

# from streamlit_option_menu import option_menu
    
# def show():
    

   

#     # Page config
#     st.set_page_config(page_title="Dalvoy - UPSC GPT", layout="wide")

#     # Initialize session state
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     if "show_feedback_modal" not in st.session_state:
#         st.session_state.show_feedback_modal = False
#     if "rating" not in st.session_state:
#         st.session_state.rating = 0
#     if "feedback_text" not in st.session_state:
#         st.session_state.feedback_text = ""


#     col1, col2, col3, col4 = st.columns([3, 0.5, 0.5, 1])

#     with col1:
#         st.markdown("## UPSC GPT")

#     with col2:
#         if st.button("📄", help="Text Mode", use_container_width=True, key="text_mode_btn"):
#             pass

#     with col3:
#         if st.button("🌐", help="Language", use_container_width=True, key="lang_btn"):
#             pass

#     with col4:
#         if st.button("📝 Give Feedback", use_container_width=True, key="give_feedback_btn"):
#             st.session_state.show_feedback_modal = True

#     st.divider()

#     # Main Chat Area
#     st.markdown("### What can I help with?")

#     # Suggested questions
#     st.markdown("**Choose a mode:**")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("TEXT", use_container_width=True, type="primary", key="text_choice_btn"):
#             pass
#     with col2:
#         if st.button("AUDIO", use_container_width=True, key="audio_choice_btn"):
#             pass

#     st.markdown("**Suggested questions**")

#     suggested_questions = [
#         "Give previous year prelims questions on lakes",
#         "Explain the concept of Federalism",
#         "Give me top foreign policy current affairs",
#         "Create a 30-day study plan for UPSC Prelims"
#     ]

#     for idx, question in enumerate(suggested_questions):
#         if st.button(f"❓ {question}", use_container_width=True, key=f"suggested_q_{idx}"):
#             st.session_state.messages.append({"role": "user", "content": question})
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": f"I'll help you with: {question}\n\n[Response content will appear here]"
#             })

#     # Chat messages display
#     if st.session_state.messages:
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#     # Chat input
#     st.divider()
#     col1, col2 = st.columns([6, 1])

#     with col1:
#         user_input = st.text_input("Ask anything...", placeholder="Ask anything...", label_visibility="collapsed", key="chat_input")

#     with col2:
#         if st.button("➤", use_container_width=True, type="primary", key="send_btn"):
#             if user_input:
#                 st.session_state.messages.append({"role": "user", "content": user_input})
#                 st.session_state.messages.append({
#                     "role": "assistant",
#                     "content": f"Response to: {user_input}\n\n[This is a sample response]"
#                 })

#     # Feedback Modal - Only displayed when show_feedback_modal is True
#     if st.session_state.show_feedback_modal:
#         @st.dialog("Share Your Feedback", width="medium")
#         def show_feedback_form():
#             st.markdown("**Rate this conversation**")
            
#             # Rating Section with stars
#             rating_cols = st.columns(5)
            
#             for i in range(5):
#                 with rating_cols[i]:
#                     star_value = i + 1
#                     if st.button("⭐", key=f"star_{star_value}", use_container_width=True):
#                         st.session_state.rating = star_value
            
#             # Display selected rating
#             if st.session_state.rating > 0:
#                 st.markdown(f"**You rated: {st.session_state.rating} / 5 stars**")
            
#             st.divider()
            
#             # Feedback Text Area
#             st.markdown("**Tell us more (optional)**")
#             feedback_text = st.text_area(
#                 "Tell us more",
#                 value=st.session_state.feedback_text,
#                 placeholder="What did you like or dislike about this conversation?",
#                 height=120,
#                 label_visibility="collapsed",
#                 key="feedback_textarea"
#             )
#             st.session_state.feedback_text = feedback_text
            
#             # Character count
#             st.caption(f"{len(feedback_text)}/500 characters")
            
#             st.divider()
            
#             # Buttons
#             col_btn1, col_btn2 = st.columns([1, 1])
#             with col_btn1:
#                 if st.button("Cancel", use_container_width=True, key="cancel_feedback_btn"):
#                     st.session_state.show_feedback_modal = False
#                     st.session_state.rating = 0
#                     st.session_state.feedback_text = ""
            
#             with col_btn2:
#                 if st.button("Submit", use_container_width=True, type="primary", key="submit_feedback_btn"):
#                     if st.session_state.rating > 0 or st.session_state.feedback_text:
#                         st.success("✅ Thank you for your feedback!")
#                         feedback_data = {
#                             "rating": st.session_state.rating,
#                             "feedback": st.session_state.feedback_text,
#                             "timestamp": datetime.now()
#                         }
#                         st.session_state.show_feedback_modal = False
#                         st.session_state.rating = 0
#                         st.session_state.feedback_text = ""
#                     else:
#                         st.warning("Please provide at least a rating or feedback")
        
#         show_feedback_form()







import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
import uuid

# Import backend functions
from final_backend import IngestPDF, chatbot, thread_has_document, thread_document_metadata
from langchain_core.messages import HumanMessage

def show():
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
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())
    if "uploaded_file_name" not in st.session_state:
        st.session_state.uploaded_file_name = None

    col1, col2, col3, col4 = st.columns([3, 0.5, 0.5, 1])

    with col1:
        st.markdown("## UPSC GPT")

    with col2:
        if st.button("🔄", help="Text Mode", use_container_width=True, key="text_mode_btn"):
            pass

    with col3:
        if st.button("🌐", help="Language", use_container_width=True, key="lang_btn"):
            pass

    with col4:
        if st.button("📝 Give Feedback", use_container_width=True, key="give_feedback_btn"):
            st.session_state.show_feedback_modal = True

    st.divider()

    # File upload section
    st.markdown("### Upload Your Answer PDF (Optional)")
    uploaded_file = st.file_uploader(
        "Upload PDF for evaluation", 
        type=['pdf'],
        help="Upload your UPSC answer PDF for evaluation and copy-checking",
        key="pdf_uploader"
    )
    
    if uploaded_file is not None:
        if st.session_state.uploaded_file_name != uploaded_file.name:
            with st.spinner("Processing PDF..."):
                try:
                    file_bytes = uploaded_file.read()
                    metadata = IngestPDF(
                        filebytes=file_bytes,
                        thread_id=st.session_state.thread_id,
                        filename=uploaded_file.name
                    )
                    st.session_state.uploaded_file_name = uploaded_file.name
                    st.success(f"✅ PDF uploaded successfully: {metadata['filename']}")
                    st.info(f"📄 Documents: {metadata['documents']} | Chunks: {metadata['chunks']}")
                except Exception as e:
                    st.error(f"❌ Error processing PDF: {str(e)}")

    # Display current document status
    if thread_has_document(st.session_state.thread_id):
        metadata = thread_document_metadata(st.session_state.thread_id)
        st.success(f"📎 Current document: {metadata.get('filename', 'Unknown')}")

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
        "Create a 30-day study plan for UPSC Prelims",
        "Evaluate my uploaded answer and provide feedback"
    ]

    for idx, question in enumerate(suggested_questions):
        if st.button(f"💡 {question}", use_container_width=True, key=f"suggested_q_{idx}"):
            process_user_message(question)

    # Chat messages display
    if st.session_state.messages:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input
    st.divider()
    col1, col2 = st.columns([6, 1])

    with col1:
        user_input = st.text_input(
            "Ask anything...", 
            placeholder="Ask anything about UPSC preparation or your uploaded answer...", 
            label_visibility="collapsed", 
            key="chat_input"
        )

    with col2:
        if st.button("➤", use_container_width=True, type="primary", key="send_btn"):
            if user_input:
                process_user_message(user_input)
                st.rerun()

    # Feedback Modal
    if st.session_state.show_feedback_modal:
        show_feedback_form()


def process_user_message(user_message: str):
    """Process user message through the backend chatbot"""
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_message})
    
    # Prepare config with thread_id
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }
    
    # Get response from chatbot
    try:
        with st.spinner("Thinking..."):
            response = chatbot.invoke(
                {"messages": [HumanMessage(content=user_message)]},
                config=config
            )
            
            # Extract assistant's response
            assistant_message = response["messages"][-1].content
            
            # Add assistant message to session
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_message
            })
    except Exception as e:
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"❌ Error: {str(e)}"
        })


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
            st.rerun()
    
    with col_btn2:
        if st.button("Submit", use_container_width=True, type="primary", key="submit_feedback_btn"):
            if st.session_state.rating > 0 or st.session_state.feedback_text:
                st.success("✅ Thank you for your feedback!")
                feedback_data = {
                    "rating": st.session_state.rating,
                    "feedback": st.session_state.feedback_text,
                    "timestamp": datetime.now()
                }
                # Here you can save feedback_data to a database
                st.session_state.show_feedback_modal = False
                st.session_state.rating = 0
                st.session_state.feedback_text = ""
                st.rerun()
            else:
                st.warning("Please provide at least a rating or feedback")


