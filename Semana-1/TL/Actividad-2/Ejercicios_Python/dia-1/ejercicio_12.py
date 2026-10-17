#Tipo de triángulo: Solicita los tres lados de un triángulo. Comprueba si es válido y clasifícalo como equilátero, isósceles o escaleno.

lado1 = float(input("Digite el primer lado del triangulo: "))
lado2 = float(input("Digite el segundo lado del triangulo: "))
lado3 = float(input("Digite el tercer lado del triangulo: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if lado1 == lado2 == lado3:
        print("Es un triangulo equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Es un triangulo isósceles")
    else: 
        print("Es un triangulo escaleno")
else:
    print("Error, digito algún valor incorrecto")