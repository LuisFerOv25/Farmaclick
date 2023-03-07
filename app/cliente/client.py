from flask import render_template
from controller import *  # Importando mis Funciones
from . import cliente
from bd import *  # Importando conexion BD


@cliente.route('/')
def index():
    return render_template("inicio.html")

# Home cliente
@cliente.route('/homecliente/')
def homecliente():
    return render_template("homecliente.html")

# Medicamentos cliente
@cliente.route('/medicamentoscliente/')
def medicamentoscliente():
    return render_template("medicamentos.html")

# Datos cliente
@cliente.route('/datoscliente/')
def datoscliente():
    return render_template('datoscliente.html', dataLogin= dataLoginSesion())


# Comprar producto
@cliente.route('/comprarproducto/')
def comprarproducto():
    return render_template("comprarproducto.html")

# Cuidado personal
@cliente.route('/cuidadopersonalclient/')
def cuidadopersonalclient():
    return render_template("cuidadopersonalclient.html")

# Dermacosmeticos
@cliente.route('/dermacosmetica/')
def dermacosmetica():
    return render_template("dermacosmetica.html")

# Nutricionales
@cliente.route('/nutricionales/')
def nutricionales():
    return render_template("nutricionales.html")

# Bebe
@cliente.route('/bebe02/')
def bebe02():
    return render_template("bebe02.html")

# Inicio cliente
@cliente.route('/inicio/')
def inicio():
    return render_template("inicio.html")
