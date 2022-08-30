'''Calcular la suma de "N" primeros numeros'''

num1 = int(input("Ingresar la cantidad de numeros a sumarse: "))

for i in range(1, num1):
    num1 += i
print(f"La suma es {num1}")