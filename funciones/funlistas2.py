import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(5,20)
l2=llenarLista(10,50)
l3=llenarLista(3,1000)
print(l1)
#print(l2)
#print(l3)
print(sumaLista(l1))
print(sumaLista(l2))
print(sumaLista(l3))
print(promedioLista(l1))
print(promedioLista(l2))
print(promedioLista(l3))

print(l1)
def mayor(lista):
    m=0
    for i in lista:
       if i>m:
           m=i
    return m
print('mayor',mayor(l1))

def menor(lista):
    m=1000000
    for i in lista:
     if i<m:
         m=i
    return m
print('menor',menor(l1))     


def retorno():
    for i in range(5):
        #print(10)
        return 10
print(retorno())

