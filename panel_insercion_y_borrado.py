from tkinter import *
#from pymysql import *
import pymysql
from tabulate import tabulate
    #sql

    #interfaz

master = Tk()

def select():
    global var_resultados
    conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='calificaciones')
    cur=conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("SELECT nombre_estudiante,apellido_estudiante,nota1,nota2,nota3 from estudiantes,notas where codigo_unicoPK=codigo_unicoFK")

    conn.commit()

    tabla=cur.fetchall()

    linea=tabulate(tabla, tablefmt='grid') 


    #almacenado de resultados en un string e insercion en variable de control asignada a label 
    var_resultados.set(linea)

    cur.close()

    conn.close


#checkbox para seleccionar las notas a modificar

global bool_nota1,bool_nota2,bool_nota3

bool_nota1 = IntVar()

bool_nota2 = IntVar()

bool_nota3 = IntVar()

c = Checkbutton(master, text="Nota1", variable=bool_nota1)
c.grid(row=9,column=0)

d = Checkbutton(master, text="Nota2", variable=bool_nota2)
d.grid(row=9,column=1)

e = Checkbutton(master, text="Nota3", variable=bool_nota3)
e.grid(row=9,column=2)


    #gestionar estado de checkbuttons 

def insertar_nota():
    global bool_nota1,bool_nota2,bool_nota3

    if   bool_nota1.get() ==1:
        print('nota1 insertada')

    if   bool_nota2.get() ==1:
        print('nota2 insertada')

    if   bool_nota3.get() ==1:
        print('nota3 insertada')

def borrar_nota():

    print('nota borrada')

def mostrar_resultado():
    select()
    print('buscar registro')

#controles


#nombre
Label(master,text='Nombre').grid(row=0,column=1)
nombre=Entry(master)
nombre.grid(row=1,column=1)

#nota
Label(master,text='Nota').grid(row=2,column=1)
nota=Entry(master)
nota.grid(row=3,column=1)

#boton insertar registro 
insert=Button(master,text="Insertar Nota", command=insertar_nota)
insert.grid(row=6,column=1)

#resultados
Label(master,text='Vista previa').grid(row=4,column=1)
var_resultados=StringVar()
resultados=Label(master,textvariable=var_resultados,height=10,background='AntiqueWhite2')
resultados.grid(row=5,column=1)


#boton borrar registro
delete=Button(master,text="Borrar Nota", command=borrar_nota)
delete.grid(row=7,column=1)

# boton buscar registro
ver=Button(master,text="Buscar registro", command=mostrar_resultado)
ver.grid(row=8,column=1)


#boton mejores 10
global mejores,peores,promedio_individual,promedio_general,total_estudiantes
mejores="SELECT nombre_estudiante,apellido_estudiante,nota1,nota2,nota3 from estudiantes,notas where codigo_unicoPK=codigo_unicoFK and "

def query(script):
    global var_resultados
    conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='calificaciones')
    cur=conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("SELECT nombre_estudiante,apellido_estudiante,nota1,nota2,nota3 from estudiantes,notas where codigo_unicoPK=codigo_unicoFK")

    conn.commit()

    tabla=cur.fetchall()

    linea=tabulate(tabla, tablefmt='grid') 


    #almacenado de resultados en un string e insercion en variable de control asignada a label 
    var_resultados.set(linea)

    cur.close()

    conn.close
#boton peores 10
#boton promedios individuales
#boton promedio general del curso
#boton total estudiantes

#borrar los campos cuando se deba recoger un dato en especifico como por ejemplo el nombre para usarlo en una consulta



#https://stackoverflow.com/questions/28530508/select-query-in-pymysql

mainloop()