#sistema de calificaciones:
calificacion = float(input("Ingrese su calificacion: "))

if (calificacion >= 9 and calificacion <= 10):
    final = "A"
elif (calificacion >= 8 and calificacion < 9):
    final = "B"
elif (calificacion >= 7 and calificacion < 8 ):
    final = "C"
elif (calificacion >= 6 and calificacion < 7 ):
    final = "D"
elif(calificacion >= 0 and calificacion < 6 ):
    final = "F"
else:
    final = "La nota no existe"
print(f"Su calificacion final es {final}")