#Positivo o negativo: Solicita un número e indica si es positivo, negativo o cero.

num = int(input("Por favor digita un número: "))

if num == 0:
    print("El número es cero")
elif num > 0: 
    print("El número es positivo")
else:
    print("El número es negativo")