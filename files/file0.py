import os
ruta='files/intro3.txt'
#ruta='files\\intro1.txt'
#ruta='C:\\Users\\usuario\\Dropbox\\sena2023\\Trimestre2-17abril-01julio\\python2693630\\files\\intro2.txt'
#r+t actualiza al inicio
#w+t borra y sobre escribe
#a+ actualiza y lee el stream
try:
    stream=open(ruta,'a+',encoding='utf-8')
    stream.write('\n + ***********')
    print(type(stream.read()))
    stream.close()
except IOError as e:
    print(e)
