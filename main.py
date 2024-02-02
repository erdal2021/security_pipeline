# app.py
from flask import Flask, request
import os
import subprocess
import pickle

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_command():
    # Direkte Ausführung von Benutzereingaben ohne Validierung
    command = request.args.get('cmd')
    subprocess.call(command, shell=False)
    return "Kommando ausgeführt\n"

@app.route('/upload', methods=['POST'])
def upload_file():
    # Unsichere Deserialisierung von Benutzereingaben
    file = request.files['file'].read()
    data = pickle.loads(file)
    return "Datei hochgeladen\n"

@app.route('/run', methods=['POST'])
def run_command():
    command = request.form['command']
    # Unsichere Verwendung von os.system für Benutzereingaben
    os.system(command)
    return "Kommando ausgeführt\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
