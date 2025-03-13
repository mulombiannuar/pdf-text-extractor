import pytesseract
from services.image_utils import preprocess_image

def extract_text_from_images(images):
    """Extract text from images using OCR, preserving structure."""
    extracted_texts = []
    for img in images:
        processed_img = preprocess_image(img)
        text = pytesseract.image_to_string(processed_img, config="--psm 6")
        extracted_texts.append(text)
    return "\n\n".join(extracted_texts)  # Preserve page order
