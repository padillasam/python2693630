#Alcance o SCOPE
num=1000

def saludo(receptor):
    num2=1000000
    #print(f'Hola {receptor}')
    return f'Hola {receptor} tome {num2}'
        
print(saludo('Juan'))

def saludar(fn, ln='Luna'):
    return f'Hola {fn} hijo del sr {ln} tome {num}'

print(saludar('Pedro'))