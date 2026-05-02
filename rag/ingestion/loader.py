from pathlib import Path
from typing import List
import re
from langchain_community.document_loaders.pdf import PyPDFLoader


def clean_text(text: str) -> str:
    """
    Light cleaning to remove PDF artifacts without destroying meaning.
    """
    # Remove bullet symbols and weird characters
    text = text.replace("●", " ")
    
    # Remove excessive newlines
    text = re.sub(r"\n+", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Optional: remove common footer/header noise
    text = re.sub(r"Contents\s+highwaycodeuk\.co\.uk\s+\d+", "", text)

    return text.strip()


def load_pdfs(data_path: str) -> List:
    documents = []

    pdf_files = list(Path(data_path).glob("*.pdf"))

    if not pdf_files:
        raise ValueError(f"No PDF files found in {data_path}")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        # Clean each page
        for doc in docs:
            doc.page_content = clean_text(doc.page_content)
            doc.metadata["source"] = str(pdf.name)

        documents.extend(docs)

    print(f"📄 Loaded {len(documents)} pages from {len(pdf_files)} PDFs")

    return documents