import mysql.connector
from Aprendiz import *

listaAprendices=[]
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adso"
)
print(type(db))
cursor=db.cursor()

cursor.execute('select * from aprendiz')
for ap in cursor:
    ob=Aprendiz(ap[0],ap[1],ap[2],ap[3])
    listaAprendices.append(ob)

for ap in listaAprendices:
    print(ap.getNombre())
