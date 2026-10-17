#Calculadora con menú: Crea un menú con las opciones de sumar, restar, multiplicar y dividir. Ejecuta la operación seleccionada y muestra el resultado.

print("******Elige por favor la operación matemática******")
print("\n1-Suma \n2-Resta \n3-Multiplicación \n4-Division")
operacion = int(input("Opción: "))

print("\n******Digita los números a operar******")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))


if num2 == 0 and operacion == 4:
    print("Esta división no se puede realizar")
else:
    if operacion == 1:
        print("\nEl resultado de l operación es: " , (num1 + num2))
    elif operacion == 2:
        print("\nEl resultado de l operación es: " , (num1 - num2))
    elif operacion == 3:
        print("\nEl resultado de l operación es: " , (num1 * num2))
    elif operacion == 4:
        print("\nEl resultado de l operación es: " , (num1 / num2))
    else : 
        print("\nOpción incorrecta")