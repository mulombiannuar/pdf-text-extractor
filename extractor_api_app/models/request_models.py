from pydantic import BaseModel

class PDFExtractionResponse(BaseModel):
    extracted_text: str
