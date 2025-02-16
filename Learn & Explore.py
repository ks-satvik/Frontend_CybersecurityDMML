import streamlit as st

# Configure the app
st.set_page_config(
    page_title="CyberCloud AI Buddy",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for a better UI
st.markdown(
    """
    <style>
        /* Center the main content */
        .main-container {
            text-align: center;
            margin-top: 20px;
        }

        /* Center the logo */
        .logo-container {
            display: flex;
            justify-content: center;
        }

        /* Style the Student Access button */
        .student-access-btn {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        
        .stButton>button {
            font-size: 18px;
            padding: 12px 30px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            display: block;
            margin: 0 auto;
        }
        
        .stButton>button:hover {
            background-color: #388E3C;
        }

        /* Style the footer */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #aaa;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ASU Logo (Centered)
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
st.image("assets/asu_logo.png", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Main Heading
st.markdown(
    """
    <div class="main-container">
        <h1 style='color: #4CAF50;'>Welcome to CyberCloud AI Buddy</h1>
        <p style='font-size: 20px; color: #444;'>Your AI-powered learning companion for Cloud Computing and Cybersecurity!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Quote by a cybersecurity scientist
st.markdown(
    """
    <div class="main-container">
        <blockquote style='font-size: 18px; font-style: italic; color: #555; border-left: 4px solid #4CAF50; padding-left: 10px;'>
        "The best defense against cyberattacks is a well-trained mind and a vigilant eye." – Dr. Bruce Schneier
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# 🎯 **THIS is the Correctly Functioning Button**
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Student Access / Signup"):
        st.switch_page("pages/1_Student Access 🎓.py")

# Footer with slight spacing
st.markdown(
    """
    <br><hr>
    <footer class="footer">
        Arizona State University | Powered by CyberCloud AI Buddy
    </footer>
    """,
    unsafe_allow_html=True,
)
