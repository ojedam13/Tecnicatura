#Ciclo while (mientras o durante)
""""
condicion = True
while condicion:
    print("Ejecutando el ciclo while")
else:
    print("Fin del ciclo while")
contador = 0

while contador < 78:
    print("Ejecutamos nuestro ciclo while ", contador)
    contador += 1
else:
    print("Fin del ciclo while")

contador = 5
minimo = 1

while contador >= minimo:
    print(contador)
    contador -= 1

#Ciclo for (ciclo para- hasta que)

cadena = "Hello"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")


#Palabra break: El break rompe cualquier tipo de estructura al encontrar el elemento
#y sigue ejecutando el siguente codigo
for letra in "Argentina":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
else:
    print("Fin del ciclo")

# Palabra continue
for i in range(7): # el rango recorre 7 elementos {0 1 2 3 4 5 6}
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(7):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}")
"""
