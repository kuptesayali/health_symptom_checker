from flask import Flask, render_template, request
from src import matcher  # this works now

# Create Flask app
app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Check symptom route
@app.route('/check', methods=['POST'])
def check():
    symptom = request.form['symptom']
    results = matcher.get_matches(symptom, top_k=5)
    return render_template('results.html', symptom=symptom, results=results)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
