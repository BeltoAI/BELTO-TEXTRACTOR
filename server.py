import requests
import spacy
import fitz  # PyMuPDF
from flask import Flask, request, jsonify, abort

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Define the Flask app
app = Flask(__name__)

# Hardcoded API keys
API_KEYS = ["123456789012345", "abcdefabcdefabc", "qwertyuiopasdfg"]

def download_pdf(url, filename):
    # Download PDF from the provided URL
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"PDF downloaded: {filename}")

def extract_text_from_pdf(pdf_path):
    # Extract text from PDF using PyMuPDF (fitz)
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def analyze_and_tokenize(text):
    # Process the text through spaCy's pipeline
    doc = nlp(text)
    
    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents]
    
    # Extract tokens (words) excluding punctuation and spaces
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    
    # Sentence and token counts
    sentence_count = len(sentences)
    token_count = len(tokens)
    
    return sentences, sentence_count, token_count

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    # Get the API key from the headers
    api_key = request.headers.get('API-Key')
    
    # Validate the API key
    if api_key not in API_KEYS:
        abort(401, description="Unauthorized: Invalid API Key")
    
    # Get the PDF URL from the request JSON data
    data = request.get_json()
    pdf_url = data.get("pdf_url")
    
    if not pdf_url:
        abort(400, description="Bad Request: No PDF URL provided")
    
    # Download the PDF file
    pdf_filename = "downloaded_pdf.pdf"
    download_pdf(pdf_url, pdf_filename)
    
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_filename)
    
    # Tokenize sentences and get analytics
    sentences, sentence_count, token_count = analyze_and_tokenize(text)
    
    # Convert sentences to a single string
    sentences_string = " ".join(sentences)
    
    # Prepare the response data
    response_data = {
        "extracted_text": sentences_string,
        "sentence_count": sentence_count,
        "token_count": token_count
    }
    
    # Return the response as JSON
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

