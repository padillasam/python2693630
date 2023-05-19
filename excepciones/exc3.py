try:
    short_list = [1]
    one_value = short_list[0.5]
except TypeError:
    print('La embarro')

try:
    short_list = [1]
    t=(1,)
    t.append(100)
    short_list.append(2)
    short_list.depend(3)
except AttributeError:
    print('Error de atributos')

try:
    raise SyntaxError
except SyntaxError:
    print('Error de código')
except:
    print('otro error')
    
try:    
    temperature = float(input('Ingresa la temperatura actual:'))
    if temperature > 0:
        print("Por encima de cero")
    elif temperature < 0:
        prin("Por debajo de cero")
    else:
        print("Cero")
except SyntaxError:
    print('Escriba bien!!!')