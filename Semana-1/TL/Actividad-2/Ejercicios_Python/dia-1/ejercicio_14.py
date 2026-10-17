#Cajero automático: 
"""
Crea un cajero con un saldo inicial de $500.000 y estas opciones:

    Consultar saldo.
    Retirar dinero.
    Depositar dinero.
    Salir.

Valida las operaciones y actualiza el saldo.
"""

saldoInicial = 500000
opcion = 0

while opcion != 4:

    print("\n\n***Bienvenido a cajerin***")
    print("\n***Por favor elige una opción***")
    print("\n1-Consultar saldo \n2-Retirar dinero \n3-Depositar dinero \n4-Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldoInicial)
    elif opcion == 2:
        retiro = float(input("\n¿Cuánto dinero desea retirar?: $"))
        saldoInicial -= retiro
        print("\nSeñor usuario, usted retiro $", retiro, "\nSu saldo actual es: $", saldoInicial)
    elif opcion == 3:
        deposito = float(input("\n¿Cuánto dinero desea depositar?: $"))
        saldoInicial += deposito
        print("\nSeñor usuario, usted deposito: $",deposito, "\nSu saldo actual es: $", saldoInicial)
    elif opcion == 4:
        break
    else:
        print("\nOpción elegida no valida")

print("\nGracias por usar nuestros servicios ¡Hasta pronto!")
