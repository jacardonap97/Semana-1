"""
nombre = input("Dime tu nombre, por favor: ")
apellido = input("Dime tu apellido, por favor: ")
correo = input("Dime tu correo, por favor: ")

print ("\nSeñor/a " + nombre + " " + apellido + " su correo es: " + correo)
"""
"""
print("\nHagamos una operación matematica")
operacion = input("Elige por favor la operación matematica, +, -, *, /: ")
numero1 = input("Deme un número por favor: ")
numero2 = input("Deme otro número por favor: ")


print("\nEl resultado de la operación es: " , eval(numero1 + operacion + numero2))
"""

"""
respuesta = "s"
while respuesta != "n":

    operacion = int(input("Elige por favor la operación matematica, 1-Suma, 2-Resta, 3-Multiplicación, 4-Division: "))
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))


    if operacion == 1:
        print("El resultado de l operación es: " , (num1 + num2))
    elif operacion == 2:
        print("El resultado de l operación es: " , (num1 - num2))
    elif operacion == 3:
        print("El resultado de l operación es: " , (num1 * num2))
    elif operacion == 4:
        print("El resultado de l operación es: " , (num1 / num2))
    else : 
        print("Opción incorrecta")

    respuesta = input("\n¿Deseas continuar? s/n: ")

print("\nFin de ejecución")
"""

while True:

    operacion = int(input("Elige por favor la operación matematica, 1-Suma, 2-Resta, 3-Multiplicación, 4-Division: "))
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))


    if operacion == 1:
        print("El resultado de l operación es: " , (num1 + num2))
    elif operacion == 2:
        print("El resultado de l operación es: " , (num1 - num2))
    elif operacion == 3:
        print("El resultado de l operación es: " , (num1 * num2))
    elif operacion == 4:
        print("El resultado de l operación es: " , (num1 / num2))
    else : 
        print("Opción incorrecta")

    continuar = input("\n¿Deseas continuar? s/n: ")
    if continuar == "s":
        continue
    else:
        break

print("\nFin de ejecución")
