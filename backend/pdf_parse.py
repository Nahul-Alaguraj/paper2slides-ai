# backend/pdf_parser.py
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> dict:
    """
    Extracts text from PDF and returns basic structure.
    """
    doc = fitz.open(pdf_path)

    full_text = []
    pages = []

    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        pages.append({
            "page_number": page_num + 1,
            "text": text.strip()
        })
        full_text.append(text)

    doc.close()

    return {
        "num_pages": len(pages),
        "full_text": "\n".join(full_text),
        "pages": pages
    }
