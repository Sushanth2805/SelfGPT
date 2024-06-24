import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Function to get response from Gemini API
def get_gemini_response(question):
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(question)
    return response.text  # Adjust based on actual response structure

# Set up the Streamlit page configuration
st.set_page_config(page_title="SelfGPT", page_icon="🤖", layout="centered")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar with brief introduction and model selection
st.sidebar.title("SelfGPT")
st.sidebar.info("""
    This application demonstrates the use of Gemini LLM for answering questions.
    Enter your query below and click "Ask Question" to get a response.
    Please ask questions for educational purposes.
""")

model_option = st.sidebar.selectbox(
    "Select the model", 
    options=["gemini-1.5-flash", "gemini-2.0", "gemini-3.0"]
)

# Main header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>SelfGPT</h1>", unsafe_allow_html=True)

# Input and button in columns for better layout
col1, col2 = st.columns([3, 1])

with col1:
    input_text = st.text_input("Ask your question here:", key="input")

with col2:
    submit = st.button("Ask Question")

# Display the response when the button is clicked
if submit:
    with st.spinner('Waiting for response...'):
        response = get_gemini_response(input_text)
        st.session_state.chat_history.append({"question": input_text, "answer": response})

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**Gemini:** {chat['answer']}")

# Add a footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <p>Powered by <a href="https://google.com" target="_blank">Google Generative AI</a></p>
    </div>
""", unsafe_allow_html=True)
