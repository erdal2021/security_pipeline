# # app.py
# from flask import Flask, request
# import os
# import subprocess
# import pickle

# app = Flask(__name__)

# @app.route('/exec', methods=['GET'])
# def exec_command():
#     # Direkte Ausführung von Benutzereingaben ohne Validierung
#     command = request.args.get('cmd')
#     subprocess.call(command, shell=True)
#     return "Kommando ausgeführt\n"

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
from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/exec', methods=['POST'])
def exec_command():
    try:
        data = request.json
        command = data.get('cmd')
        
        if not command:
            return jsonify({"error": "Invalid command"}), 400

        subprocess.run(command.split(), check=True)
        return jsonify({"message": "Command executed successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file'].read()
        data = json.loads(file)
        return jsonify({"message": "File uploaded successfully"}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid file format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/run', methods=['POST'])
def run_command():
    try:
        data = request.json
        command = data.get('command')
        
        if not command:
            return jsonify({"error": "Invalid command"}), 400

        subprocess.run(command.split(), check=True)
        return jsonify({"message": "Command executed successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
