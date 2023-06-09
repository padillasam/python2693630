class Curso:
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.__tipo=tipo
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getNombre(self):
        return self.__nombre