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

### Create Python Virtual Environment
```bash
python3 -m venv venv
```
### Activate Virtual Environment
Linux / MacOS
```bash
source venv/bin/activate
```
Windows
```bash
.\venv\Scripts\activate
```

### Install Python Packages
```bash
pip3 install -r requirements.txt
```

### Download spaCy NLP model
```bash
python -m spacy download en_core_web_sm
```


### START WEB SERVER
```bash
python3 final-server.py
```
##

### Testing with curl

### /process_pdf 
```bash
curl -X POST http://localhost:5000/process_pdf \
     -H "Content-Type: application/json" \
     -H "API-Key: 123456789012345" \
     -d '{"pdf_url": "[https://example.com/somefile.pdf](https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf)"}'
```

### /process_docx
```bash
curl -X POST http://localhost:5000/process_docx \
     -H "Content-Type: application/json" \
     -H "API-Key: 123456789012345" \
     -d '{"file_url": "[https://example.com/somefile.docx](https://belto.site/static_resources/file-download/Essay.docx)"}'
```

## Future Enhancements

The following features and improvements are planned for future updates:

- **Set max upload limit**: Implement a maximum upload size and return an error if the file exceeds the limit.
- **Structure extracted text**: Format the extracted text into a string that can be directly inserted into the user content chat template.
- **PDF metadata analysis**: Extract images from PDFs or DOCX files, convert them to Base64, and include the image data in prompts.
- **NLP tools integration**: Use NLP tools to cross-reference tokens against an English dictionary and NLP models. Perform text analysis on cleaned extracted text to maintain sentiment while reducing token count.
- **Spreadsheet extraction**: Find and integrate a library for extracting tables from PDFs or DOCX files.
- **Structured responses**: Combine extracted text, tables, and images into a cohesive user content string.
- **Secure API key storage**: Use a database or locally encrypted file to securely maintain API keys.


