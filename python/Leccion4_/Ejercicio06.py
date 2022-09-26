#Ej6: Tabla de multiplicar
#Hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ej:
# si digita 5 : 5, 10 ,15,20,25,30,35...,50

num = int(input("Digite un numero: "))
lista=[] #Lista vacia

for i in range(1,11):
    lista.append(i*num)

print(f'\n Tabla de multiplicar del {num}: \n {lista}')
indice=1
for indice,i in enumerate(lista):
    print(f'{num} x {indice+1} = {lista[indice]}')