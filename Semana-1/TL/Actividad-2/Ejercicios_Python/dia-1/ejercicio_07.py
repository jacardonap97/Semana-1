#Mayoría de edad: Solicita la edad de una persona e indica si puede ingresar a un evento para mayores de 18 años. Valida que la edad no sea negativa.

edad = int(input("Por favor, ingresa tu edad: "))

if edad < 0: 
    print("Digitaste una edad negativa y no es valida")
else:
    if edad >= 18:
        print("Hola eres mayor de edad, puedes ingresar")
    else:
        print("Hola eres menor de edad, no puedes ingresar")