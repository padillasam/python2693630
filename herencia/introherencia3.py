class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."

class Sub(Super):
    def __init__(self, name,apellido):
        Super.__init__(self, name)
        self.__apellido=apellido

    def __str__(self):
         return super().__str__()+' '+self.__apellido
    
#obj = Sub("Andy")    
obj = Sub("Andy","Stallman")

print(obj)