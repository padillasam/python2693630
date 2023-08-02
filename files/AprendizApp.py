from Aprendiz import *
import csv
aprendices=[]
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693630.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        #print(row)
        objeto=Aprendiz(row[0],row[1],row[2],row[3])
        print(objeto.verDatos())
        aprendices.append(objeto)
        # print('first name:',row[0])
        # print('last name:',row[1])
        # print('email:',row[2])
        # print('id:',row[3])
for ap in aprendices:
    print(ap.getNombre())