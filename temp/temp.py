# import streamlit as st
# from streamlit_option_menu import option_menu

# # Page config
# st.set_page_config(page_title="Dalvoy - UPSC Preparation", layout="wide")

# # Sidebar Menu
# with st.sidebar:
#     st.markdown("### Menu")
#     selected = option_menu(
#         menu_title="",
#         options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
#         icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
#         menu_icon="cast",
#         default_index=7,
#     )
    
#     st.divider()
#     if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
#         pass

# # Header with Navigation
# col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 0.5])

# with col1:
#     st.markdown("### 🎓 Dalvoy")

# with col2:
#     if st.button("✅ Prepare", use_container_width=True, key="prepare_btn"):
#         pass

# with col3:
#     if st.button("📋 Practice", use_container_width=True, key="practice_btn"):
#         pass

# with col4:
#     if st.button("📞 Support", use_container_width=True, key="support_btn"):
#         pass

# with col5:
#     if st.button("💳 Plans", use_container_width=True, key="plans_btn"):
#         pass

# with col6:
#     if st.button("👤", use_container_width=True, key="profile_btn"):
#         pass

# st.divider()

# # Hero Section
# col1, col2 = st.columns([1, 1])

# with col1:
#     st.markdown("""
#     <h1 style='font-size: 48px; font-weight: bold; color: #003d99; line-height: 1.2;'>
#     Crack UPSC IAS<br>With Dalvoy AI
#     </h1>
#     """, unsafe_allow_html=True)
    
#     st.markdown("""
#     <p style='font-size: 18px; color: #0052cc; line-height: 1.6;'>
#     Ace UPSC with our Mains Evaluator, UPSC Mentor, PYQ/Mock Test generator and Daily Current Affairs. Your complete one-stop solution for UPSC success.
#     </p>
#     """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     if st.button("🚀 Start Prep →", use_container_width=True, key="start_prep_btn"):
#         st.success("Starting UPSC Preparation!")
    
#     st.markdown("")
#     st.markdown("""
#     <div style='display: flex; align-items: center; gap: 8px;'>
#     <span style='color: #22c55e; font-size: 20px;'>✅</span>
#     <span style='font-size: 16px; color: #0052cc;'>Join 1 Lakh+ Aspirants</span>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div style='text-align: center; padding: 40px;'>
#     <div style='font-size: 80px;'>📚</div>
#     <p style='margin: 20px 0; color: #666;'>UPSC Preparation Guide</p>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # See Dalvoy in Action Section
# st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>See Dalvoy in Action</h2>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 1])

# with col1:
#     st.markdown("""
#     <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
#     <div style='font-size: 24px; font-weight: bold; color: #003d99;'>Mains Evaluator</div>
#     <p style='color: #666; margin: 10px 0;'>Evaluate your Mains answers with UPSC Level Feedback within 60s.</p>
#     <div style='text-align: right;'>➤</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     st.markdown("""
#     <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
#     <div style='font-weight: bold; color: #000;'>UPSC GPT</div>
#     <div style='text-align: right;'>➤</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     st.markdown("""
#     <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
#     <div style='font-weight: bold; color: #000;'>Test Generator</div>
#     <div style='text-align: right;'>➤</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("")
    
#     st.markdown("""
#     <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
#     <div style='font-weight: bold; color: #000;'>Current Affairs</div>
#     <div style='text-align: right;'>➤</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div style='background: linear-gradient(135deg, #e0e7ff 0%, #f0f9ff 100%); border-radius: 12px; padding: 30px; height: 100%;'>
#     <div style='text-align: center; padding: 20px;'>
#     <div style='font-size: 60px;'>⏳</div>
#     <p style='margin: 15px 0; color: #0052cc; font-weight: bold;'>AI Evaluation in Progress</p>
#     <div style='background: #0052cc; height: 6px; border-radius: 3px; margin: 20px 0; width: 100%;'></div>
#     <p style='color: #666; font-size: 14px;'>Stage 2: Generating personalized feedback</p>
#     </div>
#     <div style='margin-top: 40px; padding: 20px; background: white; border-radius: 8px;'>
#     <p style='color: #0052cc; font-weight: bold; margin: 0;'>Evaluation Results</p>
#     <div style='margin-top: 20px;'>
#     <div style='display: flex; justify-content: space-between;'>
#     <span style='color: #0052cc; font-size: 24px; font-weight: bold;'>4.5/10</span>
#     <span style='color: #666; font-size: 14px;'>Download PDF</span>
#     </div>
#     <p style='color: #666; font-size: 12px; margin: 10px 0;'>General Studies Paper I</p>
#     <p style='color: #999; font-size: 11px;'>10 marks</p>
#     <p style='color: #666; font-size: 12px; margin: 10px 0;'>Detailed Scorecard</p>
#     </div>
#     </div>
#     </div>
#     """, unsafe_allow_html=True)

