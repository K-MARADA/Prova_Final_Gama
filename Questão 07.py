import json
from flask import Flask, request

print("••• Q U E S T Ã O   0 7 •••\n")
app = Flask(__name__)

@app.route("/soma", methods=['POST'])
def soma():
    dados = request.get_json()

    x = int(dados.get('x'))
    y = int(dados.get('y'))

    return json.dumps({"resultado": x + y })

app.run('0.0.0.0', port=5000)