from flask import Flask, send_from_directory, render_template, abort
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Serve the main HTML page
@app.route('/')
def serve_html():
    return render_template('3d-model-viewer.html')

# Serve 3D model files with detailed logging
@app.route('/model/<path:filename>')
def serve_model(filename):
    model_dir = 'model'
    
    # Check if the model directory exists
    if not os.path.exists(model_dir):
        print(f"Error: Model directory '{model_dir}' does not exist!")
        abort(404)
    
    # List all files in the model directory for debugging
    print(f"Files in model directory: {os.listdir(model_dir)}")
    
    # Full path to the requested file
    full_path = os.path.join(model_dir, filename)
    
    # Check if the file exists
    if not os.path.exists(full_path):
        print(f"Error: File '{filename}' not found in model directory!")
        abort(404)
    
    # Serve the file
    return send_from_directory(model_dir, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)