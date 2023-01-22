import json
from http import HTTPStatus
from flask import Flask, request

print("••• Q U E S T Ã O   0 8 •••\n")
app = Flask(__name__)

contador = 0

@app.route("/contador", methods=['POST'])
def post_contador():
    global contador
    dados = request.get_json()
    contador = int(dados.get('numero'))

    return "", 201

@app.route("/contador", methods=['GET'])
def get_contador():
    return json.dumps({"numero": contador}), 200

@app.route("/contador/incrementa", methods=['PUT'])
def put_contador():
    global contador
    contador += 1

    return "", 202

@app.route("/contador", methods=['DELETE'])
def delete_contador():
    global contador
    contador = 0

    return "", 202

app.run('0.0.0.0', port=5000)