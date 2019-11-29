from flask import Flask, json, jsonify
from flask import request
from playhouse.shortcuts import model_to_dict
from petshop import *

app = Flask(__name__)

@app.route('/')
def inicio():
    return "backend do sistema de petshop; <a href=/listar_dados_petshop>API listar dados petshop</a>"

@app.route('/listar_dados_petshop')
def listar_consultas(): 
    consultas = list(map(model_to_dict, Consulta.select()))
    return jsonify({"lista": consultas})

app.run(debug=True, port=4999)



'''
curl localhost:4999/listar_dados_petshop
{
  lista": [
    {
      "clienti": {
        "cpf": 214389, 
        "id": 1, 
        "nome": "Eduardo"
      }, 
      "colaboradorr": {
        "funcao": " veterin\u00e1rio", 
        "id": 1, 
        "nome": "Miguel"
      }, 
      "data": "12/11/2016", 
      "id": 1, 
      "pacientizinho": {
        "animal": "passarinho", 
        "id": 1
      }
    }
  ]
}
'''