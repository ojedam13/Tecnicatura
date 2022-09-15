#Ej 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos, por ultimos mostra la lista

lista= [1,2,3,4,5,5,4,3,2,1,0,8,7,9]
lista = list(set(lista)) #conversion a un conjunto(No puede tener elmentos duplicados) y otra vez convertimos a lista
print(lista) 