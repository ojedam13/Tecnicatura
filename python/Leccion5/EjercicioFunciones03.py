#Ej 3: Funcion recursiva
# Imprimir numero de 5 a 1 de manera descentedente usando funciones recursivas
# puede ser cualquier valor positivo, por ej, si pasamos el 5, debe imprimir: 5 4 3 2 1
#Si se ingresa numero neg no imprime nada

def imprimir_num_recursivos(numero):
    if numero >= 1: #Caso base
        print(numero)
        imprimir_num_recursivos(numero-1) #Caso recursivo
    elif numero ==0:
        return
    elif numero <= 0:
        print('No ingreso un numero positivo')
numR = int(input('Digite un numero positivo: '))
resultado = imprimir_num_recursivos(numR)
print(resultado)

#imprimir_num_recursivos(5)
#imprimir_num_recursivos(-5)