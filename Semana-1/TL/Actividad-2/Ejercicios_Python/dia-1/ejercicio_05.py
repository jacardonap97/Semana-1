#Número mayor: Solicita dos números e indica cuál es mayor o si son iguales.

num1 = int(input("Por favor digita el primer número: "))
num2 = int(input("Por favor digita el segundo número: "))

if num1 == num2:
    print("Los números son iguales")
elif num1 > num2:
    print("El número " , num1 , " es mayor que " , num2)
else:
    print("El número " , num1 , " es menor que " , num2)