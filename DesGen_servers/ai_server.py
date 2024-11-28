from flask import Flask, request, jsonify
import cohere
# from codecarbon import EmissionsTracker
app = Flask(__name__)
# connect tp cohere using a valid API key
COHERE_API_KEY = "API_KEY"
co = cohere.Client(COHERE_API_KEY)
# Initialize CodeCarbon tracker
# tracker = EmissionsTracker(allow_multiple_runs=True)
# tracker.start()

@app.route('/generate', methods=['POST'])
def generate_description():
    #receiving the information from the orchestrator
    data = request.json
    pet_details = data.get("pet_details")
    #error handling in case of no info/error regarding generation model
    if not pet_details:
        return jsonify({"error": "No pet details provided"}), 400 

    try:
        #connect to cohere and ask it for a pet description
        #data will also be fed to the prompt
        response = co.generate(
            model='command-r-08-2024',
            prompt=f"Create a pet adoption description. Here are the details: {pet_details}",
            max_tokens=300
        )
        generated_text = response.generations[0].text
        #stop CodeCarbon tracker and print the results. it will also save it into a csv file 
        # emissions = tracker.stop()
        # print(f"Carbon emissions for this translation task: {emissions} kg CO2")
        return jsonify({"description": generated_text.strip()})
    except Exception as e:
        return jsonify({"error with the AI (API issues)": str(e)}), 500
        # emissions = tracker.stop()
if __name__ == '__main__':
    app.run(debug=True, port=8072)
