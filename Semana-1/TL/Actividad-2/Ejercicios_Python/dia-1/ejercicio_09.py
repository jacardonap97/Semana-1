#Descuento en compras: 
"""
Solicita el precio de una compra:

    $200.000 o más: 20 % de descuento.
    $100.000 o más: 10 % de descuento.
    Menos de $100.000: sin descuento.

Muestra el total a pagar.
"""

valor = float(input("Digite el valor de la compra: "))

if valor >= 200000:
    desc = valor * 0.2
    total = valor - desc
    print("Usted recibio un descuento del 20% y el total a pagar es: " , total)
elif valor >= 100000:
    desc = valor * 0.1
    total = valor - desc
    print("Usted recibio un descuento del 10% y el total a pagar es: " , total)
else:
    print("Usted no recibio ningun descuento, el total a pagar es: " , valor)