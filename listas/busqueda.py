import random
lista=[]
cuadrado=[]
tam=random.randint(5,10)
print(tam)
for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista)

dato=5
for i in range(len(lista)):
    if dato == lista[i]:
        print(f'{lista[i]} esta en la posicion {i}')
    # else:
    #     print(f'no esta en la posicion {i}')


