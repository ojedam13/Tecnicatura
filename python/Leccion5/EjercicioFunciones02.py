# Ej 2: Funcion con *args par multiplicar
#Crear una funcion para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos

#Definimos la función par multiplicar
def multiplicarValores(*numeros): # El mas utilizados es *args
    result = 1 # El cero no nos ayuda a multiplicar
    for numero in numeros:
        result *= numero
    return result

#Llamamos a la funcion
print(multiplicarValores(3, 5, 15, 3)) # Pasamos los argumentos