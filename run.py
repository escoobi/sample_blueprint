from flask import Flask
from view.pessoas.run_pessoas import app_pessoas

app = Flask(__name__)
app.register_blueprint(app_pessoas)

@app.route("/")
def index():
    return f"Page one!!!"

if __name__ == "__main__":
    app.run(debug=True, port=6289)
