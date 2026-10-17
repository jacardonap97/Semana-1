#Usuario y contraseña: Solicita un usuario y una contraseña. Compara los datos con valores definidos y permite el acceso si ambos coinciden.

user = "usuario"
passw = "Asd.321+"

userPed = input("Digite el usuario: ")
passwPed = input("Digite la contraseña: ")

if userPed == user and passwPed == passw:
    print("Acceso consedido")
else:
    print("Acceso denegado")