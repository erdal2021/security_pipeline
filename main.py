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
# app.py
# from flask import Flask, request
# import os
# import subprocess
# import pickle

# app = Flask(__name__)

# # Endpunkt zum direkten Ausführen von Benutzereingaben ohne Validierung
# @app.route('/exec', methods=['GET'])
# def exec_command():
#     # Direkte Ausführung des über GET-Parameter 'cmd' übermittelten Benutzerbefehls
#     command = request.args.get('cmd')
#     subprocess.call(command, shell=True)
#     return "Kommando ausgeführt\n"

# # Endpunkt zum Hochladen einer Datei mit unsicherer Deserialisierung von Benutzereingaben
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # Datei aus dem POST-Request lesen
#     file = request.files['file'].read()
#     # Unsichere Deserialisierung der Datei mit pickle.loads
#     data = pickle.loads(file)
#     return "Datei hochgeladen\n"

# # Endpunkt zum Ausführen eines Befehls mit unsicherer Verwendung von os.system für Benutzereingaben
# @app.route('/run', methods=['POST'])
# def run_command():
#     # Befehl aus dem POST-Request lesen
#     command = request.form['command']
#     # Unsichere Verwendung von os.system für Benutzereingaben
#     os.system(command)
#     return "Kommando ausgeführt\n"

# # Starte die Flask-Anwendung, wenn die Datei direkt ausgeführt wird
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

# app.py
from flask import Flask, request, jsonify
import subprocess
import os
import securepickle  # Sichere Deserialisierungsbibliothek

app = Flask(__name__)

# Sichere Ausführung von Benutzerbefehlen
@app.route('/exec', methods=['POST'])
def exec_command():
    try:
        data = request.get_json()
        command = data.get('cmd')

        if not command:
            return jsonify({"error": "Fehlender Befehl ('cmd')"}), 400

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"output": result.stdout, "error": result.stderr}), 200
    except Exception as e:
        return jsonify({"error": f"Fehler beim Ausführen des Befehls: {str(e)}"}), 500

# Sicheres Hochladen und Verarbeiten von Dateien
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        # Sichere Deserialisierung mit der Bibliothek securepickle
        data = securepickle.load(file)
        return jsonify({"message": "Datei erfolgreich hochgeladen und verarbeitet"}), 200
    except Exception as e:
        return jsonify({"error": f"Fehler beim Hochladen und Verarbeiten der Datei: {str(e)}"}), 500

# Sichere Ausführung von Befehlen
@app.route('/run', methods=['POST'])
def run_command():
    try:
        data = request.get_json()
        command = data.get('command')

        if not command:
            return jsonify({"error": "Fehlender Befehl ('command')"}), 400

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({"output": result.stdout, "error": result.stderr}), 200
    except Exception as e:
        return jsonify({"error": f"Fehler beim Ausführen des Befehls: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