# st.divider()

# # What Our Users Say Section
# st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>What Our Users Say</h2>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)

# testimonials = [
#     {
#         "name": "Tanya Agarwal",
#         "role": "RBI Manager | UPSC 2020 Prelims and Mains Qualified",
#         "rating": 5,
#         "text": "Dalvoy created crisp notes on tough topics like polity and economy in seconds. It saved hours of reading and helped me revise quickly when time was limited."
#     },
#     {
#         "name": "Mohit",
#         "role": "UPSC Mains 2025 Qualified | RBI Manager",
#         "rating": 5,
#         "text": "Dalvoy ka optional evaluation kamaal ka tha. Instant and detailed feedback mil gaya jisme usually weeks lagte hain mehenge padhai hai. Literature optional ke weak areas exam se pehle improve kar paaya, usse kaafi madad hui."
#     },
#     {
#         "name": "Siddharth",
#         "role": "UPSC Prelims 2025 Qualified",
#         "rating": 5,
#         "text": "Dalvoy made a personalized study plan that perfectly fixed my time management issue. It guided me till the last week and solved every doubt with ease, which boosted my confidence for Prelims."
#     }
# ]

# for idx, testimonial in enumerate(testimonials):
#     with [col1, col2, col3][idx]:
#         st.markdown(f"""
#         <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; height: 100%;'>
#         <div style='text-align: center;'>
#         <div style='width: 80px; height: 80px; background: #ddd; border-radius: 50%; margin: 0 auto 15px;'></div>
#         <p style='font-weight: bold; color: #000; margin: 0;'>{testimonial["name"]}</p>
#         <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>{testimonial["role"]}</p>
#         <p style='color: #ffa500; font-size: 16px; margin: 10px 0;'>{'⭐' * testimonial["rating"]}</p>
#         </div>
#         <p style='color: #666; font-size: 14px; line-height: 1.6; margin-top: 15px;'>{testimonial["text"]}</p>
#         </div>
#         """, unsafe_allow_html=True)

# st.divider()

# # Built by IITians Section
# col1, col2 = st.columns([1, 1])

# with col1:
#     st.markdown("""
#     <h2 style='color: #003d99; font-size: 32px;'>Built by IITians</h2>
#     <p style='color: #666; font-size: 16px; line-height: 1.6;'>
#     Our team is on a mission to democratize learning through AI by providing customizable and interactive learning solutions to students across the globe.
#     </p>
#     """, unsafe_allow_html=True)

# with col2:
#     col_a, col_b = st.columns(2)
    
#     with col_a:
#         st.markdown("""
#         <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; text-align: center;'>
#         <div style='width: 120px; height: 120px; background: linear-gradient(135deg, #87ceeb 0%, #e0ffff 100%); border-radius: 12px; margin: 0 auto 15px;'></div>
#         <p style='font-weight: bold; color: #000; margin: 10px 0;'>Ritik</p>
#         <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>Co-Founder</p>
#         <p style='color: #0052cc; font-size: 20px; margin: 10px 0;'>🔗</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_b:
#         st.markdown("""
#         <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; text-align: center;'>
#         <div style='width: 120px; height: 120px; background: linear-gradient(135deg, #87ceeb 0%, #e0ffff 100%); border-radius: 12px; margin: 0 auto 15px;'></div>
#         <p style='font-weight: bold; color: #000; margin: 10px 0;'>Akash Sharma</p>
#         <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>Co-Founder</p>
#         <p style='color: #0052cc; font-size: 20px; margin: 10px 0;'>🔗</p>
#         </div>
#         """, unsafe_allow_html=True)

# st.divider()

# # FAQ Section
# st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)

# faqs = [
#     {
#         "q": "How does AI-powered UPSC mains answer evaluation work?",
#         "a": "Our AI analyzes your answers against UPSC standards, provides detailed feedback on content, structure, and presentation within 60 seconds."
#     },
#     {
#         "q": "Is Dalvoy suitable for Hindi medium UPSC aspirants?",
#         "a": "Yes! Dalvoy supports multiple languages including Hindi. All features are available in Hindi for comprehensive support."
#     },
#     {
#         "q": "Can I get free UPSC mock tests and practice questions on Dalvoy?",
#         "a": "Yes, we offer free tier with limited mock tests and practice questions. Upgrade to premium for unlimited access."
#     },
#     {
#         "q": "How is Dalvoy different from traditional UPSC coaching institutes?",
#         "a": "Dalvoy uses AI for personalized feedback, instant evaluation, and adaptive learning - much faster than traditional coaching."
#     },
# ]

