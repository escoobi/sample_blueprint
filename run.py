from flask import Flask, jsonify, request
from run_pessoas import app_pessoas
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version="0.1", title="API in Flask Restx", description="Usando API para Consultar e Inserir Dados!" )
app.register_blueprint(app_pessoas)

ns = api.namespace('Pessoas', description='Operações com Pessoas')

listaPessoa = api.model('Pessoa', {
    'id': fields.Integer(readonly=True, description='Id Pessoa'),
    'name': fields.String(required=True, description='Nome Pessoa')
})



class PessoaCRUD(object):
    
    def __init__(self) -> None:
        self.counter = 0
        self.pessoas = []

    def get(self, id):
        for x in self.pessoas:
            if x["id"] == id:
                return listaPessoa
        ns.abort(404, "Pessoa {} não existe".format(id))
        
    def create(self, data):
        listaPessoa = data
        listaPessoa["id"] = self.counter = self.counter + 1
        self.pessoas.append(listaPessoa)
        return listaPessoa
    
    def update(self, id, data):
        listaPessoa = self.get(id)
        listaPessoa.update(data)
        return listaPessoa
    
    def delete(self, id):
        listaPessoa = self.get(id)
        print(listaPessoa)
        self.pessoas.remove(listaPessoa)


pp = PessoaCRUD()
pp.create({"name": "Gustavo"})
pp.create({"name": "Elaine"})
pp.create({"name": "Arthur"})

   
@ns.route("/")
class PessoaLista(Resource):
    
    @ns.doc("Lista todos!")
    @ns.marshal_list_with(listaPessoa)
    
    def get(self):
        '''Retorna a lista completa'''
        return pp.pessoas

    @ns.doc("Criar Pessoa")
    @ns.expect(listaPessoa)
    @ns.marshal_with(listaPessoa, code=201)
    def post(self):
        '''Cria uma nova listaPessoa'''
        return pp.create(api.payload), 201
    

@ns.route("/<int:id>")
@ns.response(404, "Pessoa não encontrada!")
@ns.param("id", "Nome Pessoa")
class Pessoa(Resource):
    
    @ns.doc("Obtem todos!")
    @ns.marshal_with(listaPessoa)
    def get(self, id):
        '''Obtem pessoas!'''
        return PessoaCRUD.get(id)
    
    @ns.doc("Deleta Pessoa!")
    @ns.response(204, "Pessoa Deletada!")
    def delete(self, id):
        '''Delete a listaPessoa com base no Id'''
        PessoaCRUD.delete(id)
        return "", 204
    
    @ns.expect(listaPessoa)
    @ns.marshal_with(listaPessoa)
    def put(self, id):
        '''Atualiza a listaPessoa com base no Id'''
        return PessoaCRUD.update(id, api.payload)
    

if __name__ == "__main__":
    app.run(debug=True)