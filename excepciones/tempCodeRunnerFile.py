import math

try:
    x = float(input("Ingresa un número: "))
    assert x >= 0.0

    x = math.sqrt(x)
except AssertionError:
    print('Fallo del assert')