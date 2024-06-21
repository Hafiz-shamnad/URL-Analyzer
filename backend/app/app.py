# backend/app.py

from flask import Flask, jsonify, request, send_from_directory
from security_check import check_website_security
from flask_cors import CORS


app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/api/check-security', methods=['GET'])
def check_security():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        results = check_website_security(url)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
