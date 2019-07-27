from tkinter import *
#from pymysql import *
import pymysql
from tabulate import tabulate
    #sql

    #interfaz

master = Tk()

conn='Intefaz de conexion'
cur='Instancia de cursor'

def conexion():
    global conn,cur
    conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='calificaciones')
    cur=conn.cursor(pymysql.cursors.DictCursor)

def query(script):
    global conn,cur

    conexion()

    cur.execute(script)

    conn.commit()

    tabla=cur.fetchall()

    resultados=tabulate(tabla, tablefmt='grid')

    cur.close()

    conn.close
    return resultados

def select():
    script="SELECT nombre_estudiante,apellido_estudiante,nota1,nota2,nota3 from estudiantes,notas where codigo_unicoPK=codigo_unicoFK"
    #almacenado de resultados en un string e insercion en variable de control asignada a label 
    mostrar_resultado(query(script))

def peores():
    script="SELECT nombre_estudiante,apellido_estudiante,promedio FROM estudiantes,notas where codigo_unicoPK=codigo_unicoFK ORDER BY promedio ASC LIMIT 5"
    mostrar_resultado(query(script))

def mejores():
    script="SELECT nombre_estudiante,apellido_estudiante,promedio FROM estudiantes,notas where codigo_unicoPK=codigo_unicoFK ORDER BY promedio DESC LIMIT 5"
    mostrar_resultado(query(script))

def promedios():
    script="SELECT nombre_estudiante,apellido_estudiante,promedio from estudiantes,notas where codigo_unicoPK=codigo_unicoFK"
    mostrar_resultado(query(script))


#checkbox para seleccionar las notas a modificar
def promedio():
    script="SELECT sum(promedio)/count(promedio) from notas"
    mostrar_resultado("Promedio general\n"+query(script))

def total_estudiantes():
    script="SELECT count(codigo_unicoPK) from estudiantes"
    mostrar_resultado("Total estudiantes \n "+query(script))

#SELECCIONADORES DE NOTAS
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
    global var_codigo
    global var_nota

    if   bool_nota1.get() ==1:
        print('nota1 insertada')
        query("UPDATE notas SET nota1 = ' "+var_nota.get()+" ' WHERE codigo_unicoFK = ' "+var_codigo.get())


    if   bool_nota2.get() ==1:
        query( "UPDATE notas SET nota2 = '"+var_nota.get()+"' WHERE codigo_unicoFK = '"+var_codigo.get())
        print('nota2 insertada')


    if   bool_nota3.get() ==1:
        query( "UPDATE notas SET nota3= '"+var_nota.get()+"' WHERE codigo_unicoFK = '"+var_codigo.get() )
        print('nota3 insertada')

    limpiar_campos()


def borrar_nota():
    global bool_nota1,bool_nota2,bool_nota3
    
    if   bool_nota1.get() ==1:
        print('nota1 borrada')
        mostrar_resultado(query())

    if   bool_nota2.get() ==1:
        print('nota2 borrada')

    if   bool_nota3.get() ==1:
        print('nota3 borrada')

def mostrar_resultado(resultados):
    global var_resultados

    var_resultados.set(resultados)
    print('registro encontrado')
def limpiar_campos():
    var_codigo=" "
    var_nota=" "
#controles

var_codigo=StringVar()
var_nota=StringVar()

#nombre
Label(master,text='Codigo unico').grid(row=0,column=1)
nombre=Entry(master,textvariable=var_codigo)
nombre.grid(row=1,column=1)

#nota
Label(master,text='Nota').grid(row=2,column=1)
nota=Entry(master,textvariable=var_nota)
nota.grid(row=3,column=1)

#boton insertar registro 
insert=Button(master,text="Insertar Nota", command=insertar_nota)
insert.grid(row=2,column=2)

#resultados
Label(master,text='Vista previa').grid(row=4,column=1)
var_resultados=StringVar()
lbl_resultados=Label(master,textvariable=var_resultados,height=20,width=30,background='AntiqueWhite2')
lbl_resultados.grid(row=5,column=1)


#boton borrar registro
delete=Button(master,text="Borrar Nota", command=borrar_nota)
delete.grid(row=7,column=1)

# boton peores 10
btn_peores10=Button(master,text="Peores 5", command=peores)
btn_peores10.grid(row=10,column=0)
# boton mejores 10
btn_mejores10=Button(master,text="Mejores 5", command=mejores)
btn_mejores10.grid(row=10,column=2)
# boton promedios individuales
btn_promedio_general=Button(master,text="Prom general",command=promedio)
btn_promedio_general.grid(row=11,column=2)
# boton promedio general del curso
btn_promedios_individuales=Button(master,text="Promedios", command=promedios)
btn_promedios_individuales.grid(row=11,column=0)
# boton total estudiantes
btn_promedios_individuales=Button(master,text="Total estudiantes", command=total_estudiantes)
btn_promedios_individuales.grid(row=11,column=1)

#borrar los campos cuando se deba recoger un dato en especifico como por ejemplo el nombre para usarlo en una consulta


#https://stackoverflow.com/questions/28530508/select-query-in-pymysql

mainloop()