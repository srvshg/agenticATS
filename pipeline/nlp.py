from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
import config


def build_vector_index(resume_texts):
    """
    Build a FAISS vector store index from resume texts.
    resume_texts: dict where key = file path and value = text.
    """
    documents = []
    for file_path, text in resume_texts.items():
        doc = Document(page_content=text, metadata={"source": file_path})
        documents.append(doc)

    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
