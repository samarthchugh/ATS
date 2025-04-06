# 🤖 ATS Resume Expert

A smart and interactive ATS (Applicant Tracking System) Resume Analyzer built with **Streamlit** and powered by **Google Gemini API**. This tool helps candidates improve their resumes by analyzing them against specific job descriptions.

---

## Poster
[Poster](images\Poster.png)
[UI](images\UI.png)

## 📂 Project Structure

<pre lang="markdown"> ```bash ats-resume-expert/ 
├── .streamlit/ 
│ └── config.toml # Theme & layout settings 
├── .env # API key (used locally) 
├── .gitignore # Ignored files for Git 
├── app.py # Main Streamlit app 
├── requirements.txt # Required Python packages 
└── README.md # You're reading it! ``` </pre>


---

## 🚀 Features

- 📄 Upload your resume in PDF format
- 🧠 Analyze resume against a job description
- ✍️ Get detailed improvement suggestions
- ✅ ATS Percentage match with missing keywords
- 🤝 Gemini-powered response tailored by prompt roles (HR, Career Coach, ATS)

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI API**: Google Gemini (via `google-generativeai`)
- **PDF Parser**: PyPDF2
- **Secrets Manager**: `dotenv` (local) / Streamlit secrets (cloud)

---

## 🔧 Installation
<pre lang='markdown'>```bash
### 1. Clone the repository

git clone https://github.com/your-username/ats-resume-expert.git
cd ats-resume-expert

### 2. Install the dependencies
pip install -r requirements.txt

### 3. Add your Google Gemini API key to a .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

### 4. Run the Streamlit app
streamlit run app.py
```</pre>

## ⚙️ Configuration
You can customize the theme via **.streamlit/config.toml**
<pre lang='markdown'>
```bash
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#F5F5F5"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#262730"
font = "sans serif"
```
</pre>

## 📦 Requirements
Dependencies listed in **requirements.txt**:
<pre lang='markdown'>
```bash
streamlit>=1.30.0
python-dotenv>=1.0.0
PyPDF2>=3.0.1
google-generativeai>=0.3.2
```
</pre>

## 🔗 Live Demo
<!--  -->

## 📄 License
MIT License. Feel free to use, share, and contribute.

## 🙌 Acknowledgements
[Google Gemini API](https://aistudio.google.com/app/apikey)
[Streamlit](https://streamlit.io/)

## 📬 Contact
Made with ❤️ by [Samarth Chugh](www.linkedin.com/in/-samarthchugh)

### ⭐ Don’t forget to star this repo if you found it helpful!



