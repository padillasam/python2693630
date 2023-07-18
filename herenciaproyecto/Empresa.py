from Usuario import *
from Oferta import *
class Empresa(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__ofertas=[]
    def RealizarOferta(self,nombre):
        pass
        
