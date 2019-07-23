from tkinter import *
import os

def inicio():
    global ventana
    ventana=Tk()
    color="white"
    ventana.geometry("300x100")
    ventana.title("REGISTRO")
    ventana.config(bg="WHITE")
    Button(ventana,text="Acceder como profesor", height=2, width=30, bg=color,command=loginprofesor).pack()
    Label(text="").pack()    
    Button(ventana,text="Acceder como estudiante", height=2, width=30, bg=color).pack() 
    
    ventana.mainloop()


def loginprofesor():
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
    Button(ventana_profesor, text="Entrar", width=10, height=1,command=verificar).pack()


def verificar():
	usuario=verificar_profesor_usuario.get()
	clave=verificar_profesor_clave.get()
	profesor_usuario.delete(0,END)
	profesor_clave.delete(0,END)

	if usuario == "profesor":
		if clave == "profesor":
			conexion1()
	else:
		conexion1_fallida()




def conexion1():
    global conexion
    conexion = Toplevel(ventana_profesor)
    conexion.title("Exito")
    conexion.geometry("300x50")
    Label(conexion, text="Login finalizado con exito").pack()
    Button(conexion, text="Volver",command=salir_conexion1).pack()

def conexion1_fallida():
    global conexionf
    conexionf = Toplevel(ventana_profesor)
    conexionf.title("ERROR")
    conexionf.geometry("300x50")
    Label(conexionf, text="Usuario o contraseña incorrectos").pack()
    Button(conexionf, text="Volver", command=salir_conexion1_fallida).pack() #EJECUTA "borrar_no_usuario()"


def salir_conexion1():
    conexion.destroy()

def salir_conexion1_fallida():
    conexionf.destroy()


inicio()


