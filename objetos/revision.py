class Persona:
    def __init__(self, nombre, documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre 

    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento=documento
    
    def getCursos(self):
        return self.__cursos
    def setCursos(self,cursos):
        self.__cursos=cursos
    
    def agregarCursos(self,curso):
        #curso=input("Ingrese el nombre del curso:")
        self.__cursos.append(curso)
       # return curso
        
    def getDatos(self):
        return self.__cursos


#p=Persona('Ana', 53031992, [Persona.agregarCursos])
p=Persona('Ana', 53031992)
print(p.getNombre ())
p.agregarCursos('python')
p.agregarCursos('java')
print(p.getDatos())