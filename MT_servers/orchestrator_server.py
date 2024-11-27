from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AI_SERVER_URL = 'http://127.0.0.1:8052/translate'  # AI server's URL

@app.route('/translate', methods=['POST'])
def orchestrator_translate():
    #receiving the description from the interface
    data = request.get_json() 
    text = data.get('text', '')
    
    # send the request to the AI server
    response = requests.post(AI_SERVER_URL, json={"text": text})
    #if connection successful
    #ERROR HAN
    if response.status_code == 200:
        translated_text = response.json().get('translated_text', '')
        return jsonify({"translated_text": translated_text})
    else:
        return jsonify({"error": "Translation failed. problem with the orchestrator"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8051)  # Orchestrator server runs on port 5002
