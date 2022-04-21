from ast import arg
from flask import Flask, jsonify, request
from run_pessoas import app_pessoas
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)
app.register_blueprint(app_pessoas)

name = {}


@api.route("/<string:id>")
class Hello(Resource):
    
    def get(self, id):
        return {id: name[id]}
    
    def put(self, id):
        name[id] = request.form["data"]
        return {id: name[id]}
    
   
@api.route("/pessoa/<string:nome>/<int:numero>")
class Pessoa(Resource):
 def post(self, nome, numero) -> None:
        return jsonify({"nome": str(nome), "numero": int(numero)}) 

if __name__ == "__main__":
    app.run(debug=True)