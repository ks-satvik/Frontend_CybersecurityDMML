import streamlit as st

st.set_page_config(
    page_title="CyberCloud AI Buddy - Student Access",
    page_icon="🔐",
    layout="centered",
)

# Custom CSS
st.markdown(
    """
    <style>
        .container {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .content {
            flex: 1;
        }
        .image-container {
            flex: 0.6;
            text-align: center;
        }
        img {
            max-width: 80%;
            height: auto;
        }
        h2 {
            font-size: 24px;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
            color: #555;
            text-align: center;
        }
        .form-container {
            margin-top: 20px;
        }
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Tabs for Student Access and Sign Up
tab1, tab2 = st.tabs(["Student Access 🎓", "Sign Up"])  # ✅ Fixed tab creation

# 🎓 **Student Access (Login) Tab**
with tab1:
    st.markdown("<h2>Student Access to CyberCloud AI Buddy</h2>", unsafe_allow_html=True)
    
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password", help="Make sure to use a strong password.")
        login_button = st.form_submit_button("Access CyberCloud AI")

        if login_button:
            if username and password:
                if username == "admin" and password == "admin123":
                    st.success("Welcome, admin!")
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please fill in both fields.")

# 📝 **Sign Up Tab (Now Correctly Indented)**
with tab2:
    st.markdown("<h2>Create Your CyberCloud AI Buddy Account</h2>", unsafe_allow_html=True)

    with st.form("signup_form", clear_on_submit=True):
        email = st.text_input("Email Address", placeholder="Enter your email")
        new_username = st.text_input("Username", placeholder="Choose a username")
        new_password = st.text_input("Password", type="password", placeholder="Create a password")
        signup_button = st.form_submit_button("Sign Up")

        if signup_button:
            if email and new_username and new_password:
                st.success("Account created successfully! You can now log in.")
            else:
                st.error("Please fill in all fields.")
