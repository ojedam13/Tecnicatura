#Ej 01: Crear una funcion par sumar los valores recibidos de tipo
#numericos, utilizando argumentos variables *args como parametro de la
#funcion y agregar como resultado la suma de todos losvalores pasados
#como argumentos.
#Definimos una funcion
def sumar_valor(*args): #Recibimos una cantidad de parametros indefinidos
    resultado = 0
    #iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

#Llamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))