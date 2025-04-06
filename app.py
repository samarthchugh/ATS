from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import PyPDF2
import google.generativeai as genai
import re

# --- Configuration ---
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.set_page_config(page_title="ATS Resume Expert", page_icon=":guardsman:", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🧠 Smart ATS Resume Expert</h1>", unsafe_allow_html=True)
# st.markdown("##### Built with Streamlit & Gemini API")
st.markdown("---")

# --- Sidebar Navigation ---
st.sidebar.title("🔎 Navigation")
option = st.sidebar.radio("Choose Action", ["Resume Analysis", "Improve Resume", "ATS Match"])

# --- Functions ---
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return re.sub(r'\s+', ' ', text.strip())  # Clean up whitespace
    except Exception as e:
        return f"Error: {str(e)}"

def get_gemini_response(prompt_intro, resume_text, job_description):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt_intro, resume_text, job_description])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- Prompts ---
input_prompt1 = """You are an experienced HR manager. Analyze the following resume text and compare it to the provided job description.
Highlight:
- Strengths of the candidate in context of the job description
- Weaknesses or missing skills
- A final overall assessment: Strong/Moderate/Weak fit"""

input_prompt2 = """You are a professional career coach and resume expert.
Based on the job description and the following resume text, provide a detailed and personalized list of improvements the candidate can make to strengthen their resume.
Include suggestions such as:
- Skills to add or elaborate on
- Sections that are missing or weak
- Formatting or structural tips (if applicable)
- How to tailor resume better to this specific job"""

input_prompt3 = """You are a skilled ATS (Applicant Tracking System) scanner with deep understanding of roles like Data Scientist, Full Stack Developer,
Big Data Engineer, DevOps, and Data Analyst. Evaluate the resume text against the job description.
Respond in the following format:
1. **Percentage Match:** XX%
2. **Missing Keywords:**
3. **Final Thoughts:**"""

# --- Layout ---
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("📤 Upload & Description")
    input_text = st.text_area("Job Description:", key="input", height=250)
    uploaded_file = st.file_uploader("Upload Resume (PDF)...", type=["pdf"])
    if uploaded_file:
        st.success("PDF Uploaded Successfully!")

with col2:
    st.subheader("⚙️ Actions")
    if uploaded_file and input_text.strip():
        resume_text = extract_text_from_pdf(uploaded_file)

        with st.spinner("Analyzing with Gemini..."):
            if option == "Resume Analysis":
                response = get_gemini_response(input_prompt1, resume_text, input_text)
                st.subheader("📋 Resume Review")
                st.markdown(response, unsafe_allow_html=True)
                st.download_button("📥 Download Review", response, file_name="resume_review.txt")

            elif option == "Improve Resume":
                response = get_gemini_response(input_prompt2, resume_text, input_text)
                st.subheader("🛠 Improvement Suggestions")
                st.markdown(response, unsafe_allow_html=True)
                st.download_button("📥 Download Suggestions", response, file_name="resume_suggestions.txt")

            elif option == "ATS Match":
                response = get_gemini_response(input_prompt3, resume_text, input_text)
                st.subheader("📊 ATS Percentage Match")
                st.markdown(response, unsafe_allow_html=True)
                st.download_button("📥 Download ATS Report", response, file_name="ats_report.txt")
    else:
        st.info("Please provide both a job description and a resume.")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Made with ❤️ by Samarth Chugh, Neeraj Gupta, Shubham Kotnala | Powered by Gemini API</p>",
    unsafe_allow_html=True
)
# project done by samarth chugh, neeraj gupta, shubham kotnala