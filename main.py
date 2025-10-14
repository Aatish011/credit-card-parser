import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from src.parser import get_parser

# Create an instance of the Flask web application
app = Flask(__name__)

# Configure a folder to temporarily store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the main route for the application
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request is a POST, it means the user has submitted the form
    if request.method == 'POST':
        # Check if a file was included in the request
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Secure the filename to prevent malicious file paths
            filename = secure_filename(file.filename)
            # Save the uploaded file to our configured folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # --- This is where the magic happens ---
            # Use our factory function to get the correct parser for the uploaded file
            parser = get_parser(file_path)
            # Run the parser to extract the data
            data = parser.parse()
            
            # Clean up the uploaded file after processing
            os.remove(file_path)

            # Render the same page, but this time pass in the extracted data
            # The HTML will now display the results in the table
            return render_template('index.html', data=data, filename=filename)

    # If the request is a GET, just show the regular upload page
    return render_template('index.html', data=None)

# This block ensures the server only runs when the script is executed directly
if __name__ == '__main__':
    # Starts the development server on localhost port 5000
    app.run(debug=True)

