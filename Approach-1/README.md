## Overview
This Python script automates the process of converting PDF files in the current directory into PNG images, applying OCR (Optical Character Recognition) to extract text, and merging the resulting OCR-processed pages back into a single PDF. The script is designed to handle multiple PDF files and uses the following technologies:
- **ImageMagick** for PDF to PNG conversion.
- **Tesseract OCR** for extracting text from images.
- **PyPDF2** for merging multiple PDF pages.

## Prerequisites

1. **Python 3.x**: Make sure Python is installed on your system.
2. **ImageMagick**: Install ImageMagick, which is used to convert PDFs to images. You can install it by running:
   ```
   sudo apt-get install imagemagick
   ```
3. **Tesseract OCR**: Install Tesseract for OCR conversion. You can install Tesseract using:
   ```
   sudo apt-get install tesseract-ocr
   ```
   Also, make sure to install the Hindi language pack:
   ```
   sudo apt-get install tesseract-ocr-hin
   ```
4. **PyPDF2**: Install the Python package PyPDF2 to handle PDF merging. You can install it using:
   ```
   pip install PyPDF2
   ```

## Script Workflow

1. **Identify Files**: The script lists all the files in the current working directory and filters out non-PDF files.
2. **Epoch Timestamp**: Generates a folder name based on the current time in epoch format and the original PDF file's name.
3. **PDF to PNG Conversion**: 
   - The script runs an ImageMagick command to convert each PDF page into PNG images.
   - Each converted image is saved into the newly created folder.
4. **OCR on PNG Images**: 
   - The script applies Tesseract OCR to the PNG images, specifically using the Hindi (`hin`) language model.
   - OCR-processed images are saved as PDFs in the same folder.
5. **PDF Merging**: 
   - After OCR, the script merges all the OCR-generated PDFs into a single combined PDF file.
6. **Cleanup**: Merged PDFs are stored with the suffix `-ocr-combined.pdf`.
7. To change the language in of the pdf to English, just remove the -l tag in the tesseract command.

## How to Use

1. Place the script in the same directory as the PDF files you want to process.
2. Run the script with:
   ```bash
   python script_name.py
   ```
3. The script will:
   - Convert each PDF in the directory into PNG images.
   - Apply OCR on each image.
   - Merge the OCR'd pages into a single PDF file with the suffix `-ocr-combined.pdf`.


## Dependencies

- Python 3.x
- PyPDF2
- ImageMagick
- Tesseract OCR



