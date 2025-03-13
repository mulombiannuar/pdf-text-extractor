import streamlit as st
import requests
import tempfile
import base64
from pdf2image import convert_from_path

# FastAPI URL
API_URL = "http://localhost:8000/extract_text"

# Streamlit App Title
st.set_page_config(page_title="Scanned PDF Text Extractor", layout="wide")

# Sidebar Section
with st.sidebar:
    st.title("📂 Upload PDF")
    uploaded_file = st.file_uploader("Choose a scanned PDF", type=["pdf"])
    extract_button = st.button("Extract Text")

# Function to send file to FastAPI
def extract_text_from_api(pdf_path):
    with open(pdf_path, "rb") as f:
        files = {"file": f}
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        return response.json().get("extracted_text", "No text found")
    else:
        return f"❌ Error: {response.status_code}, {response.text}"

# Function to display PDF in Streamlit
def display_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# Main Body - Two Column Layout
if uploaded_file and extract_button:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    col1, col2 = st.columns(2)

    # Column 1: Show Embedded PDF
    with col1:
        st.subheader("📄 Uploaded PDF")
        display_pdf(pdf_path)

    # Column 2: Extracted Text
    with col2:
        st.subheader("📝 Extracted Text")
        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_api(pdf_path)
            st.text_area("Extracted Text", extracted_text, height=500)
            



