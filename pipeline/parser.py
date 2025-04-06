# pipeline/parser.py
import warnings
import docx

# Suppress specific warnings if needed
warnings.filterwarnings(
    "ignore", message="CropBox missing from /Page, defaulting to MediaBox")


def parse_pdf_with_pypdf2(file_path):
    """
    Parse a PDF file using PyPDF2 and return its text content.
    """
    text = ""
    try:
        from PyPDF2 import PdfReader
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            # Iterate over each page and extract text
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        print(f"Error parsing PDF {file_path} with PyPDF2: {e}")
    return text


def parse_resume(file_path):
    """
    Parse a resume file (PDF, DOCX, TXT) and return its text content.
    Uses PyPDF2 for PDF parsing.
    """
    text = ""
    if file_path.lower().endswith('.pdf'):
        text = parse_pdf_with_pypdf2(file_path)
    elif file_path.lower().endswith(('.docx', '.doc')):
        try:
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"Error parsing DOCX {file_path}: {e}")
            text = ""
    elif file_path.lower().endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading TXT {file_path}: {e}")
            text = ""
    else:
        print(f"Unsupported file type: {file_path}")
    return text
