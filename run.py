from flask import Flask, jsonify
from run_pessoas import app_pessoas
from flask_restx import Api, Resource


api = Api()
app = Flask(__name__)
app.register_blueprint(app_pessoas)
api.init_app(app)

@api.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "123"}

if __name__ == "__main__":
    app.run(debug=True)