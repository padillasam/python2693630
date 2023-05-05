import random
lista=[]
cuadrado=[]
tam=random.randint(5,10)
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

#in - not in

# for i in range(tam):
#     print(lista[i])

# for dato in lista:
#     print()
    
if 10 not in lista:
    print('si esta')
else:
    print('no esta')