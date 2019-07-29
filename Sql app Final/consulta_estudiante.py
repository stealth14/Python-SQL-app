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

    resultados=tabulate(tabla, tablefmt='simple')

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

#gestionar estado de checkbuttons 

def mostrar_resultado(resultados):
    global var_resultados

    var_resultados.set(resultados)
    print('registro encontrado')

def limpiar_campos():
    var_codigo=" "
    var_nota=" "

def estado_registros():
    script_estado_actual="SELECT codigo_unicoPK,nombre_estudiante,apellido_estudiante,nota1,nota2,nota3,promedio FROM estudiantes,notas WHERE codigo_unicoPK=codigo_unicoFK"

    mostrar_resultado("Estado actual\n"+query(script_estado_actual))
#controles

var_codigo=StringVar()
var_nota=StringVar()

#resultados
Label(master,text='Vista previa').grid(row=4,column=1)
var_resultados=StringVar()
lbl_resultados=Label(master,textvariable=var_resultados,height=20,width=30,background='AntiqueWhite2')
lbl_resultados.grid(row=5,column=1)

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

# boton total estudiantes
btn_promedios_individuales=Button(master,text="Estado actual", command=estado_registros)
btn_promedios_individuales.grid(row=1,column=0)

#borrar los campos cuando se deba recoger un dato en especifico como por ejemplo el nombre para usarlo en una consulta


#https://stackoverflow.com/questions/28530508/select-query-in-pymysql

mainloop()