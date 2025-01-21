# Usage

## 1. Processing a PDF via URL

### Request:
```bash
curl -X POST http://beltoss.com/process_pdf_url \\
-H "Content-Type: application/json" \\
-H "API-Key: 123456789012345" \\
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
curl -X POST http://beltoss.com/process_docx_base64 \\
-H "Content-Type: application/json" \\
-H "API-Key: 123456789012345" \\
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
