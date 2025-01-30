import streamlit as st

# Configure the app
st.set_page_config(
    page_title="CyberQ AI",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Arizona State University logo (ensure "asu_logo.png" is in the "assets/" folder)
st.image("assets/asu_logo.png", use_container_width=True)  # Updated to use use_container_width

# Main Heading
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50; margin-top: 20px;'>Welcome to CyberQ AI</h1>
    <p style='text-align: center; font-size: 20px; color: #444;'>Your ultimate cybersecurity learning companion.</p>
    """,
    unsafe_allow_html=True,
)

# Quote by a great cybersecurity scientist
st.markdown(
    """
    <blockquote style='text-align: center; font-size: 18px; font-style: italic; color: #555; border-left: 4px solid #4CAF50; padding-left: 10px;'>
    "The best defense against cyberattacks is a well-trained mind and a vigilant eye." – Dr. Bruce Schneier
    </blockquote>
    """,
    unsafe_allow_html=True,
)

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Login and Signup Buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <a href="./pages/1_Login.py" style="text-decoration: none;">
                <button style='font-size: 18px; padding: 12px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer; margin-right: 20px;'>
                    Login
                </button>
            </a>
            <a href="./pages/1_Login.py" style="text-decoration: none;">
                <button style='font-size: 18px; padding: 12px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;'>
                    Signup
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer with slight spacing
st.markdown(
    """
    <br><hr>
    <footer style='text-align: center; font-size: 14px; color: #aaa;'>
        Arizona State University | Powered by CyberQ AI
    </footer>
    """,
    unsafe_allow_html=True,
)
