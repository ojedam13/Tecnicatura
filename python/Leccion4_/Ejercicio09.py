#Ej 9: Mostrar uuna frase sin espacion y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, sel e
#devolvera la misma frase pero sin espacios y ademas un contador
# de cuantos caracteres tiene

frase1 = input("Escriba una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N° de caracteres: {len(frase1)}')