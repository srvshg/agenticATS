# agenticATS
# ATS Resume Shortlisting & Screening Workflow

This project implements an AI-powered ATS system that:
- Retrieves resumes from Google Drive (using a public link),
- Parses PDF, DOCX, and TXT resumes,
- Uses NLP (embeddings and an LLM agent) to search and rank resumes based on a job description,
- Presents a user-friendly dashboard built with Streamlit.

## Setup

1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Application:
   ```bash
   streamlit run app.py
   ```