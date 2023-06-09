from Aprendiz import *
from Curso import *

ob1=Aprendiz('Maria Suarez',123456,'ADSO',2693630)
c1=Curso('Programacion de Software','Tecnico')
c2=Curso('Python','complementario')
ob1.agregarCurso(c1)
ob1.agregarCurso(c2)
print(c1.getNombre())
#print(ob1.getCursos())
for curso in ob1.getCursos():
    print(curso.getNombre())
#del ob1
print(c1)
ob1.componerCurso('Java','Complementario')
for curso in ob1.getCursos():
    print(curso.getNombre())
del ob1
#print(ob1)
#del ob1
