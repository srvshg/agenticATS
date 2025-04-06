# app.py
import streamlit as st
from pipeline import drive_io, parser, nlp, agent, ranker


def main():
    st.set_page_config(page_title="ATS Resume Shortlisting", layout="wide")
    st.title("ATS Resume Shortlisting & Screening Workflow")
    st.write("Enter the job description or requirements below:")

    # User input for job description
    job_description = st.text_area("Job Description", height=200)

    if st.button("Shortlist Resumes"):
        if not job_description.strip():
            st.error("Please enter a job description.")
            return

        # Step 1: Fetch resumes from Google Drive
        with st.spinner("Fetching resumes from Google Drive..."):
            resume_files = drive_io.fetch_resumes_from_drive()
        st.success(f"Fetched {len(resume_files)} resumes.")

        # Step 2: Parse each resume to extract text content
        with st.spinner("Parsing resumes..."):
            resume_texts = {}
            for file in resume_files:
                text = parser.parse_resume(file)
                if text:
                    resume_texts[file] = text
        st.success("Parsing complete.")

        # Step 3: Build the vector index using NLP embeddings
        with st.spinner("Generating embeddings and building index..."):
            vector_store = nlp.build_vector_index(resume_texts)
        st.success("Embeddings and index built.")

        # Step 4: Run the LLM agent to perform a search over resumes
        with st.spinner("Running LLM Agent for candidate search..."):
            agent_results = agent.run_agent(job_description, vector_store)
        st.success("Agent completed search.")

        # Step 5: Rank resumes based on agent output and other criteria
        with st.spinner("Ranking resumes..."):
            ranked_results = ranker.rank_resumes(agent_results, resume_texts)
        st.success("Ranking complete.")

        # Step 6: Display results on the dashboard
        st.header("Top Matching Candidates")
        for candidate in ranked_results:
            st.subheader(
                f"{candidate['name']} - {candidate['score']*100:.1f}% match")
            st.write(candidate['summary'])
            st.markdown("---")


if __name__ == "__main__":
    main()
