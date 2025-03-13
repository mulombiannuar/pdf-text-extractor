from fastapi import FastAPI, File, UploadFile
from services.pdf_converter import convert_pdf_to_images
from services.ocr_processor import extract_text_from_images
from utils.file_utils import save_uploaded_file
import os

app = FastAPI(title="Scanned PDF Text Extractor API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the upload directory exists

@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    """Extract text from a scanned PDF while preserving layout."""
    pdf_path = save_uploaded_file(file, UPLOAD_DIR)
    images = convert_pdf_to_images(pdf_path)
    extracted_text = extract_text_from_images(images)
    return {"extracted_text": extracted_text}
