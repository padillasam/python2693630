class Empleador:
    suma = 0
    contador = 0
    def __init__(self,nombre,cargo,salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        Empleador.suma = Empleador.suma + self.__salario 
        Empleador.contador = Empleador.contador + 1
        
    def getNombre (self):
        return f"{self.__nombre}"
    
    def getCargo (self):
        return f"{self.__cargo}"
    
    def getSalario (self):
        return f"{self.__salario}"
    
    def calculoHoras (self):
        a = self.__salario // 30
        resultado = a // 8
        return f"El salario que se gana {self.__nombre} por hora es: ${resultado}"
    
    def recibeIncrement (self):
        if self.__salario <= 1160000:
            ipc = self.__salario * 16.12 / 100
            self.__salario = self.__salario + ipc
        else:
            ipc = self.__salario * 13.12 / 100
            self.__salario = self.__salario + ipc
        return f"El salario de {self.__nombre} con ipc es de: ${round (self.__salario)}"
    
    def extrasTotal (self,horas):
        if horas <= 40:
            resultado = horas * 4833
            self.__salario = self.__salario + resultado
            Empleador.suma = Empleador.suma + resultado 
            return f"El salario de {self.__nombre} con horas extras es de: ${round (self.__salario)}"
        else:
            return f"El salario que acaba de ingresar como horas extras no es valido"
        
    def getSuma (self):
        return f"La suma de todos los salarios es de: ${Empleador.suma}"
        
    def getPromedio (self):
        promedio = Empleador.suma / Empleador.contador
        return f"El promedio de todos los salarios es: {promedio}"
    

a = Empleador("Sebas","Profesor", 1160000)
print(a.getSalario())
print(a.extrasTotal(1))
print(a.getSalario())
b = Empleador("Andres","Doctor", 2000000)
print(b.getSuma())


# b = Empleador("Andres","Doctor", 2000000)
# c=Empleador("Fulano", "De tal",10000000)
# print(a.getNombre())
# print(a.getCargo())
# print(a.getSalario())
# print(a.calculoHoras())
# print(a.recibeIncrement())
# print(a.extrasTotal(2))
# print(a.getSuma())
# print(a.getPromedio())