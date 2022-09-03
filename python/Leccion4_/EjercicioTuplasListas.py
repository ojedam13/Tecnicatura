# Dada la siguiente tupla
tupla = (13,1,6,3,2,5,8)
#crear una lista q solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]
lista = []
for numero in tupla:
    if numero < 5:
        lista.append(numero)
print(lista)

