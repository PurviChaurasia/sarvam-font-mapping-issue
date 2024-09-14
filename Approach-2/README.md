## Overview

This Python script is designed to extract and compare text from PDFs using two different methods: 
1. **OCR-based extraction** using Tesseract to recognize text from PDF images.
2. **Raw text extraction** using `pdfplumber` to retrieve embedded text.

The script generates a **difference report** in HTML format that highlights discrepancies between the OCR-processed text and the raw embedded text in the PDF. This can be useful for finding unicode mapping issues present in the PDFs.

## Prerequisites

### Python Libraries

Make sure you have the following Python libraries installed:

1. **pdf2image**: To convert PDF pages into images.
   ```
   pip install pdf2image
   ```
2. **pytesseract**: For performing OCR on the images.
   ```
   pip install pytesseract
   ```
   Additionally, you need to have **Tesseract OCR** installed on your machine. Installation instructions can be found [here](https://github.com/tesseract-ocr/tesseract).
3. **pdfplumber**: To extract raw text from the PDF.
   ```
   pip install pdfplumber
   ```
4. **difflib**: This is part of Python's standard library and is used to generate an HTML report showing the differences between the raw and OCR text.

### External Dependencies

1. **Tesseract OCR**: Ensure that Tesseract is properly installed on your system. For installation:
   - On Ubuntu:
     ```
     sudo apt-get install tesseract-ocr
     ```
   - On macOS (using Homebrew):
     ```
     brew install tesseract
     ```
   - On Windows, download the installer from [here](https://github.com/tesseract-ocr/tesseract/wiki).

2. **poppler-utils**: Required for `pdf2image` to convert PDFs to images.
   - On Ubuntu:
     ```
     sudo apt-get install poppler-utils
     ```
   - On macOS:
     ```
     brew install poppler
     ```

## How the Script Works

### 1. OCR Text Extraction
The script uses `pdf2image` to convert each page of the PDF into a JPEG image. It then processes these images using Tesseract OCR to extract text from the images. The extracted text is saved in a list, with each element corresponding to one page of the PDF.

### 2. Raw Text Extraction
Using `pdfplumber`, the script extracts the embedded text directly from each page of the PDF and saves it in a list. This method works for PDFs that already have selectable text.

### 3. Generating a Difference Report
The script compares the text obtained from OCR with the raw text using Python's `difflib.HtmlDiff` module. It generates an HTML file that visually highlights the differences between the two texts for each page of the PDF.


