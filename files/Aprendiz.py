class Aprendiz:
    def __init__(self,nombre,apellido,correo,doc):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        self.__doc=doc
    def verDatos(self):
        return f"{self.__nombre} {self.__apellido} {self.__correo} {self.__doc}"
    def getNombre(self):
        return self.__nombre
