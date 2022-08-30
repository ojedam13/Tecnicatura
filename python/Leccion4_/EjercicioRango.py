#Ejercicio1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
#Ej de ejecucion: 0,3,6,9
print('Ejercicio 1')
for i in range(11):
    if i % 3 == 0:
        print(i)


#Ejercicio2: Crear un rango de 2 a 16 e imprimirlos
#Ej de ejecucion: 2,3,4,5,6
print('Ejercicio 2')
for i in range(2,7):
    print(i)

#Ejercicio : Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#Ejemplo de ejecucion: 3,5,7,9
print('Ejercicio 3')

for i in range(3, 11):
    if i % 2 != 0:
        print(i)