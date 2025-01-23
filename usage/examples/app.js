import fetch from 'node-fetch';

const url = 'http://beltoss.com/process_pdf_url';
const apiKey = '123456789012345';

const requestBody = {
    file_url: 'https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf',
    reduce_tokens: false,
    include_images: true,
    max_char_count: 1000000
};

const fetchPdfData = async () => {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'API-Key': apiKey
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Response:', data);
    } catch (error) {
        console.error('Error:', error);
    }
};

fetchPdfData();

