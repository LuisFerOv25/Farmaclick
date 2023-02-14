from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from os import listdir
from flask import flash

from administrador import administrador
from cliente import cliente
from auth import autenticar


app = Flask(__name__)

app.register_blueprint(administrador)
app.register_blueprint(cliente)
app.register_blueprint(autenticar)

@app.errorhandler(500)
def base_error_handler(e):
    return render_template('error500.html', error="Parece que ha habido un error"), 500

@app.errorhandler(404)
def error_404_handler(e):
    return render_template("error404.html", error="Página no encontrada"), 404

@app.errorhandler(401)
def error_401_handler(e):
    return render_template('error401.html', error="No tienes permisos de acceso"), 401


if __name__ == '__main__':
    app.run(debug=True, port=5010)
