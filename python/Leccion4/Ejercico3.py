'''Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos
y cuantos neutros.'''
x = 1
neutros = 0
positivos = 0
negativos = 0
while x <= 10:
     numero1 = int(input("Ingresar la cantidad de numeros a sumarse: "))
     if numero1 == 0:
         neutros += 1
     else:
         if numero1 > 0:
            positivos += 1
         else:
            negativos += 1
     x+= 1
print(f'Hay {neutros} numero neutros')
print(f'Hay {positivos} numero positivos')
print(f'Hay {negativos} numero negativos')