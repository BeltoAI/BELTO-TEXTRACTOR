# Document Text Extraction and Analysis API

This project is a Flask-based API that allows users to extract and analyze text from PDF and DOCX files. It uses various libraries including spaCy for natural language processing, PyMuPDF for PDF text extraction, and python-docx for DOCX file handling.

## Features

- Extract text from PDF files using PyMuPDF.
- Extract text from DOCX files using python-docx.
- Analyze and tokenize text using spaCy.
- Count sentences and tokens in the extracted text.
- Secure API access with API keys.

## Requirements

To run this project, you need to install the required libraries. You can do so by running:

```bash
python3 -m venv venv
```

## Linux / MacOS
```bash
source venv/bin/activate
```

## Windows
```bash
.\venv\Scripts\activate
```

## Install Python Packages














## START WEB SERVER
```bash
python3 final-server.py
```

```bash
curl -X POST http://localhost:5000/process_pdf \
     -H "Content-Type: application/json" \
     -H "API-Key: 123456789012345" \
     -d '{"pdf_url": "[https://example.com/somefile.pdf](https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf)"}'
```

```bash
curl -X POST http://localhost:5000/process_docx \
     -H "Content-Type: application/json" \
     -H "API-Key: 123456789012345" \
     -d '{"file_url": "[https://example.com/somefile.docx](https://belto.site/static_resources/file-download/Essay.docx)"}'
```
