from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, dpi=300):
    """Convert PDF pages into high-resolution images."""
    return convert_from_path(pdf_path, dpi=dpi)
