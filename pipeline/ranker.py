def rank_resumes(agent_results, resume_texts):
    """
    Simulate ranking by parsing the agent's output.
    In this demo, we look for lines starting with 'File:'
    and create a candidate entry.
    Returns a list of candidate dictionaries.
    """
    candidates = []
    lines = agent_results.split("\n")
    for line in lines:
        if "File:" in line:
            # Example line: "File: resumes/Alice.pdf"
            file_info = line.split("File:")[-1].strip()
            candidate = {
                "name": file_info.split("/")[-1],
                "score": 0.9,  # Placeholder score (90% match)
                "summary": "Relevant match based on skills and experience\
                      extracted from the resume."
            }
            candidates.append(candidate)
    # Sort candidates by score (highest first)
    candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
    return candidates
