import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adso"
)
print(type(db))
cursor=db.cursor()
# cursor.execute("SHOW DATABASES")
# print(cursor)
# for dbs in cursor:
#     print(dbs)

cursor.execute("SHOW TABLES")
print(cursor)
for dbs in cursor:
    print(dbs)

# cursor.execute("SELECT * FROM aprendiz")
# for ap in cursor:
#     print(ap)

# cursor.execute("""INSERT INTO aprendiz (nombre, documento,formacion,sexo)VALUES ('Sebastiana Simbaqueba','54761154','redes','F') """)
#db.commit()

name="Ronald Suarez"
doc='909404'
formacion='cosmetologia'
genero='m'

# query ="INSERT INTO aprendiz (nombre, documento, formacion,sexo) VALUES ('"+ name  +"','"+  doc+"','"+formacion+"','"+genero+"')"
# cursor.execute(query)
# db.commit()

cursor.execute("SELECT * FROM aprendiz")
for ap in cursor:
    print(ap[0])



