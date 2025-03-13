import os
import logging
import traceback
from fastapi import FastAPI, File, UploadFile, HTTPException
from services.pdf_converter import convert_pdf_to_images
from services.ocr_processor import extract_text_from_images
from utils.file_utils import save_uploaded_file

# Initialize FastAPI
app = FastAPI(title="Scanned PDF Text Extractor API")

# Setup Logging
logging.basicConfig(
    filename="error.log",  # Save logs to a file
    filemode="a",  # Append logs instead of overwriting
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.ERROR
)

# Create Upload Directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    """Extract text from a scanned PDF while preserving layout."""
    pdf_path = None  # Initialize variable for later cleanup

    try:
        # Save uploaded file
        pdf_path = save_uploaded_file(file, UPLOAD_DIR)
        logging.info(f"File saved at: {pdf_path}")

        # Convert PDF to images
        images = convert_pdf_to_images(pdf_path)
        logging.info(f"Converted PDF to {len(images)} images")

        # Extract text using OCR
        extracted_text = extract_text_from_images(images)
        logging.info("OCR extraction successful")

        return {"extracted_text": extracted_text}

    except Exception as e:
        error_message = f"❌ Error processing PDF: {str(e)}"
        logging.error(error_message)
        logging.error(traceback.format_exc())  # Log full traceback

        raise HTTPException(status_code=500, detail=error_message)

    finally:
        # Delete uploaded PDF after processing
        if pdf_path and os.path.exists(pdf_path):
            try:
                os.remove(pdf_path)
                logging.info(f"Deleted uploaded file: {pdf_path}")
            except Exception as e:
                logging.error(f"❌ Error deleting file {pdf_path}: {str(e)}")
