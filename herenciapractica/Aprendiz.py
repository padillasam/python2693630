from Persona import *
from Curso import *
class Aprendiz(Persona):
    def __init__(self, nombre,documento,programa,ficha):
        super().__init__(nombre, documento)
        self.__programa=programa
        self.__ficha=ficha
        self.__cursos=[]
        
    def agregarCurso(self,curso):
        self.__cursos.append(curso)
    
    def componerCurso(self,nombre,tipo):
        cursito=Curso(nombre,tipo)
        self.__cursos.append(cursito)
        
    def getCursos(self):
        return self.__cursos
        # for curso in self.__cursos:
        #     print(curso.getNombre())

# lista=[1,2,3]
# print(lista)