import math #importamos la clase math
# Dada la siguiente tupla
tupla = (13,1,6,3,2,5,8)
#crear una lista q solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]
lista = []
for numero in tupla:
    if numero < 5:
        lista.append(numero)
print(lista)

#Ejercicio matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo:"))

while numero < 0:
    print("Error -> Deberia ser positivo")
    numero = int(input("Digite un numero positivo:"))
print(f'\n Su raiz cuadrada es: {math.sqrt(numero):.2f}') #.2f = a dos numero desp de la coma
