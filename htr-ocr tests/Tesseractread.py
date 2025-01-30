import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Verify that Tesseract is recognized
if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
    print(f"Error: Tesseract executable not found at '{pytesseract.pytesseract.tesseract_cmd}'")
else:
    print("Tesseract executable found.")

# Path to the PDF file
pdf_path = 'C:/Users/Frdob/Documents/Scanner/Scan2025-01-09_174247.pdf'

# Check if the PDF file exists
if not os.path.exists(pdf_path):
    print(f"Error: The file '{pdf_path}' does not exist.")
else:
    # Convert PDF to images
    try:
        images = convert_from_path(pdf_path)
        print("PDF converted to images successfully.")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")

    # Perform OCR on each image
    extracted_text = ""
    for i, image in enumerate(images):
        try:
            # Specify the language and configuration for Tesseract
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(image, config=custom_config)
            extracted_text += f"Page {i+1}:\n{text}\n"
            print(f"OCR performed successfully on page {i+1}.")
        except Exception as e:
            print(f"Error performing OCR on page {i+1}: {e}")

    # Print the extracted text
    print("Extracted text:")
    print(extracted_text)