#Ej 4: Sumar numero pares dentro de un rango
#Hacer un programa para sumar numeros pares dentro
#de un rango

a = int(input('Digite de donde va a comenzar la suma: '))
b = int(input('Digite el numero hasta donde quiere llegar a sumar: '))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0:
        suma += i
print(f'\n La suma de números pares dentro del rango es: {suma}')