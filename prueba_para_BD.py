import pymysql 

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='SISTEMA2')

cur = conn.cursor()

cur.execute("INSERT INTO estudiantes(Nombre, Edad, nota1, nota2, nota3) VALUES ('Franklin', 21,2,8,7)")

select = 'SELECT Nombre, AVG(nota1) as promedio_nota1 FROM estudiantes group by Nombre'

cur.execute(select)

conn.commit()

print(cur.description,"\n\n")

for row in cur:
    print(row)

cur.close()
conn.close()