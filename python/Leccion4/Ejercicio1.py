'''Diseñar un programa que ingresando un año nos devuelva por consola
si es un año bisiesto o no, repetir la accion hasta que el usuario lo desida'''
opcion = 1
while opcion == 1:
    anio = int(input("Ingresar un año: "))

    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    opcion = int(input("Para seguir adelante escriba la opcion 1: "))