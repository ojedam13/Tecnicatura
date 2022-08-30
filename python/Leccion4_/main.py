# Listas = Ariel, Liliana, Natalia, Osvaldo
nombres = ["Naty", "Messi", "roman", "Ariel"]
print(nombres)
#de manera individual
print(nombres[0])
print(nombres[1:3]) #solo muestra el indice 1 ,2 pero no el 3
print(nombres[ :3]) #muestra desde 0 a 3
print(nombres[-1]) #muestr el primero desde atras
print(nombres[1: ]) #muestra desde el 1 hasta el final

#modificamos un valor
nombres[2] = "Lili"
print(nombres)

#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos")

#Preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

#Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

#insertar un elemetno en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)

#eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

#eliminar el ultimo eleento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[2] #del significa delete
print(nombres)

#eliminar todos los elementos
nombres.clear()
print(nombres)

#eliminar lista
del nombres
print(nombres)
