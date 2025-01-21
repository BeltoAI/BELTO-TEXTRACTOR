import base64
from flask import Flask, request, jsonify
from io import BytesIO
import PyPDF2
import docx
import sys

app = Flask(__name__)

# Set maximum request size to 10 MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

@app.route('/upload-base64', methods=['POST'])
def upload_base64():
    data = request.json

    # Validate input fields
    filename = data.get('filename')
    filedata = data.get('filedata')

    if not filename or not filedata:
        return jsonify({'error': 'Filename and filedata are required'}), 400

    try:
        # Decode base64 file data
        decoded_data = base64.b64decode(filedata)
        if sys.getsizeof(decoded_data) > 10 * 1024 * 1024:
            return jsonify({'error': 'File size exceeds 10MB limit'}), 400

        file_bytes = BytesIO(decoded_data)

        # Process PDF or DOCX files
        if filename.lower().endswith('.pdf'):
            reader = PyPDF2.PdfReader(file_bytes)
            text = ''.join(page.extract_text() or '' for page in reader.pages)
        elif filename.lower().endswith('.docx'):
            doc = docx.Document(file_bytes)
            text = '\n'.join(para.text.strip() for para in doc.paragraphs if para.text.strip())
        else:
            return jsonify({'error': 'Unsupported file format'}), 400

        if not text.strip():
            return jsonify({'error': 'No extractable text found'}), 400

        return jsonify({'text': text}), 200

    except base64.binascii.Error:
        return jsonify({'error': 'Invalid base64 encoding'}), 400
    except Exception as e:
        return jsonify({'error': f'File processing error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)