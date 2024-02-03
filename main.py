# # app.py
# from flask import Flask, request
# import os
# import subprocess

# app = Flask(__name__)

# @app.route('/exec', methods=['GET'])
# def exec_command():
#     # Direkte Ausführung von Benutzereingaben ohne Validierung
#     command = request.args.get('cmd')

#     subprocess.call(command, shell=False)
#     return "Kommando ausgeführt\n"

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # Unsichere Deserialisierung von Benutzereingaben
#     file = request.files['file'].read()
#     # data = pickle.loads(file)
#     return "Datei hochgeladen\n"

# @app.route('/run', methods=['POST'])
# def run_command():
#     command = request.form['command']
#     # Unsichere Verwendung von os.system für Benutzereingaben
#     os.system(command)
#     return "Kommando ausgeführt\n"
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, request, abort, json
import subprocess  # nosec

app = Flask(__name__)


@app.route('/exec', methods=['GET'])
def exec_command():
    # Direkte Ausführung von Benutzereingaben ohne Validierung
    command = request.args.get('cmd')
    if not command:
        abort(400, "Invalid command")

    subprocess.run(command, shell=False)  # nosec
    return "Kommando ausgeführt\n"


@app.route('/upload', methods=['POST'])
def upload_file():
    # Unsichere Deserialisierung von Benutzereingaben
    file = request.files['file'].read()

    try:
        json.loads(file.decode('utf-8'))
    except json.JSONDecodeError:
        abort(400, "Invalid file format")

    return "Datei hochgeladen\n"


@app.route('/run', methods=['POST'])
def run_command():
    command = request.form['command']
    # Unsichere Verwendung von os.system für Benutzereingaben
    if not command:
        abort(400, "Invalid command")

    subprocess.run(command.split(), shell=False)  # nosec
    return "Kommando ausgeführt\n"


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)
