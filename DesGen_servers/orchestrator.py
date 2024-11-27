from flask import Flask, request, jsonify
import requests  

app = Flask(__name__)

AI_SERVER_URL = "http://localhost:8072" # AI server's URL

@app.route('/generate', methods=['POST'])
def generate_description():
    #receiving the description from the interface
    data = request.json
    pet_details = data.get("pet_details")
    #error handling if no pet details are given
    if not pet_details:
        return jsonify({"error": "No pet details provided"}), 400

    # send the request to the AI server
    response = requests.post(f"{AI_SERVER_URL}/generate", json={"pet_details": pet_details})
    #error handling in case of unsuccessful conncetion to AI server
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to generate description. problem with the orchestrator!"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=8071)
