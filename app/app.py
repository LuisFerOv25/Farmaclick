from flask import Flask
from flask import render_template
from flask import request,session
from administrador import administrador
from cliente import cliente
from auth import autenticar
from datetime import date
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'


#Conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_farmaclick'


mysql = MySQL(app)

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
