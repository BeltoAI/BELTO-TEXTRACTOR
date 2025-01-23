import axios from 'axios';

const url = 'http://beltoss.com/process_pdf_url';
const apiKey = '123456789012345';

const requestBody = {
    file_url: 'https://www.gpo.gov/fdsys/pkg/FR-2019-01-31/pdf/2019-00489.pdf',
    reduce_tokens: false,
    include_images: true,
    max_char_count: 1000000
};

const processPdf = async () => {
    try {
        const response = await axios.post(url, requestBody, {
            headers: {
                'Content-Type': 'application/json',
                'API-Key': apiKey
            }
        });

        console.log('Response:', response.data);
    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
    }
};

processPdf();

