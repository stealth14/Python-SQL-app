import pymysql
from tkinter import *
import os
root=Tk()
StringVar()

conn=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='usuarios')

cur=conn.cursor()
cur.execute("SELECT nombre from nombres")
print(cur.description)

global info_usuario

file=open('info_usuario',"w")
for row in cur:    
    info_usuario=(row)
    file.write(StringVar(info_usuario))
    file.write(info_clave)
file.close()
	
cur.close()
conn.close