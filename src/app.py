from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_JSON = BASE_DIR / "instituicoesEnsino.json"

with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
    instituicoes = json.load(arquivo)

@app.get("/")
def index():
    return {
        "versao": "1.0.0",
        "status": "ok",
        "aviso": "to aqui"
    }, 200


@app.get("/instituicoesensino")
def instituicoesensino():   
    return jsonify(instituicoes), 200


@app.get("/instituicoesensino/<int:id>")
def instituicao_por_id(id):

    for instituicao in instituicoes:
        if instituicao["co_entidade"] == id:
            return jsonify(instituicao), 200

    return jsonify({
        "erro": "Instituição não encontrada"
    }), 404


@app.get("/instituicoesensino/<string:nome>")
def instituicao_por_nome(nome):
    for instituicao in instituicoes:
        if instituicao["no_entidade"].lower() == nome.lower():
            return jsonify(instituicao), 200

    return jsonify({
        "erro": "Instituição não encontrada"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)