import random
#tam=random.randint(5,10)
lista = [random.randrange(100) for i in range(10)]
print(lista)
l1=lista[:5]
print(l1)
l2=lista[5:9]
print(l2)
l3=lista[5:-1]
print(l3)
l4=lista[-1:1]
print(l4)