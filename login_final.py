from tkinter import *
#from pymysql import *
import pymysql
from tabulate import tabulate
master = Tk() 
conn='Intefaz de conexion' 
cur='Instancia de cursor'
def conexion():
    global conn,cur
    conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='calificaciones')
    cur=conn.cursor(pymysql.cursors.DictCursor)
def query(script,variable):
    global conn,cur
    conexion()
    cur.execute(script,(variable))
    conn.commit()
    tabla=cur.fetchall()
    cur.close()
    conn.close
    return tabla
def extraer_celda(tabla,columna):
    fila=tabla[0]
    celda=fila[columna]
    return celda

def verificar():
    global var_nombre,var_clave,conn,cur
    usuario_ingresado=var_nombre.get()
    clave_ingresada=var_clave.get()
    limpiar_campos()
    extraer_clave_bd="SELECT contrasenia_estudiantes FROM estudiantes WHERE nombre_estudiante=%s"
    extraer_usuario_bd="SELECT nombre_estudiante FROM estudiantes WHERE nombre_estudiante =%s"

    tabla=query(extraer_clave_bd,usuario_ingresado)
    clave_bd=extraer_celda(tabla,'contrasenia_estudiantes')

    tabla=query(extraer_usuario_bd,usuario_ingresado)
    usuario_bd=extraer_celda(tabla,'nombre_estudiante')
    
    if clave_bd == clave_ingresada and usuario_bd == usuario_ingresado :

        print("Bienvenido!!")
    else:
        print('Usuario o clave incorrectos')

def verificar_profe():
    global var_nombre,var_clave,conn,cur
    usuario_ingresado=var_nombre.get()
    clave_ingresada=var_clave.get()
    limpiar_campos()
    extraer_clave_bd="SELECT contrasenia_profesor FROM profesor WHERE nombre_profesor=%s"
    extraer_usuario_bd="SELECT nombre_profesor FROM profesor WHERE nombre_profesor=%s"

    tabla=query(extraer_clave_bd,usuario_ingresado)
    clave_bd=extraer_celda(tabla,'contrasenia_profesor')

    tabla=query(extraer_usuario_bd,usuario_ingresado)
    usuario_bd=extraer_celda(tabla,'nombre_profesor')
    
    if clave_bd == clave_ingresada and usuario_bd == usuario_ingresado :

        print("Bienvenido!!")
    else:
        print('Usuario o clave incorrectos')

def limpiar_campos():
    global txt_nombre,txt_nombre
    txt_nombre.delete(0, END)
    txt_clave.delete(0, END)
#interfaz
var_nombre=StringVar()
var_clave=StringVar()
#entry nombre
Label(master,text='Nombre').grid(row=0,column=1)
txt_nombre=Entry(master,textvariable=var_nombre)
txt_nombre.grid(row=1,column=1)

#entry clave
Label(master,text='Clave').grid(row=2,column=1)
txt_clave=Entry(master,textvariable=var_clave)
txt_clave.grid(row=3,column=1)
#ingreso maestro
btn_ingreso_profe=Button(master,text="Ingresar profesor",command=verificar_profe)
btn_ingreso_profe.grid(row=4,column=1)
#ingreso alumno
btn_ingreso_alumno=Button(master,text="Ingresar alumno",command=verificar)
btn_ingreso_alumno.grid(row=5,column=1)
master.mainloop()