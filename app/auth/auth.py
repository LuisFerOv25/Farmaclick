from flask import render_template
from . import autenticar

# Rutas para login y recuperacion de cuenta
@autenticar.route('/login/')
def login():
    return render_template("login.html")

@autenticar.route('/recuperar_correo/')
def recuperarc():
    return render_template("cuenta.html")

@autenticar.route('/verificar/')
def verificar():
    return render_template("cuenta2.html")

@autenticar.route('/validar/')
def validar():
    return render_template("cuenta3.html")

