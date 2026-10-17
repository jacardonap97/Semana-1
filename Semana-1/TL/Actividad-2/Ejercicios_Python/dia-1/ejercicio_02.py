#Suma y resta: Solicita dos números, calcula su suma y resta. Indica si la suma es mayor que 10.}

num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segudo número: "))

sum = num1 + num2
res = num1 - num2

if sum > 10:
    print("La suma es mayor a 10")
else:
    print("La suma es menor o igual 10")
