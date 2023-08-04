class Aprendiz:
    def __init__(self,nombre,doc,formacion,sexo):
        self.__nombre=nombre
        self.__doc=doc
        self.__formacion=formacion
        self.__sexo=sexo
        
    def verDatos(self):
        return f"{self.__nombre} {self.__doc} {self.__formacion} {self.__sexo} "
    
    def getNombre(self):
        return self.__nombre
