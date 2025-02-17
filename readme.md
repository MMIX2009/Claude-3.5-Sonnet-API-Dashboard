
# Claude 3.5 Streamlit Web App

This Streamlit web application integrates the Claude 3.5 Sonnet API by Anthropic to showcase various natural language processing capabilities. The app is divided into several sections, each demonstrating a different functionality powered by Claude's language model.

## Features

1. **Text Summarization**: 
   - Users can input text and receive a concise summary.

2. **Code Review**: 
   - Submit a code snippet to receive feedback on potential bugs, performance improvements, and best practices.

3. **Interactive Chat**: 
   - Engage in a dynamic conversation with Claude AI, maintaining context across messages.

4. **Custom Prompt**: 
   - Send any custom prompt to Claude and receive a response.

5. **Text-to-Speech**: 
   - Convert text into spoken words using a local text-to-speech engine.

6. **Document Comparison**: 
   - Compare two documents to identify similarities and differences.

7. **Entity Recognition**: 
   - Extract named entities (e.g., people, organizations, locations) from text.

8. **Topic Classification**: 
   - Analyze text to determine its primary topics.

## Technical Details

- Built using Python and Streamlit.
- Utilizes the Anthropic API for Claude 3.5 Sonnet interactions.
- Implements error handling, dynamic conversation state management, and adjustable parameters via the sidebar.

## Usage Instructions

1. Run the application using Streamlit: `streamlit run app.py`
2. Configure the Anthropic API key either as an environment variable or hardcoded in the source code.
3. Interact with various functionalities via the provided UI.

## Future Enhancements

- Add language translation and sentiment analysis.
- Integrate file uploads for document processing.
- Visualize response statistics like token usage.

---

*Developed as a demonstration of the capabilities of Claude 3.5 Sonnet within a Streamlit interface.*
