
from bd import *
from flask import session,render_template

def insertar_producto(nombre, descripcion, cantidad,precio,proveedor,fecha_vencimiento,imagen,categoria):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO producto(nombre, descripcion,cantidad, precio,proveedor,fecha_vencimiento,imagen,categoria) VALUES (%s, %s, %s,%s, %s, %s, %s, %s)",
                        (nombre, descripcion, cantidad,precio,proveedor,fecha_vencimiento,imagen,categoria))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f'Ha ocurrido el error {e}')
    
def insertar_usuario(tipo_user,nombre, apellido, direccion,correo,telefono,genero,imagen):
    conexion = obtener_conexion()
    
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(tipo_user,nombre, apellido,correo,direccion,telefono,genero,imagen) VALUES (%s, %s, %s,%s, %s, %s, %s, %s)",
                       (tipo_user,nombre, apellido,correo,direccion,telefono,genero,imagen))
    conexion.commit()
    conexion.close()


def producto_personal():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where CATEGORIA = 1 LIMIT 0,10")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def producto_dermacosmetico():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where CATEGORIA = 2 LIMIT 0,10")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def producto_nutricional():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where CATEGORIA = 3 LIMIT 0,10")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def producto_bebe():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where CATEGORIA = 4 LIMIT 0,10 ")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def producto_medicamento():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM producto where CATEGORIA = 5 LIMIT 0,10")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def usuario_admin():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario where tipo_user = 1 LIMIT 0,10")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def usuario_cliente():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario where tipo_user = 2 LIMIT 0,10")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


def user_cant_admin():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM usuario where tipo_user = 1")
        usuarios = cursor.fetchone()[0]
    conexion.close()
    return usuarios

def user_cant_client():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM usuario where tipo_user = 2")
        usuarios = cursor.fetchone()[0]
    conexion.close()
    return usuarios


def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
    conexion.commit()
    conexion.close()

def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()    
    


def obtener_producto_por_id(id_producto):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_producto,nombre, descripcion,cantidad, precio,proveedor,fecha_vencimiento,imagen FROM producto WHERE id_producto = %s", (id_producto,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombre,apellido,correo, direccion,telefono,genero FROM usuario WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_producto(nombre, descripcion,cantidad, precio,fecha_vencimiento,imagen,id_producto ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s,cantidad = %s, precio = %s,fecha_vencimiento = %s,imagen = %s WHERE id_producto = %s",
                       (nombre,descripcion,cantidad,precio,fecha_vencimiento,imagen,id_producto ))
    conexion.commit()
    conexion.close()
    
def actualizar_usuario(nombre, apellido, correo,direccion,telefono,genero,imagen,id ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombre = %s, apellido = %s,correo = %s, direccion = %s,telefono = %s,genero = %s,imagen = %s WHERE id = %s",
                       (nombre, apellido, correo,direccion,telefono,genero,imagen,id))
    conexion.commit()
    conexion.close()
    
#FUNCIONES PARA CREDENCIALES DE ACCESO

def dataLoginSesion():
    inforLogin = {
        "id"                  :session['id'],
        "tipoLogin"           :session['tipo_user'],
        "nombre"              :session['nombre'],
        "apellido"            :session['apellido'],
        "emailLogin"          :session['correo'],
        "direccion"           :session['direccion'],
        "telefono"            :session['telefono'],
        "genero"              :session['genero'],
        "create_at"           :session['create_at'],
        "imagen"              :session['imagen']
    }
    return inforLogin

def dataPerfilUsuario():
    conexion = obtener_conexion()
    mycursor       = conexion.cursor()
    idUser         = session['id']
    
    querySQL  = ("SELECT * FROM ususrio WHERE id='%s'" % (idUser,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion.close() #cerrando conexion de la BD
    return datosUsuario
