from flask import Blueprint

app_pessoas = Blueprint("pessoas", __name__, url_prefix="/pessoas")


@app_pessoas.route("/")
def index():
    return f"Page people."


@app_pessoas.route("/adm")
def adm():
    return f"Page people adm!!!"

