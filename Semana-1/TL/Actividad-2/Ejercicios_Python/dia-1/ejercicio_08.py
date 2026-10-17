#Calificaciones: Solicita una nota de 0 a 100 e indica si el estudiante está aprobado (70 o más) o reprobado. Valida la nota.

nota = int(input("Por favor, ingresa la nota del estudiante (de 0 a 100): "))

if nota < 70: 
    print("El estudiante esta reprobado")
else:
    print("El estudiante esta aprobado")