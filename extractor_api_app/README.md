# 📄 Scanned PDF Text Extractor API

This is a **FastAPI-based** project that extracts text from scanned PDFs while preserving layout using **Tesseract OCR** and **image preprocessing techniques**.

---

## 🚀 Features

✅ **Extracts text from scanned PDFs**  
✅ **Preserves layout as closely as possible**  
✅ **Uses OpenCV for image preprocessing**  
✅ **FastAPI-based for quick API deployment**  
✅ **Docker-ready for containerized deployment**  

---

## 📂 Project Structure

pdf_text_extractor/ │── main.py # FastAPI entry point │── services/ │ ├── pdf_converter.py # Convert PDF to images │ ├── ocr_processor.py # Perform OCR and text extraction │ ├── image_utils.py # Preprocess images for better OCR accuracy │── models/ │ ├── request_models.py # Request validation models │── utils/ │ ├── file_utils.py # File handling utilities │── requirements.txt # Python dependencies │── README.md # Project documentation │── .env # Environment variables (optional) │── Dockerfile # Containerization setup (optional) │── run.sh # Shell script to run the project (optional)