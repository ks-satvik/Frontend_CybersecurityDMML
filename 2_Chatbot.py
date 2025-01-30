import streamlit as st

st.set_page_config(
    page_title="CyberQ AI - Chatbot",
    page_icon="🤖",
)

st.markdown(
    """
    <h2 style='text-align: center;'>CyberQ AI Chatbot</h2>
    <p style='text-align: center;'>Ask your cybersecurity-related questions and get expert guidance instantly!</p>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat UI
st.markdown("### Chat with CyberQ AI")
for chat in st.session_state["chat_history"]:
    with st.container():
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**CyberQ:** {chat['bot']}")

# Chat Input
with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input("Type your question here:")
    send_button = st.form_submit_button("Send")

# Chat response logic
if send_button:
    if user_message.strip():
        bot_response = "This is a placeholder response. AI model integration pending."
        st.session_state["chat_history"].append(
            {"user": user_message, "bot": bot_response}
        )
        st.experimental_rerun()
    else:
        st.error("Please enter a message.")
