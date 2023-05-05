#x,y,z=1,2,3
import random
lista=[]
cuadrado=[]
tam=random.randint(5,10)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

# 3,1,7,2
for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            lista[i],lista[j]=lista[j],lista[i]

print(lista)