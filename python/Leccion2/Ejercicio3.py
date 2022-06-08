#Calcular estacion del año
mes = int(input("Digite el numero del mes del año: "))
estacion = None
if (mes == 1 or mes == 2 or mes ==3):
    estacion = "Verano"
elif (mes == 4 or mes == 5 or mes ==6):
    estacion = "Otoño"
elif (mes == 7 or mes == 8 or mes ==9):
    estacion = "Invierno"
elif (mes == 10 or mes == 11 or mes ==12):
    estacion = "Primavera"
else:
    estacion = "Estacion desconocida"

print(f"La estacion es {estacion}")
