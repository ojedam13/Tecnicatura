#Rj5: Factorial de un num positivo
# Hacer un programa para calcular el factorial de un numero positivo

num = int(input('Digite un numero: '))
while num < 0:
    print('El numero tiene que ser positivo')
    num = int(input('Digite un numero: '))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f'El factorial de {num} es {factorial}')