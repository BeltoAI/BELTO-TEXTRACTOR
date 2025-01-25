import axios from 'axios';
import OpenAI from 'openai';

const extractApiUrl = 'http://textractor.api.beltoss.com/process_pdf_url';
const apiKeyExtract = 'API-KEY GOES HERE'; // Key for your text extraction API

const openai = new OpenAI({
  baseURL: 'http://97.90.193.213:9999/v1', // OpenAI API endpoint
  apiKey: 'API-KEY GOES HERE', // OpenAI API key
});

const requestBody = {
  file_url: 'https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf',
  reduce_tokens: false,
  include_images: true,
  max_char_count: 1000000,
};

const fetchPdfAndGenerateResponse = async () => {
  try {
    // Step 1: Fetch text data from your PDF extraction API using Axios
    const response = await axios.post(extractApiUrl, requestBody, {
      headers: {
        'Content-Type': 'application/json',
        'API-Key': apiKeyExtract,
      },
    });

    const extractedData = response.data;
    const extractedText = extractedData.text; // Extract the text from the API response

    const hardcodedUserQuery = "Can you explain the info in this document for me"

    // Step 2: Send the extracted text to the OpenAI chat completion endpoint
    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: 'You are a Belto AI.' },
        { role: 'user', content: `This is an enriched context generation scenario with text extracted from a document. start of [object Object]
          **${extractedText}**
          end of [object Object]\n\nBased on the content above, please provide a response to the user query.\n\nUser Query: ${hardcodedUserQuery}` },
      ],
    });

    // Step 3: Print the AI's response
    console.log('AI Response:', completion.choices[0].message.content);
  } catch (error) {
    console.error('Error:', error);
  }
};

// Execute the function
fetchPdfAndGenerateResponse();
