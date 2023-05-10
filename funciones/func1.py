# METODOS VS FUNCIONES
lista=[11,2,34,4,5]
print(lista)
print(len(lista))
lista.sort()
print(lista)

#INTRODUCCION A LAS FUNCIONES CREADAS POR EL PROGRAMADOR

def saludo(receptor):
    print(f'Hola {receptor}')

saludo('Aprendices')
saludo('soacha')
saludo('Sub director')

def saludar(receptor):
    return f'Hola {receptor}'

print(len(saludar('Aprendices')))
cadena=saludar('soacha')
print(cadena)
print(len(cadena))
cadena='Esto recibo de la funcion'+saludar('subdirector')
print(cadena)
#print(saludar('soacha'))
#print(saludar('Sub director'))

