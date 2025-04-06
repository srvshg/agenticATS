from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI
import config


def resume_search_tool(query, vector_store):
    """
    Searches the resume vector store for the given query.
    Returns a summary string of top matching resumes.
    """
    results = vector_store.similarity_search(query, k=3)
    summary = ""
    for doc in results:
        source = doc.metadata.get("source", "Unknown")
        snippet = doc.page_content[:100].replace("\n", " ")
        summary += f"File: {source}\nSnippet: {snippet}...\n\n"
    return summary


def run_agent(job_description, vector_store):
    """
    Initialize and run an LLM agent using a resume search tool.
    Returns the agent's output.
    """
    # Define the tool function for resume search
    def tool_func(query):
        return resume_search_tool(query, vector_store)

    search_tool = Tool(
        name="ResumeSearch",
        func=tool_func,
        description="Search the resume database for relevant\
              candidate information based on a query."
    )

    # Initialize the LLM (using OpenAI GPT)
    llm = OpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
    agent = initialize_agent(
        [search_tool], llm, agent="zero-shot-react-description", verbose=True)

    # Prepare the input prompt for the agent
    agent_input = (
        f"Given the following job description:\n{job_description}\n\n"
        "Search the resume database using the tool and provide"
        "a summary of the most relevant candidates "
        "and why they match the requirements."
    )
    result = agent.run(agent_input)
    return result
