## Nombre y edad: Solicita el nombre y la edad de una persona. Muestra su nombre e indica si es mayor de edad.

nombre = input("Hola por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Hola " + nombre + " eres mayor de edad")
else:
    print("Hola " + nombre + " eres menor de edad")