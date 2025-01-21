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

# Usage

## 1. Processing a PDF via URL

### Request:
```bash
curl -X POST http://localhost:5000/process_pdf_url \\
-H "Content-Type: application/json" \\
-H "API-Key: YOUR_API_KEY" \\
-d '{
    "file_url": "https://example.com/sample.pdf",
    "reduce_tokens": false,
    "include_images": true,
    "max_char_count": 1000000
}'
```

Response:

```bash
{
    "text": "Extracted text from the PDF.",
    "token_count": 1200,
    "sentence_count": 150,
    "images": [],
    "process_time_seconds": 2.3,
    "file_size_bytes": 1048576
}
```


## 2. Processing a DOCX via Base64
Request:

```bash
curl -X POST http://localhost:5000/process_docx_base64 \\
-H "Content-Type: application/json" \\
-H "API-Key: YOUR_API_KEY" \\
-d '{
    "file_base64": "BASE64_ENCODED_STRING",
    "reduce_tokens": true,
    "include_images": false,
    "max_char_count": 1000000
}'
```

Response:

```bash
{
    "text": "Extracted text from the DOCX.",
    "token_count": 2500,
    "sentence_count": 300,
    "reduced_text": "Summarized or filtered text based on input criteria.",
    "images": [],
    "process_time_seconds": 1.9,
    "file_size_bytes": 524288
}
```


# Error Handling

The server provides detailed error messages for invalid requests or exceeding processing limits.

## Example Errors

### Invalid API Key:
```json
{
    "error": "Invalid or missing API key"
}
```
### Character Limit Exceeded:

```json
{
    "error": "Text exceeds maximum character limit of 1000000. Reduce the file size or content."
}
```
### Malformed JSON:

```json
{
    "error": "The browser (or proxy) sent a request that this server could not understand."
}
```

# Limitations

While the Belto Web Server is a robust and efficient text processing API, it has some limitations that users should be aware of:
## 1. File Size Limitations

    Maximum file size: 10 MB
        Larger files will be rejected. Users must split large files into smaller parts before processing.

## 2. Character Limitations

    Default maximum character count: 1,000,000 characters.
    Absolute maximum character count: 2,000,000 characters.
        Exceeding this limit will result in errors. Text-heavy PDFs or DOCX files can easily hit these limits.

## 3. Processing Time

    For very large files, the server may experience increased processing times due to the computational overhead of token and sentence parsing.

## 4. Image Processing

    Image extraction is supported but limited to embedded images in PDF or DOCX files.
    It does not perform OCR (optical character recognition) on image-only PDFs.

5. Base64 Payload Size

    Large Base64-encoded files can exceed the maximum request payload size. This limit depends on the Flask server configuration but defaults to 16 MB.

# Potential Ways to Break It

While we have implemented several safeguards, here are scenarios where the server could run into issues:

    ## Submitting Files Beyond Limits
        Sending files larger than 10 MB or exceeding 2,000,000 characters will result in errors. However, users who bypass these checks by misconfiguring the server may cause excessive memory consumption or crashes.

    ##Sending Invalid Base64 Strings
        Submitting malformed or incomplete Base64 strings will cause decoding errors, leading to a 400 Bad Request.

    Overloading the Server
        Sending multiple large requests simultaneously can overwhelm the server, especially with limited resources.

    Improper API Key Management
        Using invalid or missing API keys will block access, but if the server is misconfigured to skip validation, unauthorized users could potentially abuse the service.

    Bypassing Character Limits
        If a custom max_char_count above the hardcoded limit (2,000,000) is allowed due to server misconfiguration, processing may cause memory exhaustion or delays.

    Sending Corrupt Files
        Submitting corrupt PDF or DOCX files could lead to exceptions in the extraction libraries (e.g., PyMuPDF or python-docx).

Mitigation Strategies

    Input Validation:
        Ensure all files meet size, format, and character count limits before submitting.
    Rate Limiting:
        Prevent server overload by limiting the number of concurrent requests.
    Improved Error Handling:
        Implement logging and fail-safe mechanisms for invalid Base64 strings or corrupt files.
    Testing and Hardening:
        Continuously test the server against edge cases, malformed inputs, and high traffic.























# Developer Information

    Developers: Belto Developers Team
    Organization: Belto Inc.
    Contact: info@beltoss.com
    Repository: Belto Textractor GitHub

# License

This API is licensed under Belto Inc. All Rights Reserved.

API keys are required for usage.
To request an API key, contact us at info@beltoss.com.





# Future Enhancements

The following features and improvements are planned for future updates:

- **Base64 File Uploads**: Include ways for files to be passed as Base64 data
- **Set max upload limit**: Implement a maximum upload size and return an error if the file exceeds the limit.
- **Structure extracted text**: Format the extracted text into a string that can be directly inserted into the user content chat template.
- **PDF metadata analysis**: Extract images from PDFs or DOCX files, convert them to Base64, and include the image data in prompts.
- **NLP tools integration**: Use NLP tools to cross-reference tokens against an English dictionary and NLP models. Perform text analysis on cleaned extracted text to maintain sentiment while reducing token count.
- **Spreadsheet extraction**: Find and integrate a library for extracting tables from PDFs or DOCX files.
- **Structured responses**: Combine extracted text, tables, and images into a cohesive user content string.
- **Secure API key storage**: Use a database or locally encrypted file to securely maintain API keys.


