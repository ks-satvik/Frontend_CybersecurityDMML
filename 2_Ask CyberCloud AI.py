import streamlit as st

st.set_page_config(
    page_title="CyberCloud AI Buddy - Chatbot",
    page_icon="🤖",
)

# Custom CSS for Visual Improvements
st.markdown(
    """
    <style>
        /* Center the main heading */
        .main-heading {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2E7D32;
            margin-bottom: 10px;
        }

        /* Center subheadings with spacing */
        .subheading {
            text-align: center;
            font-size: 18px;
            color: #444;
            margin-bottom: 5px;
        }

        /* Style the chat history container */
        .chat-container {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
        }

        /* Style user messages */
        .user-message {
            font-weight: bold;
            color: #1565C0;
        }

        /* Style bot responses */
        .bot-message {
            color: #333;
            font-style: italic;
        }

        /* Style the disclaimer */
        .disclaimer {
            text-align: justify;
            font-size: 14px;
            color: #888;
            padding: 15px;
            background: #f1f1f1;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 📢 **Main Title & Description (Visually Improved)**
st.markdown("<h2 class='main-heading'>CyberCloud AI Buddy Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p class='subheading'>☁️ Want to explore Cloud Computing models like IaaS, PaaS, SaaS, and deployment options?</p>", unsafe_allow_html=True)
st.markdown("<p class='subheading'>💡 Got questions about cyber threats, vulnerabilities, network security tools, or defense strategies?</p>", unsafe_allow_html=True)
st.markdown("<p class='subheading'>🚀 This space is here to help you learn key concepts, deepen your understanding, and help with projects.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 💬 **Chat UI**
st.markdown("### Your Learning History 📖")
if not st.session_state["chat_history"]:
    st.info("Dive In – Start Building Your Knowledge Library!")

for chat in st.session_state["chat_history"]:
    with st.container():
        st.markdown(f"<p class='user-message'>🧑‍💻 You: {chat['user']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='bot-message'>🤖 CyberCloud AI Buddy: {chat['bot']}</p>", unsafe_allow_html=True)

# ✍ **Chat Input Box**
with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input("Type your question on cloud or cybersecurity – let’s learn together!")
    send_button = st.form_submit_button("Ask CyberCloud AI")

# 🤖 **Chat Response Logic**
if send_button:
    if user_message.strip():
        bot_response = "🔍 This is a placeholder response. AI model integration pending."
        st.session_state["chat_history"].append(
            {"user": user_message, "bot": bot_response}
        )
        st.experimental_rerun()
    else:
        st.error("⚠️ Please enter a valid question.")

#  **Disclaimer (Now Looks More Professional)**
st.markdown(
    """
    <div class="disclaimer">
        <b>Disclaimer:</b> 
        This project is also being used to evaluate the performance and use of LLMs in education through our ontology-validation approach.
        By using this bot, you are contributing to the development of a robust AI-driven learning system.  
        If you find any answers that do not meet your expectations, please let the bot know—we will analyze the logs and improve the system.  
        Your feedback helps shape the future of AI in education! 
    </div>
    """,
    unsafe_allow_html=True,
)

