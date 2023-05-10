import random
tam=random.randint(5,10)
lista = [random.randrange(100) for i in range(tam)]
lista2=[i/2 for i in lista]
print(lista)
#print(lista2)
par=[x for x in lista if x%2==0]
print(par)
parimpar=[0 if x%2==0 else x for x in lista]
print(parimpar)
parimpar2=['par' if x%2==0 else 'impar' if x%2!=0 else 'cero' for x in lista]
print(parimpar2)