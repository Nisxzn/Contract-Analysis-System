# Contract Analysis System

## Objective
A simple, beginner-friendly full-stack NLP project designed for academic demonstration. The goal of this system is to analyze short contract texts and extract key entities, specifically:
- **Obligor** (Organization / Company Name)
- **Amount** (Contract amount / Money)
- **Date** (Maturity date or Deadline)

## System Architecture
This project features a lightweight full-stack implementation locally:
1. **Frontend:** HTML, CSS, JavaScript using a clean, minimal UI pattern. Represents a single-page web interface.
2. **Backend:** Python and Flask act as the API server. Provides a simple `POST /analyze` endpoint.
3. **NLP Engine:** spaCy (using the pretrained `en_core_web_sm` model). Extracts specific real-world entities (ORG, MONEY, DATE) based on text.

## Dataset Description
A small synthesized dataset composed of over 100 simple contract sentences, mapped around different financial templates. Includes fields for company names, monetary values, and dates. Useful for evaluation and testing the text analyzer UI natively.
- **Dataset File:** `dataset/contracts.csv`
- A generator Python script `generate_dataset.py` is included which algorithmically generates diverse sentences.

## Implementation Steps
1. **Model Building:** The backend loads `spacy` pre-trained model `en_core_web_sm` and relies on its robust Named Entity Recognition (NER) to isolate `ORG`, `MONEY`, and `DATE`.
2. **Setup Server:** A Flask API endpoint is built, listening for simple requests mapped using standard CORS implementation.
3. **Web View Architecture:** Wrote basic HTML grid and structured the styles explicitly through `Inter` font mimicking high-end minimal design concepts.
4. **Link logic:** Integrated async `fetch()` hooks in `script.js` firing towards the Flask app on port `5000`.

## Example Input and Output
### Example Input (via POST or the frontend text area):
```json
{
    "contract": "ABC Bank agrees to repay $5M before 2030."
}
```

### Example JSON Payload Output:
```json
{
    "entities": {
        "obligor": "ABC Bank",
        "amount": "$5M",
        "date": "2030"
    }
}
```

## Instructions to run the project

### 1. Requirements Installation
Ensure Python (3.x) is installed. First, install the required packages using the terminal:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Run the Backend API Server
Navigate to the backend directory and spin up the Python Flask Server.
```bash
cd backend
python app.py
```
*The server will start executing locally on `http://127.0.0.1:5000/`*

### 3. Open the Frontend
Simply open the `frontend/index.html` file using any modern Web Browser (Chrome, Firefox, Edge, etc.). Paste a contract sentence and run logic.
