# Importieren Sie sichere Bibliotheken
from flask import Flask, request, jsonify
import subprocess
import shlex  # Sichere Verwendung von Befehlszeilen-Argumenten

app = Flask(__name__)

# Sichere Ausführung von Benutzerbefehlen
@app.route('/exec', methods=['POST'])
def exec_command():
    try:
        data = request.get_json()
        command = data.get('cmd')

        if not command:
            return jsonify({"error": "Fehlender Befehl ('cmd')"}), 400

        # Sicherstellen, dass der Befehl sicher ausgeführt wird
        subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)

        return jsonify({"message": "Kommando erfolgreich ausgeführt"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Fehler beim Ausführen des Befehls: {e.stderr}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unerwarteter Fehler: {str(e)}"}), 500
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

@app.route('/upload', methods=['POST'])
def upload_file():
    # Unsichere Deserialisierung von Benutzereingaben
    file = request.files['file'].read()
    data = pickle.load(file)
    return "Datei hochgeladen\n"

@app.route('/run', methods=['POST'])
def run_command():
    command = request.form['command']
    # Unsichere Verwendung von os.system für Benutzereingaben
    os.system(command)
    return "Kommando ausgeführt\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)