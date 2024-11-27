from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
# from codecarbon import EmissionsTracker
import csv
app = Flask(__name__)

# Initialize CodeCarbon tracker
# tracker = EmissionsTracker(allow_multiple_runs=True)
# tracker.start()

# Loading the pre-trained MarianMT model for english to dutch texts
model_name = "Helsinki-NLP/opus-mt-en-nl"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

@app.route('/translate', methods=['POST'])
def translate():
    #receiving the description from the orchestrator
    data = request.get_json()
    text = data.get('text', '')
    # Tokenize and translate
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**tokens)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    #stop CodeCarbon tracker and print the results. it will also save it into a csv file 
    # emissions = tracker.stop()
    # print(f"Carbon emissions for this translation task: {emissions} kg CO2")
    #return translation
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8052)  # AI server runs on port 5001
