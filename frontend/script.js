/**
 * Frontend script to connect with Flask API
 */

async function analyzeContract() {
    const textInput = document.getElementById('contractText').value;
    const errorDiv = document.getElementById('error');
    const analyzeBtn = document.getElementById('analyzeBtn');

    // Reset results and hide errors
    document.getElementById('resObligor').innerText = '-';
    document.getElementById('resAmount').innerText = '-';
    document.getElementById('resDate').innerText = '-';
    errorDiv.style.display = 'none';

    // Basic validation
    if (!textInput.trim()) {
        showError('Please enter some contract text first.');
        return;
    }

    // Update UI state to loading
    analyzeBtn.disabled = true;
    analyzeBtn.innerText = 'Analyzing...';

    try {
        // Send request to Flask API
        const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ contract: textInput })
        });

        const data = await response.json();

        // Handle successful response
        if (response.ok) {
            document.getElementById('resObligor').innerText = data.entities.obligor;
            document.getElementById('resAmount').innerText = data.entities.amount;
            document.getElementById('resDate').innerText = data.entities.date;
        } else {
            // Handle logical backend errors
            showError(data.error || 'Failed to analyze text.');
        }

    } catch (error) {
        // Handle network errors
        console.error('API Error:', error);
        showError('Error connecting to the backend API. Please make sure the Flask server is running.');
    } finally {
        // Restore button state
        analyzeBtn.disabled = false;
        analyzeBtn.innerText = 'Analyze Contract';
    }
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.innerText = message;
    errorDiv.style.display = 'block';
}
