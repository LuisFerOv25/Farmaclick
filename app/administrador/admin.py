from flask import render_template
from datetime import date
from flask import request,session
from . import administrador
import controlador_juegos
from flask import Flask,url_for,redirect

from datetime import date


from bd import *  #Importando conexion BD
from controlador_juegos import *  #Importando mis Funciones

import re
from werkzeug.security import generate_password_hash, check_password_hash

#Rutas para acceder a las vistas del administrador 

@administrador.route('/home_admin/')
def home_admin():
    return render_template("home.html")

@administrador.route("/registrar_producto", methods=["POST"])
def registrar_producto():
    
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    proveedor = request.form["proveedor"]
    fecha_vencimiento = request.form["fecha_vencimiento"]
    imagen = request.form["imagen"]
    categoria = request.form["categoria"]
    controlador_juegos.insertar_producto(nombre, descripcion, cantidad,precio,proveedor,fecha_vencimiento,imagen,categoria)
    # De cualquier modo, y si todo fue bien, redireccionar
    return render_template("home.html")


#Gestion de productos
@administrador.route('/cuidado_personal/')
def cuidado_personal():
    productos = controlador_juegos.producto_personal()
    return render_template("cuidadopersonal.html", productos=productos)

@administrador.route('/dermacosmetico/')
def dermacosmetico():
    productos = controlador_juegos.producto_dermacosmetico()
    return render_template("dermacos.html", productos=productos)


@administrador.route('/nutricional/')
def nutricional():
    productos = controlador_juegos.producto_nutricional()
    return render_template("nutricional.html", productos=productos)


@administrador.route('/bebe/')
def bebe():
    productos = controlador_juegos.producto_bebe()
    return render_template("bebe.html", productos=productos)


@administrador.route('/medicamento/')
def medicamento():
    productos = controlador_juegos.producto_medicamento()
    return render_template("medicamento.html", productos=productos)

#Gestion de usuarios
@administrador.route('/gestionadmin/')
def gestionadmin():
    usuarios = controlador_juegos.usuario_admin()
    return render_template("gestionadmin.html", usuarios=usuarios)

@administrador.route('/gestioncliente/')
def gestioncliente():
    usuarios = controlador_juegos.usuario_cliente()
    return render_template("gestioncliente.html", usuarios=usuarios)

@administrador.route("/formulario_editar_producto/<int:id_producto>")
def editar_producto(id_producto):
    # Obtener el juego por ID
    productos = controlador_juegos.obtener_producto_por_id(id_producto)
    return render_template("editar_producto.html", productos=productos)


@administrador.route("/formulario_editar_usuario/<int:id>")
def editar_usuario(id):
    # Obtener el juego por ID
    usuarios = controlador_juegos.obtener_producto_por_id(id)
    return render_template("editar_usuario.html", usuarios=usuarios)

@administrador.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id_producto = request.form["id_producto"]
    nombre = request.form["nombre"]
    cantidad = request.form["cantidad"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    fecha_vencimiento = request.form["fecha_vencimiento"]
    controlador_juegos.actualizar_producto(nombre,descripcion,cantidad ,precio,fecha_vencimiento,id_producto )
    return render_template("home.html")


@administrador.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id= request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    genero = request.form["genero"]
    controlador_juegos.insertar_usuario(nombre, apellido,correo,direccion,telefono,genero)
    return render_template("home.html")


@administrador.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_juegos.eliminar_producto(request.form["id_producto"])
    return render_template("home.html")



@administrador.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_juegos.eliminar_usuario(request.form["id"])
    return render_template("home.html")


@administrador.route('/registro_admin', methods=['GET', 'POST'])
def registerUser():
    msg = ''
    conexion = obtener_conexion()
    if request.method == 'POST':
        tipo_user                   = request.form['tipo_user']
        nombre                      = request.form['nombre']
        apellido                    = request.form['apellido']
        correo                       = request.form['correo']
        direccion                       = request.form['direccion']
        telefono                       = request.form['telefono']
        password                    = request.form['password']
        repite_password             = request.form['repite_password']
        genero                        = request.form['genero']
        create_at                   = date.today()
        #current_time = datetime.datetime.now()

        # Comprobando si ya existe la cuenta de Usuario con respecto al correo
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuario WHERE correo = %s', (correo,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL
          
        if account:
            msg = 'Ya existe el Email!'
        elif password != repite_password:
            msg = 'Disculpa, las clave no coinciden!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', correo):
            msg = 'Disculpa, formato de Email incorrecto!'
        elif not correo or not password or not password or not repite_password:
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuario (tipo_user, nombre, apellido, correo,direccion,telefono, password,genero, create_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (tipo_user, nombre, apellido, correo,direccion,telefono, password_encriptada, genero, create_at))
            conexion.commit()
            cursor.close()
            msg = 'Cuenta creada correctamente!'

        return render_template('login.html', msjAlert = msg, typeAlert=1)
    return render_template('login.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0)