# for faq in faqs:
#     with st.expander(faq["q"]):
#         st.write(faq["a"])



import streamlit as st
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="Dalvoy - UPSC Preparation", layout="wide")

# Sidebar Menu
with st.sidebar:
    st.markdown("### Menu")
    selected = option_menu(
        menu_title="",
        options=["UPSC GPT", "Test Generator", "AI Maps", "Mains Evaluator", "Current Affairs", "UPSC Puzzle", "Dashboard", "Home"],
        icons=["lightning-charge", "file-text", "map", "pencil-square", "newspaper", "puzzle", "speedometer", "house"],
        menu_icon="cast",
        default_index=7,
    )
    
    st.divider()
    if st.button("❓ Not Satisfied?", key="not_satisfied_btn"):
        pass

# Header with Navigation
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 0.5])

with col1:
    st.markdown("### 🎓 Dalvoy")

with col2:
    if st.button("✅ Prepare", use_container_width=True, key="prepare_btn"):
        pass

with col3:
    if st.button("📋 Practice", use_container_width=True, key="practice_btn"):
        pass

with col4:
    if st.button("📞 Support", use_container_width=True, key="support_btn"):
        pass

with col5:
    if st.button("💳 Plans", use_container_width=True, key="plans_btn"):
        pass

with col6:
    if st.button("👤", use_container_width=True, key="profile_btn"):
        pass

st.divider()

