
# import streamlit as st

# def show_login():
#     col1, col2, col3 = st.columns([1, 1, 1])
    
#     with col2:
#         st.markdown("<h1 style='text-align: center; color: #0052cc;'>🎓 Dalvoy</h1>", unsafe_allow_html=True)
#         st.markdown("<p style='text-align: center; color: #666;'>Master UPSC with AI-Powered Learning</p>", unsafe_allow_html=True)
        
#         st.divider()
        
#         tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
#         with tab1:
#             st.markdown("### Login to Your Account")
#             email = st.text_input("Email", placeholder="your@email.com", key="login_email")
#             password = st.text_input("Password", type="password", key="login_password")
            
#             if st.button("Login", use_container_width=True, type="primary", key="login_btn"):
#                 if email and password:
#                     st.session_state.logged_in = True
#                     st.session_state.username = email.split('@')[0]
#                     st.success(f"Welcome {st.session_state.username}!")
#                     st.rerun()
#                 else:
#                     st.error("Please enter email and password")
        
#         with tab2:
#             st.markdown("### Create New Account")
#             new_email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
#             new_password = st.text_input("Password", type="password", key="signup_password")
#             confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
            
#             if st.button("Sign Up", use_container_width=True, type="primary", key="signup_btn"):
#                 if new_email and new_password and confirm_password:
#                     if new_password == confirm_password:
#                         st.session_state.logged_in = True
#                         st.session_state.username = new_email.split('@')[0]
#                         st.success(f"Account created! Welcome {st.session_state.username}!")
#                         st.rerun()
#                     else:
#                         st.error("Passwords don't match!")
#                 else:
#                     st.error("Please fill all fields")


import streamlit as st
import sqlite3
import hashlib
import re
from datetime import datetime

# ==================== DATABASE SETUP ====================

def init_db():
    """Initialize SQLite database for user management"""
    try:
        conn = sqlite3.connect("dalvoy_users.db")
        cursor = conn.cursor()
        
        # Create users table
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
        print(f"Error initializing database: {e}")
        return False

# ==================== UTILITY FUNCTIONS ====================

def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> tuple[bool, str]:
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number"
    return True, "Password is strong"

def validate_phone(phone: str) -> bool:
    """Validate Indian phone number"""
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone.replace(" ", "")) is not None if phone else True

