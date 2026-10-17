#Calculadora básica: Solicita dos números y una operación (+, -, *, /). Muestra el resultado y evita la división entre cero.

num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
operacion = int(input("Elige por favor la operación matematica, 1-Suma, 2-Resta, 3-Multiplicación, 4-Division: "))


if num2 == 0 and operacion == 4:
    print("Esta división no se puede realizar")
else:
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