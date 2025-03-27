from app.agents.reader_agent import extract_text_from_pdf
from app.agents.extractor_agent import extract_abstract

def process_uploaded_pdf(filepath):
    text = extract_text_from_pdf(filepath)
    abstract = extract_abstract(text)
    return {
        "abstract": abstract[:1000]  # Preview limitado
    }