def user_exists(email: str) -> bool:
    """Check if user already exists"""
    conn = sqlite3.connect("dalvoy_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def register_user(full_name: str, email: str, phone: str, password: str, 
                  bpsc_attempt: str, commitment_4hrs: bool) -> tuple[bool, str]:
    """Register a new user"""
    try:
        conn = sqlite3.connect("dalvoy_users.db")
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        
        cursor.execute("""
            INSERT INTO users (full_name, email, phone, password_hash, bpsc_attempt, commitment_4hrs)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (full_name, email, phone, password_hash, bpsc_attempt, commitment_4hrs))
        
        conn.commit()
        conn.close()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "Email already registered. Please login instead."
    except Exception as e:
        return False, f"Registration failed: {str(e)}"

def authenticate_user(email: str, password: str) -> tuple[bool, str, dict]:
    """Authenticate user and return user data"""
    try:
        conn = sqlite3.connect("dalvoy_users.db")
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        cursor.execute("""
            SELECT id, full_name, email, bpsc_attempt, commitment_4hrs 
            FROM users 
            WHERE email = ? AND password_hash = ?
        """, (email, password_hash))
        
        user = cursor.fetchone()
        
        if user:
            user_id, full_name, email_val, bpsc_attempt, commitment = user
            
            # Update last login
            cursor.execute("""
                UPDATE users 
                SET last_login = CURRENT_TIMESTAMP 
                WHERE id = ?
            """, (user_id,))
            conn.commit()
            
            user_data = {
                "id": user_id,
                "full_name": full_name,
                "email": email_val,
                "bpsc_attempt": bpsc_attempt,
                "commitment_4hrs": commitment
            }
            conn.close()
            return True, "Login successful!", user_data
        else:
            conn.close()
            return False, "Invalid email or password", {}
    
    except Exception as e:
        return False, f"Authentication failed: {str(e)}", {}

# ==================== UI COMPONENTS ====================

def show_login():
    """Display login and signup interface"""
    
    # Initialize database - CRITICAL
    if not init_db():
        st.error("❌ Failed to initialize database. Please restart the application.")
        return
    
    # Main container with custom styling
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        # Header with logo
        st.markdown("""
            <div style='text-align: center; padding: 30px 0;'>
                <h1 style='color: #0052cc; margin-bottom: 0; font-size: 48px;'>🎓BPSC LAKSHYA</h1>
                <p style='color: #666; font-size: 16px; margin-top: 5px;'>Master BPSC with AI-Powered Learning</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Tabs for login and signup
        tab1, tab2 = st.tabs(["🔓 Login", "✍️ Sign Up"])
        
        # ==================== LOGIN TAB ====================
        with tab1:
            st.markdown("### Welcome Back")
            
            login_email = st.text_input(
                "Email",
                placeholder="your@email.com",
                key="login_email",
                help="Enter your registered email"
            )
            
            login_password = st.text_input(
                "Password",
                type="password",
                key="login_password",
                placeholder="Enter your password",
                help="Enter your password"
            )
            
            # Forgot password option
            col_forgot1, col_forgot2 = st.columns([1, 1])
            with col_forgot1:
                st.markdown("""
                    <small><a href="#" style='color: #0052cc; text-decoration: none;'>Forgot Password?</a></small>
                """, unsafe_allow_html=True)
            
            if st.button(
                "🔓 Login",
                use_container_width=True,
                type="primary",
                key="login_btn",
                help="Click to login to your account"
            ):
                if not login_email or not login_password:
                    st.error("❌ Please enter both email and password")
                elif not validate_email(login_email):
                    st.error("❌ Invalid email format")
                else:
                    success, message, user_data = authenticate_user(login_email, login_password)
                    
                    if success:
                        st.session_state.logged_in = True
                        st.session_state.username = user_data["full_name"].split()[0]
                        st.session_state.user_id = user_data["id"]
                        st.session_state.email = user_data["email"]
                        st.session_state.bpsc_attempt = user_data["bpsc_attempt"]
                        
                        st.success(f"✅ {message}")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
            
            st.markdown("---")
            st.markdown("""
                <div style='text-align: center; margin-top: 20px;'>
                    <p style='color: #999; font-size: 14px;'>Don't have an account? Click the <strong>Sign Up</strong> tab above</p>
                </div>
            """, unsafe_allow_html=True)
        
        # ==================== SIGNUP TAB ====================
        with tab2:
            st.markdown("### Embark on Your Journey")
            
            # Progress indicator
            st.markdown("""
                <div style='background: linear-gradient(to right, #00d4ff 50%, #e0e0e0 50%); 
                            height: 3px; border-radius: 3px; margin-bottom: 20px;'></div>
                <p style='text-align: center; color: #666; font-size: 12px;'>Step 1 of 2: Create Account</p>
            """, unsafe_allow_html=True)
            
            # Full Name
            signup_full_name = st.text_input(
                "Full Name",
                placeholder="Enter your full name",
                key="signup_fullname",
                help="Your complete name"
            )
            
            # Email
            signup_email = st.text_input(
                "Email",
                placeholder="your@email.com",
                key="signup_email",
                help="We'll use this to log you in"
            )
            
            # Phone (Optional)
            signup_phone = st.text_input(
                "Phone Number (Optional)",
                placeholder="10-digit mobile number",
                key="signup_phone",
                help="Indian phone number (10 digits)"
            )
            
            # Password
            signup_password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
                placeholder="Create a strong password",
                help="Min 8 chars, 1 uppercase, 1 number"
            )
            
            # Password strength indicator
            if signup_password:
                is_strong, strength_msg = validate_password(signup_password)
                if is_strong:
                    st.success(f"✅ {strength_msg}")
                else:
                    st.warning(f"⚠️ {strength_msg}")
            
            # Confirm Password
            signup_confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="signup_confirm_password",
                placeholder="Re-enter your password"
            )
            
            # BPSC Attempt
            signup_bpsc_attempt = st.selectbox(
                "Which UPSC/BPSC attempt is this for?",
                ["71st", "72nd", "73rd", "74th", "75th+"],
                key="signup_bpsc",
                help="Select your attempt number"
            )
            
            # Commitment checkbox
            signup_commitment = st.checkbox(
                "✅ I commit to 4+ hours of dedicated study today",
                key="signup_commitment",
                help="Show your dedication to preparation"
            )
            
            # Terms and Privacy
            st.markdown("""
                <small style='color: #999;'>By continuing, I agree to our 
                <a href="#" style='color: #0052cc; text-decoration: none;'>Terms & Privacy Policy</a></small>
            """, unsafe_allow_html=True)
            
            if st.button(
                "🚀 Start My Journey",
                use_container_width=True,
                type="primary",
                key="signup_btn",
                help="Create your account and begin learning"
            ):
                # Validation
                if not all([signup_full_name, signup_email, signup_password, signup_confirm_password]):
                    st.error("❌ Please fill all required fields")
                
                elif len(signup_full_name.strip().split()) < 2:
                    st.error("❌ Please enter your full name (first and last name)")
                
                elif not validate_email(signup_email):
                    st.error("❌ Invalid email format")
                
                elif signup_phone and not validate_phone(signup_phone):
                    st.error("❌ Invalid phone number. Please enter a valid 10-digit number")
                
                elif signup_password != signup_confirm_password:
                    st.error("❌ Passwords don't match!")
                
                else:
                    is_strong, strength_msg = validate_password(signup_password)
                    if not is_strong:
                        st.error(f"❌ {strength_msg}")
                    else:
                        if user_exists(signup_email):
                            st.error("❌ Email already registered. Please login instead.")
                        else:
                            success, message = register_user(
                                signup_full_name,
                                signup_email,
                                signup_phone,
                                signup_password,
                                signup_bpsc_attempt,
                                signup_commitment
                            )
                            
                            if success:
                                st.success(f"✅ {message}")
                                st.info("📝 Please login with your credentials above")
                                st.balloons()
                            else:
                                st.error(f"❌ {message}")
        
        st.divider()
        st.markdown("""
            <div style='text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px; margin-top: 20px;'>
                <p style='color: #333; font-size: 14px; margin: 0;'>
                    <strong>"Success is the sum of small efforts, repeated day in and day out."</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)