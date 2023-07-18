try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuupsss...")
except ArithmeticError:
    print("Usssstele")
print("FIN.")

try:
    # for i inrange(10):
    #     print(i)
    raise SyntaxError
except SyntaxError:
    print('Error de sintaxis')

#-------------------------------------
def bad_fun(n):
    try:
        raise
        return n / 0
     
    except RuntimeError:
        print("¡Lo hice otra vez!")
        #raise

bad_fun(0)
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("¡Ya veo!")

print("FIN.")

#------------------------------

import math

try:
    x = float(input("Ingresa un número: "))
    assert x >= 0.0

    x = math.sqrt(x)
except AssertionError:
    print('Fallo del assert')