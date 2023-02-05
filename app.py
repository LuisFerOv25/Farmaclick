from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from os import listdir
from werkzeug.utils import secure_filename
from flask import flash

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("/login/login.html")

 
def error404(error):
    return render_template("/estatico/error404.html"),404


# Rutas para login y recuperacion de cuenta
@app.route('/login/')
def login():
    return render_template("/login/login.html")

@app.route('/recuperar_correo/')
def recuperarc():
    return render_template("/login/cuenta.html")

@app.route('/verificar/')
def verificar():
    return render_template("/login/cuenta2.html")

@app.route('/validar/')
def validar():
    return render_template("/login/cuenta3.html")

#Rutas para acceder a las vistas del administrador 

@app.route('/home_admin/')
def home_admin():
    return render_template("/admin/home.html")

#Gestion de productos
@app.route('/cuidado_personal/')
def cuidado_personal():
    return render_template("/admin/cuidadopersonal.html")

@app.route('/dermacosmetico/')
def dermacosmetico():
    return render_template("/admin/dermacos.html")


@app.route('/nutricional/')
def nutricional():
    return render_template("/admin/nutricional.html")


@app.route('/bebe/')
def bebe():
    return render_template("/admin/bebe.html")


@app.route('/medicamento/')
def medicamento():
    return render_template("/admin/medicamento.html")

#Gestion de usuarios
@app.route('/gestionadmin/')
def gestionadmin():
    return render_template("/admin/gestionadmin.html")

@app.route('/gestioncliente/')
def gestioncliente():
    return render_template("/admin/gestioncliente.html")

# Home cliente
@app.route('/homecliente/')
def homecliente():
    return render_template("/cliente/homecliente.html")


if __name__ == '__main__':
    app.register_error_handler(404,error404 )
    app.run(debug=True,port=5000)