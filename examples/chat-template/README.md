# Belto API Integration Guide

This guide explains how to use the **Belto Web Server API** with JavaScript to extract text and images from documents and integrate the extracted content with OpenAI's chat completion endpoint.

## Table of Contents
1. [Overview](#overview)
2. [Setup](#setup)
3. [Files](#files)
    - [axios-test.js](#axios-testjs)
    - [node-fetch-test.js](#node-fetch-testjs)
4. [Using the API](#using-the-api)
5. [Error Handling](#error-handling)
6. [Next Steps](#next-steps)

---

## Overview

The **Belto Web Server API** supports:
- **PDF and DOCX Processing**: Extract text and images.
- **Base64 or URL File Input**: Flexibility in document input.
- **Integration with OpenAI**: Enrich extracted content using the OpenAI library.

Developers can use either `axios` or `node-fetch` to interact with the API.

---

## Setup

### Prerequisites
1. **Node.js** installed on your system.
2. Install the required dependencies:
   ```bash
   npm install axios node-fetch openai
   ```
3. Ensure you have a valid **API Key** for the Belto Web Server.

---

## Files

### 1. **axios-test.js**
This file demonstrates using **Axios** to:
1. Fetch text and images from a PDF document via the Belto API.
2. Pass the extracted text into OpenAI's chat completion endpoint for processing.

#### Key Highlights:
- Axios is used for HTTP requests.
- OpenAI library is used to integrate with OpenAI's chat endpoint.

### 2. **node-fetch-test.js**
This file demonstrates the same functionality as `axios-test.js` but uses **node-fetch** for HTTP requests.

#### Key Highlights:
- Uses `fetch` to interact with the Belto API.
- Integrates OpenAI chat completion endpoint using the OpenAI library.

---

## Using the API

### **1. Process a PDF Document**
Both files include code to:
1. Extract text and images from a PDF using the Belto API.
2. Send the extracted text to OpenAI's chat model for further processing.

#### Example (from `axios-test.js`):
```javascript
const response = await axios.post(extractApiUrl, requestBody, {
  headers: {
    'Content-Type': 'application/json',
    'API-Key': apiKeyExtract,
  },
});

const extractedText = response.data.text; // Extracted text from the PDF.
```

#### Example (from `node-fetch-test.js`):
```javascript
const response = await fetch(extractApiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'API-Key': apiKeyExtract,
  },
  body: JSON.stringify(requestBody),
});

const extractedData = await response.json();
const extractedText = extractedData.text; // Extracted text from the PDF.
```

---

### **2. Send Extracted Text to OpenAI Chat Completion**

Both files follow this consistent structure:
```javascript
const completion = await openai.chat.completions.create({
  model: 'gpt-3.5-turbo',
  messages: [
    { role: 'system', content: 'You are a Belto AI.' },
    { role: 'user', content: `This is an enriched context generation scenario with text extracted from a document. start of [object Object]
      **${extractedText}**
      end of [object Object]\n\nBased on the content above, please provide a response to the user query.\n\nUser Query: ${hardcodedUserQuery}` },
  ],
});
```

The extracted text (`extractedText`) is formatted and sent to the OpenAI endpoint.

---

## Error Handling

### Common Errors:
1. **Invalid API Key**:
   ```json
   { "error": "Invalid or missing API key" }
   ```

2. **Character Limit Exceeded**:
   ```json
   { "error": "Text exceeds maximum character limit of 1000000." }
   ```

3. **Unsupported File Size**:
   ```json
   { "error": "File size exceeds maximum limit of 10 MB." }
   ```

### Solution:
- Ensure the API Key is correct.
- Reduce the document size or character count using the `max_char_count` parameter.

---

## Next Steps

1. **Integration**:
   - Replace the sample `file_url` with dynamic URLs or user-provided input.
   - Handle responses dynamically to suit your application's requirements.

2. **Custom Enhancements**:
   - Use additional OpenAI features like summarization, question answering, or content classification on the extracted text.

3. **API Expansion**:
   - Explore other endpoints (e.g., `/process_docx_base64`) for DOCX support and Base64 input.

---

### Contact
For further questions or API Key requests, contact **Belto Inc.** at [info@beltoss.com](mailto:info@beltoss.com).

---

