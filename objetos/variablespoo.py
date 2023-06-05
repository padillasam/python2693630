class Prueba:
    contador=0
    def __init__(self,var1=1):
        self.__var1=var1
        Prueba.contador+=1

    def otroAtributo(self,var2):
        self.__var2=var2
    # def getvar1(self):
    #     return self.__var1

    # def getContador(self):
    #     return Prueba.contador
    
    
ob1=Prueba()
print(ob1.contador)
ob2=Prueba()
ob2.otroAtributo(2)
print(ob2.contador)
ob3=Prueba()
ob3.otroAtributo(3)
ob3.var3=100
ob3.__var2=32
print(ob3.contador)
#print(ob1.getvar1())
print(ob1.__dict__)
print(ob2.__dict__)
print(ob3.__dict__)
print(Prueba.__dict__)
