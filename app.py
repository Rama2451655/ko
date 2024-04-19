from flask import Flask, render_template, request

app = Flask(__name__)

# Function to process user input
def process_input(user_input):
    # Example processing logic (convert input to uppercase)
    processed_input = user_input.upper()
    return processed_input

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        user_input = request.form['user_input']
        
        # Process the user input
        processed_input = process_input(user_input)
        
        # Render the main page with the processed input
        return render_template('index.html', processed_input=processed_input)
    
    # Render the main page with an empty processed input
    return render_template('index.html', processed_input='')

if __name__ == '__main__':
    app.run(debug=True)
