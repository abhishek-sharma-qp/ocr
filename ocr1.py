import os
from ollama_ocr import OCRProcessor
import streamlit as st

# Set the path to Poppler
os.environ["POPPLER_PATH"] = "C:/poppler/Library/bin"  # Adjust this path to where you installed Poppler

# Initialize OCR processor
ocr = OCRProcessor(model_name='llama3.2-vision:11b')  # Ensure this model name is correct and available

# Streamlit UI
st.title("OCR Text Extraction")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the uploaded file
    result = ocr.process_image(
        image_path="temp_file",  # Path to the temporary file
        format_type="markdown"  # Options: markdown, text, json, structured, key_value
    )
    
    # Display the result
    st.markdown(result)