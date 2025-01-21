# Belto Web Server: Text Processing API

The **Belto Web Server** is a robust, open-source API designed for efficient and scalable text extraction and processing. It supports PDF and DOCX file formats, allowing developers to extract text, analyze content, and optionally include metadata such as token counts, sentence counts, and embedded images.

This API is maintained by **Belto Inc.** and licensed under its proprietary license. **API keys are required** to use the service. For inquiries, contact the Belto team at [info@beltoss.com](mailto:info@beltoss.com).

---

## Key Features

- **PDF Text Extraction**: Extract plain text and images from PDF documents.
- **DOCX Text Extraction**: Extract plain text and images from Microsoft Word (.docx) files.
- **Base64 File Support**: Process files sent as Base64-encoded strings.
- **Token and Sentence Analysis**: Get token counts, sentence counts, and reduced versions of text for meaningful insights.
- **Customizable Character Limits**: Enforce character limits during processing to optimize performance and resource usage.
- **Detailed Error Handling**: User-friendly error messages for invalid requests or unsupported file sizes.

---

## Capabilities

### Processing Limits
| **Parameter**           | **Value**                          |
|--------------------------|-------------------------------------|
| Max File Size            | 10 MB                              |
| Default Max Character Count | 1,000,000 characters            |
| Absolute Max Character Count | 2,000,000 characters          |
| Supported File Types     | PDF, DOCX                         |
| Supported Input Methods  | File URL, Base64 Encoded Files    |

### Key Endpoints
| **Endpoint**                 | **Method** | **Description**                                                                                                                                 |
|------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `/process_pdf_url`           | `POST`     | Process a PDF file provided via URL.                                                                                                           |
| `/process_docx_url`          | `POST`     | Process a DOCX file provided via URL.                                                                                                          |
| `/process_pdf_base64`        | `POST`     | Process a PDF file sent as a Base64-encoded string.                                                                                            |
| `/process_docx_base64`       | `POST`     | Process a DOCX file sent as a Base64-encoded string.                                                                                           |
| `/capabilities`              | `GET`      | Get the server's processing limits and capabilities.                                                                                           |
| `/health`                    | `GET`      | Check the server's health status.                                                                                                              |
| `/info`                      | `GET`      | Get general information about the server, including licensing, repository details, and developer contact information.                          |

---

## Installation

### Prerequisites
- Python 3.7 or later
- `pip` (Python package installer)

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
-d '{"pdf_url": "https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf"}'
```

### /process_docx
```bash
curl -X POST http://localhost:5000/process_docx \
-H "Content-Type: application/json" \
-H "API-Key: 123456789012345" \
-d '{"file_url": "https://belto.site/static_resources/file-download/Essay.docx"}'
```

## Future Enhancements

The following features and improvements are planned for future updates:

- **Base64 File Uploads**: Include ways for files to be passed as Base64 data
- **Set max upload limit**: Implement a maximum upload size and return an error if the file exceeds the limit.
- **Structure extracted text**: Format the extracted text into a string that can be directly inserted into the user content chat template.
- **PDF metadata analysis**: Extract images from PDFs or DOCX files, convert them to Base64, and include the image data in prompts.
- **NLP tools integration**: Use NLP tools to cross-reference tokens against an English dictionary and NLP models. Perform text analysis on cleaned extracted text to maintain sentiment while reducing token count.
- **Spreadsheet extraction**: Find and integrate a library for extracting tables from PDFs or DOCX files.
- **Structured responses**: Combine extracted text, tables, and images into a cohesive user content string.
- **Secure API key storage**: Use a database or locally encrypted file to securely maintain API keys.


