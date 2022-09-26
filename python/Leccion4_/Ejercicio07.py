#Ej 7: Juego divina el numero
#Realizar un juego para adivinar un numero. Para ello se debe
#generar un numero aleatorio entre 1-100, y luego ir pidiendo
#numero idicando si es mayor o menor con respecto a N.
#Termina cuando el usuario acierta y debe mostrar el n de intentos

import random
print('\t.: Juego adivina el número: .')
aleatorio = random.randint(0,100) #recorre de 0 a 100, generamos un num aleatorio
count = 0

while True:
    num = int(input("Digite un numero de 1 a 100: "))
    count += 1
    if num > aleatorio:
        print("\t No es el numero, digite un número menor")
    elif num < aleatorio:
        print("\t No es el numero, digite un número mayor")
    else:
        print(f'FELICIDADES, acabas de adivinar el numero {aleatorio}')
        break #Rompe el ciclo y el bucle
print(f'\n Numero de intentos: {count}')
