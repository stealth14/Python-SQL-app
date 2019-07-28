import pymysql
from tkinter import *
import os
import crud
from crud import *

conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='calificaciones')
cur=conn.cursor()

def inicio():
    global ventana
    ventana=Tk()
    color="white"
    ventana.geometry("300x100")
    ventana.title("Autenticación")
    ventana.config(bg="WHITE")
    Button(ventana,text="Acceder como profesor", height=2, width=30, bg=color,command=login_profesor).pack()
    Label(text="").pack()    
    Button(ventana,text="Acceder como estudiante", height=2, width=30, bg=color,command=login_estudiante).pack() 
    
    ventana.mainloop()


def login_profesor():
    global ventana_profesor
    ventana_profesor = Toplevel(ventana)
    ventana_profesor.title("Acceso como profesor")
    ventana_profesor.geometry("300x250")
    Label(ventana_profesor, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_profesor, text="").pack()

    global profesor_usuario
    global profesor_clave
    global verificar_profesor_usuario
    global verificar_profesor_clave

    verificar_profesor_usuario = StringVar()
    verificar_profesor_clave = StringVar()
  
    Label(ventana_profesor, text="Nombre usuario ").pack()
    profesor_usuario = Entry(ventana_profesor, textvariable=verificar_profesor_usuario)
    profesor_usuario.pack()
    Label(ventana_profesor, text="").pack()
    Label(ventana_profesor, text="Contraseña ").pack()
    profesor_clave = Entry(ventana_profesor, textvariable=verificar_profesor_clave,show='*')
    profesor_clave.pack()
    Label(ventana_profesor, text="").pack()
    Button(ventana_profesor, text="Entrar", width=10, height=1,command=verificar_profesor).pack()

def verificar_profesor():
    usuario=verificar_profesor_usuario.get()
    clave=verificar_profesor_clave.get()
    profesor_usuario.delete(0,END)
    profesor_clave.delete(0,END)
    lista_nombre=[]
    lista_clave=[]
    buscar_usuario="SELECT nombre_profesor FROM profesor"
    cur.execute(buscar_usuario)
    lista_profesor=cur.fetchall()    
    for row in lista_profesor:
        lista_nombre.append(str(row[0]))
    if usuario in lista_nombre:
            v_clave="SELECT contrasenia_profesor FROM profesor"
            cur.execute(v_clave)
            claves=cur.fetchall()
            for raw in claves:
                lista_clave.append(raw[0])
            if clave in lista_clave:
                conexion_exitosa()
    else:
        conexion_fallida()
            


def login_estudiante():
    global ventana_estudiante
    ventana_estudiante = Toplevel(ventana)
    ventana_estudiante.title("Acceso como estudiante")
    ventana_estudiante.geometry("300x250")
    Label(ventana_estudiante, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_estudiante, text="").pack()
    
    global estudiante_usuario
    global estudiante_clave
    global verificar_estudiante_usuario
    global verificar_estudiante_clave

    verificar_estudiante_usuario = StringVar()
    verificar_estudiante_clave = StringVar()
  
    Label(ventana_estudiante, text="Nombre usuario ").pack()
    estudiante_usuario = Entry(ventana_estudiante, textvariable=verificar_estudiante_usuario)
    estudiante_usuario.pack()
    Label(ventana_estudiante, text="").pack()
    Label(ventana_estudiante, text="Contraseña ").pack()
    estudiante_clave = Entry(ventana_estudiante, textvariable=verificar_estudiante_clave,show='*')
    estudiante_clave.pack()
    Label(ventana_estudiante, text="").pack()
    Button(ventana_estudiante, text="Entrar", width=10, height=1,command=verificar_estudiante).pack()

def verificar_estudiante():
    usuario=verificar_estudiante_usuario.get()
    clave=verificar_estudiante_clave.get()
    estudiante_usuario.delete(0,END)
    estudiante_clave.delete(0,END)
    lista_nombre=[]
    lista_clave=[]
    buscar_usuario="SELECT nombre_estudiante FROM estudiantes"
    cur.execute(buscar_usuario)
    lista_estudiante=cur.fetchall()    
    for row in lista_estudiante:
        lista_nombre.append(str(row[0]))
    if usuario in lista_nombre:
            v_clave="SELECT contrasenia_estudiantes FROM estudiantes"
            cur.execute(v_clave)
            claves=cur.fetchall()
            for raw in claves:
                lista_clave.append(raw[0])
            if clave in lista_clave:
                conexion_exitosa1()
    else:
        conexion_fallida1()

def conexion_exitosa():
    global conexion,root
    conexion = Toplevel(ventana_profesor)
    conexion.title("Exito")
    conexion.geometry("300x50")
    Label(conexion, text="Login finalizado con exito").pack()
    root = True
    Button(conexion, text="Aceptar",command=salir_conexion1).pack()

def conexion_fallida():
    global conexionf
    conexionf = Toplevel(ventana_profesor)
    conexionf.title("ERROR")
    conexionf.geometry("300x50")
    Label(conexionf, text="Usuario o contraseña incorrectos").pack()
    Button(conexionf, text="Volver", command=salir_conexion1_fallida).pack()


def conexion_exitosa1():
    global conexion,root
    conexion = Toplevel(ventana_estudiante)
    conexion.title("Exito")
    conexion.geometry("300x50")
    Label(conexion, text="Login finalizado con exito").pack()
    root = False
    Button(conexion, text="Aceptar",command=salir_conexion1).pack()

def conexion_fallida1():
    global conexionf
    conexionf = Toplevel(ventana_estudiante)
    conexionf.title("ERROR")
    conexionf.geometry("300x50")
    Label(conexionf, text="Usuario o contraseña incorrectos").pack()
    Button(conexionf, text="Volver", command=salir_conexion1_fallida).pack()


def salir_conexion1():
    crud.main_crud(True)
    conexion.destroy()

def salir_conexion1_fallida():
    conexionf.destroy()


inicio()


