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
from error import error

app = Flask(__name__)

app.register_blueprint(administrador)
app.register_blueprint(cliente)
app.register_blueprint(autenticar)
app.register_blueprint(error)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada"), 404


if __name__ == '__main__':
    app.register_error_handler(404,error)
    app.run(debug=True,port=5010)