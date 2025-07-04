import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit GUI Setup
st.set_page_config(page_title="Startup Idea Generator", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>AI Startup Idea Generator</h1>
    <p style='text-align: center;'>Powered by Gemini API | Build your next big thing</p>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4327/4327320.png", width=100)
st.sidebar.header("Configure Input")

# Input: Industry
industry = st.sidebar.selectbox(
    "Choose an Industry:",
    ["Education", "Fashion", "Health"]
)

# Input: Language
language = st.sidebar.selectbox(
    "Choose Output Language:",
    ["English", "Urdu", "Spanish", "German"]
)

# Button
if st.sidebar.button("Generate Ideas"):
    with st.spinner("Generating innovative ideas..."):

        # Gemini Prompt
        prompt = f"""
You are a successful business startup expert.
Generate 5 unique startup ideas in the {industry} industry.
Each idea must include:
1. Idea Name
2. Problem it solves
3. The Solution
4. Target Users
5. Why it's innovative

Write everything in {language}.
Be concise, clear, and professional.
Use bullet points or clear formatting.
"""

        # Call Gemini
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        st.markdown("---")
        st.subheader(f" 5 Startup Ideas in {industry} Industry ({language})")
        st.markdown(response.text)

