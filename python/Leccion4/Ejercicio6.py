'''Ingresar "N" enteros, visualizar la suma de los numero pares
de la lista, cuantos numeros pares existen y cual es el promedio
de los numero impares'''

elementos = int(input("Digite cantidad de elementos a ingresar: "))
i = 1
suma_pares=0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

while i <= elementos:
    num = int(input("digite un numero: "))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1
    i += 1

if conteo_pares != 0:
    print(f'''La suma de los numeros pares es: {suma_pares}''')
    print(f'''El conteo de los numeros pares es: {conteo_pares}''')
else:
    print("No se han digitado numeros pares")
if conteo_impares == 0:
    print("No se han digitado numeros impares")
else:
    promedio_impares = suma_impares/conteo_impares
    print(f"El promedio de impares es {promedio_impares}")