# Hero Section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <h1 style='font-size: 48px; font-weight: bold; color: #003d99; line-height: 1.2;'>
    Crack UPSC IAS<br>With Dalvoy AI
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style='font-size: 18px; color: #0052cc; line-height: 1.6;'>
    Ace UPSC with our Mains Evaluator, UPSC Mentor, PYQ/Mock Test generator and Daily Current Affairs. Your complete one-stop solution for UPSC success.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("🚀 Start Prep →", use_container_width=True, key="start_prep_btn"):
        st.success("Starting UPSC Preparation!")
    
    st.markdown("")
    st.markdown("""
    <div style='display: flex; align-items: center; gap: 8px;'>
    <span style='color: #22c55e; font-size: 20px;'>✅</span>
    <span style='font-size: 16px; color: #0052cc;'>Join 1 Lakh+ Aspirants</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 40px;'>
    <div style='font-size: 80px;'>📚</div>
    <p style='margin: 20px 0; color: #666;'>UPSC Preparation Guide</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# See Dalvoy in Action Section
st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>See Dalvoy in Action</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
    <div style='font-size: 24px; font-weight: bold; color: #003d99;'>Mains Evaluator</div>
    <p style='color: #666; margin: 10px 0;'>Evaluate your Mains answers with UPSC Level Feedback within 60s.</p>
    <div style='text-align: right;'>➤</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
    <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
    <div style='font-weight: bold; color: #000;'>UPSC GPT</div>
    <div style='text-align: right;'>➤</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
    <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
    <div style='font-weight: bold; color: #000;'>Test Generator</div>
    <div style='text-align: right;'>➤</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
    <div style='border: 2px solid #e0e0e0; border-radius: 12px; padding: 20px; cursor: pointer;'>
    <div style='font-weight: bold; color: #000;'>Current Affairs</div>
    <div style='text-align: right;'>➤</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #e0e7ff 0%, #f0f9ff 100%); border-radius: 12px; padding: 30px; height: 100%;'>
    <div style='text-align: center; padding: 20px;'>
    <div style='font-size: 60px;'>⏳</div>
    <p style='margin: 15px 0; color: #0052cc; font-weight: bold;'>AI Evaluation in Progress</p>
    <div style='background: #0052cc; height: 6px; border-radius: 3px; margin: 20px 0; width: 100%;'></div>
    <p style='color: #666; font-size: 14px;'>Stage 2: Generating personalized feedback</p>
    </div>
    <div style='margin-top: 40px; padding: 20px; background: white; border-radius: 8px;'>
    <p style='color: #0052cc; font-weight: bold; margin: 0;'>Evaluation Results</p>
    <div style='margin-top: 20px;'>
    <div style='display: flex; justify-content: space-between;'>
    <span style='color: #0052cc; font-size: 24px; font-weight: bold;'>4.5/10</span>
    <span style='color: #666; font-size: 14px;'>Download PDF</span>
    </div>
    <p style='color: #666; font-size: 12px; margin: 10px 0;'>General Studies Paper I</p>
    <p style='color: #999; font-size: 11px;'>10 marks</p>
    <p style='color: #666; font-size: 12px; margin: 10px 0;'>Detailed Scorecard</p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# What Our Users Say Section
st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>What Our Users Say</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

testimonials = [
    {
        "name": "Tanya Agarwal",
        "role": "RBI Manager | UPSC 2020 Prelims and Mains Qualified",
        "rating": 5,
        "text": "Dalvoy created crisp notes on tough topics like polity and economy in seconds. It saved hours of reading and helped me revise quickly when time was limited."
    },
    {
        "name": "Mohit",
        "role": "UPSC Mains 2025 Qualified | RBI Manager",
        "rating": 5,
        "text": "Dalvoy ka optional evaluation kamaal ka tha. Instant and detailed feedback mil gaya jisme usually weeks lagte hain mehenge padhai hai. Literature optional ke weak areas exam se pehle improve kar paaya, usse kaafi madad hui."
    },
    {
        "name": "Siddharth",
        "role": "UPSC Prelims 2025 Qualified",
        "rating": 5,
        "text": "Dalvoy made a personalized study plan that perfectly fixed my time management issue. It guided me till the last week and solved every doubt with ease, which boosted my confidence for Prelims."
    }
]

for idx, testimonial in enumerate(testimonials):
    with [col1, col2, col3][idx]:
        st.markdown(f"""
        <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; height: 100%;'>
        <div style='text-align: center;'>
        <div style='width: 80px; height: 80px; background: #ddd; border-radius: 50%; margin: 0 auto 15px;'></div>
        <p style='font-weight: bold; color: #000; margin: 0;'>{testimonial["name"]}</p>
        <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>{testimonial["role"]}</p>
        <p style='color: #ffa500; font-size: 16px; margin: 10px 0;'>{'⭐' * testimonial["rating"]}</p>
        </div>
        <p style='color: #666; font-size: 14px; line-height: 1.6; margin-top: 15px;'>{testimonial["text"]}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Built by IITians Section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <h2 style='color: #003d99; font-size: 32px;'>Built by Techie</h2>
    <p style='color: #666; font-size: 16px; line-height: 1.6;'>
    Our team is on a mission to democratize learning through AI by providing customizable and interactive learning solutions to students across the globe.
    </p>
    """, unsafe_allow_html=True)

with col2:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; text-align: center;'>
        <div style='width: 120px; height: 120px; background: linear-gradient(135deg, #87ceeb 0%, #e0ffff 100%); border-radius: 12px; margin: 0 auto 15px;'></div>
        <p style='font-weight: bold; color: #000; margin: 10px 0;'>Sachin</p>
        <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>Co-Founder</p>
        <p style='color: #0052cc; font-size: 20px; margin: 10px 0;'>🔗</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
        <div style='background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 20px; text-align: center;'>
        <div style='width: 120px; height: 120px; background: linear-gradient(135deg, #87ceeb 0%, #e0ffff 100%); border-radius: 12px; margin: 0 auto 15px;'></div>
        <p style='font-weight: bold; color: #000; margin: 10px 0;'>Shantanu</p>
        <p style='color: #0052cc; font-size: 14px; margin: 5px 0;'>Co-Founder</p>
        <p style='color: #0052cc; font-size: 20px; margin: 10px 0;'>🔗</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# FAQ Section
st.markdown("<h2 style='text-align: center; color: #0052cc; font-size: 36px;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)

faqs = [
    {
        "q": "How does AI-powered UPSC mains answer evaluation work?",
        "a": "Our AI analyzes your answers against UPSC standards, provides detailed feedback on content, structure, and presentation within 60 seconds."
    },
    {
        "q": "Is Dalvoy suitable for Hindi medium UPSC aspirants?",
        "a": "Yes! Dalvoy supports multiple languages including Hindi. All features are available in Hindi for comprehensive support."
    },
    {
        "q": "Can I get free UPSC mock tests and practice questions on Dalvoy?",
        "a": "Yes, we offer free tier with limited mock tests and practice questions. Upgrade to premium for unlimited access."
    },
    {
        "q": "How is Dalvoy different from traditional UPSC coaching institutes?",
        "a": "Dalvoy uses AI for personalized feedback, instant evaluation, and adaptive learning - much faster than traditional coaching."
    },
]

for faq in faqs:
    with st.expander(faq["q"]):
        st.write(faq["a"])
