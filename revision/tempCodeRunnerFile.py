primero=int(input("Digite el primer número: "))
segundo=int(input("Digite el segundo número: "))
while primero==segundo or segundo==primero:
    print("No hay mayor. Intente nuevamente")
    primero=int(input("Digite el primer número: "))
    segundo=int(input("Digite el segundo número: "))
if primero>segundo:
    print("La resta de los número es: ", primero-segundo)
else:
    print("La resta de los número es: ", segundo-primero)