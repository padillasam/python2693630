resul = 0
num1=20
num2=20

while num1 == num2 or num2 == num1:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))

    if num1 > num2:
        resul = num1 - num2
        print (f"El resultado de la resta entre {num1} y {num2} es: {resul}")
    elif num2 > num1:
        resul = num2 - num1
        print (f"El resultado de la resta entre {num2} y {num1} es: {resul}")

    while resul != 0:
        if num1 < num2:
            resul = resul - num1
            print(f"El resultado {resul}")
        else:
            resul = resul - num2
            print(f"El resultado {resul}")     
        if resul <=0:
            print (f"Lo sobrante de la resta es {resul}")
            break
    
incio = int(input("Ingrese el numero de partida: "))
fin = int(input("Ingrese el numero de finalizacion: "))
increment = int(input("Ingrese la cantidad a incrementar o decrementar: "))

n = int(input("ingrese un numero entero postivo: "))

for i in range (incio, fin, increment):
    if i%n==0:
        print(i, "es multiplo de", n)
    else:
        print(i)

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