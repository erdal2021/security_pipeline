# app.py
from flask import Flask, request
import os
import subprocess
import pickle

app = Flask(__name__)

ALLOWED_COMMANDS = ['echo', 'ls']  # Add more allowed commands

@app.route('/exec', methods=['GET'])
def exec_command():
    # Direkte Ausführung von Benutzereingaben ohne Validierung
    command = request.args.get('cmd', '').strip()
        # Check if the command is in the allowed list
    if command not in ALLOWED_COMMANDS:
        return "Invalid command\n", 400
        # Execute the command using subprocess with safe shell escaping
    try:
        subprocess.run(command, shell=True, check=True)
        return "Command executed successfully\n"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}\n", 500
    # subprocess.call(command, shell=True)
    # return "Kommando ausgeführt\n"

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
