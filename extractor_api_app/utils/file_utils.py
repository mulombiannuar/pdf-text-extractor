import shutil
import os
from fastapi import UploadFile

def save_uploaded_file(uploaded_file: UploadFile, upload_dir: str) -> str:
    """Save uploaded file to a directory and return its path."""
    file_path = os.path.join(upload_dir, uploaded_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return file_path
