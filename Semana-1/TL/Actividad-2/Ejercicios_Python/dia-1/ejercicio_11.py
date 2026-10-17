#Temperatura: 
"""
Solicita una temperatura y clasifícala:

    Menos de 10 °C: frío.
    De 10 a menos de 25 °C: templado.
    De 25 a menos de 35 °C: caluroso.
    35 °C o más: muy caluroso.
"""

temp = float(input("Digite la temperatura: "))

if temp < 10:
    print("Frío")
elif temp >= 10 and temp < 25:
    print("Templado")
elif temp >= 25 and temp < 35:
    print("Caluroso")
else:
    print("Muy caluroso")