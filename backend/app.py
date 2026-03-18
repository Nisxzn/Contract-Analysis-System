from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

app = Flask(__name__)
# Enable CORS for frontend to communicate with backend
CORS(app)

# Load spaCy NLP model, download if not exists
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading English language model for spaCy...")
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint that receives contract text and returns extracted entities.
    """
    data = request.get_json()
    
    if not data or 'contract' not in data:
        return jsonify({'error': 'No contract text provided in the request body.'}), 400

    text = data['contract']
    
    # Process the text using spaCy NER
    doc = nlp(text)

    # Initialize default extracted entities
    obligor = "Not found"
    amount = "Not found"
    date = "Not found"

    # Entities we are looking for:
    # ORG (Companies, agencies, institutions) -> OBLIGOR
    # MONEY (Monetary values) -> AMOUNT
    # DATE (Absolute or relative dates) -> DATE

    for ent in doc.ents:
        if ent.label_ == "ORG" and obligor == "Not found":
            obligor = ent.text
        elif ent.label_ == "MONEY" and amount == "Not found":
            amount = ent.text
        elif ent.label_ == "DATE" and date == "Not found":
            date = ent.text

    # Fallback: sometimes spaCy identifies companies as PERSON or GPE
    if obligor == "Not found":
        for ent in doc.ents:
            if ent.label_ in ["PERSON", "GPE"]:
                obligor = ent.text
                break

    # Return the extracted entities as JSON
    return jsonify({
        'entities': {
            'obligor': obligor,
            'amount': amount,
            'date': date
        }
    })

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True, port=5000)
