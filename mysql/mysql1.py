import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adso"
)
#print(type(db))


cursor=db.cursor()
cursor.execute('SHOW DATABASES')
#print(type(cursor))
for dbs in cursor:
     print(dbs)

# for n in cursor:
#     print(n)
print('--------------------')
cursor.execute("SHOW TABLES")
for n in cursor:
    print(n)

cursor.execute("""INSERT INTO aprendiz (nombre, documento,formacion,sexo)VALUES ('Reinaldo Rueda','151219','contabilidad','M') """)
db.commit()
cursor.execute('select * from aprendiz')
for ap in cursor:
     print(ap[0])
     print(ap[1])
     print(ap[2])
     print(ap[3])

     #print(type(ap))
     #print(ap[0])


# name="Alirio Suarez"
# doc='909997'
# formacion='adso'
# genero='m'

# query ="INSERT INTO aprendiz (nombre, documento, formacion,sexo) VALUES ('"+ name  +"','"+  doc+"','"+formacion+"','"+genero+"')"
# cursor.execute(query)
# #cursor.commit()

# cursor.execute('select * from aprendiz')
# for ap in cursor:
#     #print(type(ap))
#     print(ap[0])


# query ="INSERT INTO favourite (number, info) VALUES ('"+ variable1  +"','"+  variable2+"')"
# cursor.execute(query)
# conn.commit()


# sql = "INSERT INTO favourite (number, info) VALUES (%s, %s)"
# val = (numbers, animals)
# cursor.execute(sql, val)
# conn.commit()