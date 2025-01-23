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

### **Why This Is Important**
The `{ role: 'user', content: ... }` section is a key technical element of the integration because it defines the exact format in which the user query and extracted text are passed into OpenAI's chat completion endpoint. Below is a breakdown of its technical significance:

1. **Embedding Extracted Text**:
   - The extracted text from the document (`extractedText`) is embedded within the `content` field. This ensures that the AI has full access to the context needed to process the user query accurately.
   - The `start of [object Object]` and `end of [object Object]` markers act as delimiters, ensuring the extracted text is clearly separated from any additional instructions or metadata.

2. **Dynamic Query Insertion**:
   - The `hardcodedUserQuery` is dynamically inserted into the `content` field, making it easy to replace with real-time user input. This allows developers to create interactive systems that adapt to user-specific queries without hardcoding responses.

3. **Maintaining Input Structure**:
   - The consistent structure of this field ensures OpenAI's models receive well-organized and interpretable input. For example, using clear delimiters (`start of` and `end of`) helps the AI distinguish between the extracted document content and instructions.

4. **Customizable Contextual Instructions**:
   - Developers can enhance the `content` field by adding context-specific instructions. For example, phrases like "Based on the content above, provide a response to the user query" direct the AI's attention to both the document's content and the user's needs.

5. **Optimized for OpenAI Models**:
   - By combining the extracted text with the user query in a single `content` field, the input aligns perfectly with OpenAI's expectation for chat completions. This approach minimizes token usage while maximizing context delivery.

6. **Scalability Across Use Cases**:
   - This structure is flexible enough to handle multiple applications, such as summarization, question answering, or document analysis. Developers can reuse the same template for different scenarios by simply adjusting the query or the surrounding instructions.

### Example Structure Recap:
```javascript
const completion = await openai.chat.completions.create({
  model: 'gpt-3.5-turbo',
  messages: [
    { role: 'system', content: 'You are a Belto AI.' },
    { role: 'user', content: `This is an enriched context generation scenario with text extracted from a document. start of [object Object]
      **${extractedText}**
      end of [object Object]

Based on the content above, please provide a response to the user query.

User Query: ${hardcodedUserQuery}` },
  ],
});
```
This structure is crucial for achieving consistent and meaningful interactions with OpenAI's models, ensuring developers can leverage the API effectively in their applications.
The `{ role: 'user', content: ... }` section is especially critical because it defines how the user query (`hardcodedUserQuery`) and extracted document text (`extractedText`) are passed into the chat template. This process is the backbone of how the Belto API ensures rich and contextual interaction with OpenAI's chat models.

- **Contextual Relevance**: By embedding the extracted document text into the chat input, the AI has the necessary context to understand and respond to the user query meaningfully. The AI can analyze the document text alongside the user query to provide accurate and relevant responses.

- **Dynamic Query Handling**: The `hardcodedUserQuery` parameter can easily be replaced with real-time user input, making the system highly interactive. This flexibility allows developers to adapt the template for various use cases, from document summarization to Q&A systems.

- **Enhanced Customization**: Developers can include additional instructions or metadata in the `content` field, enabling the AI to process the input in a specific way. For example, you can add instructions to prioritize certain parts of the document or respond in a specific tone.

- **Streamlined Workflow**: The consistent structure of the `{ role: 'user', content: ... }` section ensures seamless integration into existing pipelines. This reduces complexity for developers and ensures the input is always structured correctly for OpenAI's models.

- **Scalability**: By leveraging this template, developers can handle various document processing tasks—such as summarization, analysis, or extraction—without needing to modify the underlying structure of the interaction, making it scalable for different applications and industries.
The `{ role: 'user', content: ... }` section is especially critical because it defines how the user query (`hardcodedUserQuery`) and extracted document text (`extractedText`) are passed into the chat template. This format ensures:
- **Contextual Relevance**: The extracted document text is included in the conversation, providing context for the AI to process the user query effectively.
- **Flexibility**: Developers can dynamically replace `hardcodedUserQuery` with user-provided queries, enabling real-time interaction.
- **Rich Input**: The format allows for detailed instructions and content to be passed into OpenAI for enriched responses.

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

