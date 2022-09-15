#Ej 2 : Operaciones de conjuntos con listas
#Escriba un programa q tenga 2 listas y q a contiruacion
#cree las siguientes listas(En la q no deber haber repeticiones)
#1 Lista de palabras q aparecen en las listas
#2 Lista de palabras q aparecen en la priumer lista, pero no en la segunda
#3 Lista de palabras q aparecen en la segunda lista, pero no en la primera
#4 Lista de palabras q aparecen en ambas listas

lista1 = ["Messi", "Di Maria", "Dybala", "Martinez", "Otamendi"]
lista2 = ["Paredes", "De Paul", "Messi", "Otamendi", "Correa"]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
print(union)
primeraLista = list(conjunto1 - conjunto2)
print(primeraLista)
segundaLista = list(conjunto2 - conjunto1)
print(segundaLista)
ambasListas= list(conjunto1 & conjunto2)
print(ambasListas)
