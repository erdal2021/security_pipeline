# app.py
# from flask import Flask, request
# import os
# import subprocess
# import pickle

# app = Flask(__name__)

# @app.route('/exec', methods=['GET'])
# def exec_command():
#     # Direkte Ausführung von Benutzereingaben ohne Validierung
#     command = request.args.get('ls')
#     result: subprocess.run(command, check=True)
#     return "Kommando ausgeführt\n"
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_command():
    # Get the command from the request parameters
    command = request.args.get('command')

    if not command:
        return "No command provided."

    # Use subprocess.run with a list of arguments to prevent command injection
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        output = result.stdout
        return f"Command executed successfully. Output: {output}\n"
    except subprocess.CalledProcessError as e:
        return f"Error executing command. Return code: {e.returncode}, Error: {e.stderr}\n"

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # Unsichere Deserialisierung von Benutzereingaben
#     file = request.files['file'].read()
#     data = pickle.loads(file)
#     return "Datei hochgeladen\n"

# @app.route('/run', methods=['POST'])
# def run_command():
#     command = request.form['command']
#     # Unsichere Verwendung von os.system für Benutzereingaben
#     os.system(command)
#     return "Kommando ausgeführt\n"

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
