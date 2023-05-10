import random
tam=random.randint(5,10)
lista = [random.randint(-10,10) for i in range(tam)]
print(lista)
signos=['positivo' if x>0 
        else 'negativo' 
        if x<0 else 'cero' 
        for x in lista]
print(signos)