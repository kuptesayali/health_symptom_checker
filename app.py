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
    # Get the user input
    symptom = request.form['symptom']

    # Call match_symptoms (it expects a list)
    results = matcher.match_symptoms([symptom])

    # Pass results to the template
    return render_template('results.html', symptom=symptom, results=results)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
