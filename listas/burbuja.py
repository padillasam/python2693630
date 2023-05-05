import random
lista=[]
cuadrado=[]
tam=random.randint(5,10)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print(lista) 

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista)