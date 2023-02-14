from flask import render_template
from . import administrador
#Rutas para acceder a las vistas del administrador 

@administrador.route('/home_admin/')
def home_admin():
    return render_template("home.html")

#Gestion de productos
@administrador.route('/cuidado_personal/')
def cuidado_personal():
    return render_template("cuidadopersonal.html")

@administrador.route('/dermacosmetico/')
def dermacosmetico():
    return render_template("dermacos.html")


@administrador.route('/nutricional/')
def nutricional():
    return render_template("nutricional.html")


@administrador.route('/bebe/')
def bebe():
    return render_template("bebe.html")


@administrador.route('/medicamento/')
def medicamento():
    return render_template("medicamento.html")

#Gestion de usuarios
@administrador.route('/gestionadmin/')
def gestionadmin():
    return render_template("gestionadmin.html")

@administrador.route('/gestioncliente/')
def gestioncliente():
    return render_template("gestioncliente.html")
