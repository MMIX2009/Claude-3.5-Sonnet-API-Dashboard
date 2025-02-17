import streamlit as st
import os
import anthropic
import pyttsx3

ANTHROPIC_API_KEY = "*************************************"
# Initialize Anthropic client
# client = anthropic.Client(api_key=os.environ.get("ANTHROPIC_API_KEY"))
client = anthropic.Client(api_key=ANTHROPIC_API_KEY)
# client = anthropic.Client(api_key="your-hardcoded-api-key")


# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Streamlit app layout
st.set_page_config(page_title="Claude 3.5 Dashboard", layout="wide")
st.title("Claude 3.5 Sonnet API Dashboard")

# Sidebar for user input
with st.sidebar:
    st.header("Settings")
    max_tokens = st.slider("Max Tokens", min_value=100, max_value=4096, value=1024)
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    top_p = st.slider("Top P", min_value=0.1, max_value=1.0, value=0.9)

# Helper function to call Claude API
def get_claude_response(prompt, max_tokens=max_tokens, temperature=temperature, top_p=top_p):
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Tabs for different functionalities
tabs = st.tabs(["Text Summarization", "Code Review", "Interactive Chat", "Custom Prompt", "Text-to-Speech", "Document Comparison", "Entity Recognition", "Topic Classification"])

# Text Summarization
with tabs[0]:
    st.subheader("Text Summarization")
    text_to_summarize = st.text_area("Enter text to summarize")
    if st.button("Summarize"):
        if text_to_summarize:
            summary = get_claude_response(f"Summarize this text: {text_to_summarize}")
            st.write(summary)

# Code Review
with tabs[1]:
    st.subheader("Code Review")
    code_snippet = st.text_area("Enter code for review")
    if st.button("Review Code"):
        if code_snippet:
            review = get_claude_response(f"Review this code for bugs, performance improvements, and best practices:\n{code_snippet}")
            st.write(review)

# Interactive Chat
with tabs[2]:
    st.subheader("Interactive Chat")
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    user_message = st.text_input("Enter your message")
    if st.button("Send"):
        if user_message:
            st.session_state["chat_history"].append({"role": "user", "content": user_message})
            response = get_claude_response(user_message)
            if response:
                st.session_state["chat_history"].append({"role": "assistant", "content": response})

    # Display chat history
    for msg in st.session_state["chat_history"]:
        role = "🧑 User" if msg["role"] == "user" else "🤖 Claude"
        st.text(f"{role}: {msg['content']}")

# Custom Prompt
with tabs[3]:
    st.subheader("Custom Prompt")
    custom_prompt = st.text_area("Enter your prompt")
    if st.button("Submit"):
        if custom_prompt:
            response = get_claude_response(custom_prompt)
            st.write(response)

# Text-to-Speech
with tabs[4]:
    st.subheader("Text-to-Speech")
    tts_text = st.text_area("Enter text to convert to speech")
    if st.button("Convert to Speech"):
        if tts_text:
            tts_engine.say(tts_text)
            tts_engine.runAndWait()
            st.success("Text converted to speech")

# Document Comparison
with tabs[5]:
    st.subheader("Document Comparison")
    doc1 = st.text_area("Enter first document")
    doc2 = st.text_area("Enter second document")
    if st.button("Compare Documents"):
        if doc1 and doc2:
            comparison = get_claude_response(f"Compare these two documents:\nDocument 1: {doc1}\nDocument 2: {doc2}")
            st.write(comparison)

# Entity Recognition
with tabs[6]:
    st.subheader("Entity Recognition")
    text_for_entities = st.text_area("Enter text for entity recognition")
    if st.button("Recognize Entities"):
        if text_for_entities:
            entities = get_claude_response(f"Identify entities in the following text:\n{text_for_entities}")
            st.write(entities)

# Topic Classification
with tabs[7]:
    st.subheader("Topic Classification")
    text_for_classification = st.text_area("Enter text to classify")
    if st.button("Classify Text"):
        if text_for_classification:
            classification = get_claude_response(f"Classify the following text into topics:\n{text_for_classification}")
            st.write(classification)

# Additional Ideas:
# - Add language translation feature
# - Add sentiment analysis
# - Integrate file upload for document summarization
# - Visualize response statistics like token usage
# - Add a text-to-speech functionality
# - Implement a document comparison tool
# - Add an entity recognition feature
# - Include a topic classification utility
