from flask import Flask, render_template, send_from_directory, send_file, request, redirect, send_file
import os
import csv
import zipfile
from generate import generate_images

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mode = request.form['inputMode']
        prompts = []

        if mode == 'csv' and 'promptFile' in request.files:
            file = request.files['promptFile']
            if file.filename.endswith('.csv'):
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                with open(file_path, newline='') as f:
                    reader = csv.reader(f)
                    prompts = [row[0] for row in reader if row]

        elif mode == 'manual':
            manual_input = request.form.get('manualPrompts', '')
            prompts = [line.strip() for line in manual_input.split('\n') if line.strip()]

        if prompts:
            generate_images(prompts)

        return redirect('/results')

@app.route('/results')
def results():
    image_files = os.listdir('static/images')
    return render_template('results.html', images=image_files)

@app.route('/download')
def download_zip():
    zip_path = "static/generated_images.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for fname in os.listdir("static/images"):
            zipf.write(os.path.join("static/images", fname), fname)
    return send_file(zip_path, as_attachment=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mode = request.form['inputMode']
        prompts = []

        if mode == 'csv' and 'promptFile' in request.files:
            file = request.files['promptFile']
            if file.filename.endswith('.csv'):
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                with open(file_path, newline='') as f:
                    reader = csv.reader(f)
                    prompts = [row[0] for row in reader if row]

        elif mode == 'manual':
            manual_input = request.form.get('manualPrompts', '')
            prompts = [line.strip() for line in manual_input.split('\n') if line.strip()]

        if prompts:
            generate_images(prompts)
        return redirect('/results')

    return render_template('index.html')  # ← should be here


if __name__ == '__main__':
    app.run(debug=True)
