#Sistema de facturación: 
"""
Solicita el nombre del cliente, el producto, su precio y la cantidad. Calcula el subtotal y aplica estos descuentos:

    $500.000 o más: 15 %.
    $200.000 o más: 10 %.
    Menos de $200.000: sin descuento.

Muestra una factura con el subtotal, el descuento y el total a pagar.
"""

nombre  = input("Digite el nombre del cliente: ")
nombreProducto  = input("Digite el nombre del producto: ")
precio  = int(input("Digite el precio del producto: "))
cantidad = int(input("Digite la cantidad: "))

subTotal = precio * cantidad

if subTotal >= 500000:
    desc = subTotal * 0.15
    total = subTotal - desc
    print("****Factura de venta****")
    print("\nUsuario: ", nombre)
    print("Producto                   Cantidad                         Precio")
    print(nombreProducto, "                         ", cantidad, "                         $", precio)
    print("\nSubtotal: $", subTotal)
    print("Descuento del 15%: $", desc)
    print("Total: $", total)
elif subTotal >= 200000:
    desc = subTotal * 0.1
    total = subTotal - desc
    print("****Factura de venta****")
    print("\nUsuario: ", nombre)
    print("Producto                   Cantidad                         Precio")
    print(nombreProducto, "                         ", cantidad, "                         $", precio)
    print("\nSubtotal: $", subTotal)
    print("Descuento del 10%: $", desc)
    print("Total: $", total)
else:
    print("****Factura de venta****")
    print("\nUsuario: ", nombre)
    print("Producto                   Cantidad                         Precio")
    print(nombreProducto, "                         ", cantidad, "                         $", precio)
    print("\nSubtotal: $", subTotal)
    print("Descuento: ", "Sin descuento")
    print("Total: $", subTotal)