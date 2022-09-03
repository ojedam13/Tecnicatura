# Listas = Ariel, Liliana, Natalia, Osvaldo
# Listas son mutables se pueden modificar
'''
#Las lista es lo q se conoce como arreglos o vectores en otros lenguajes

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
nombre.append([1,2,3])
nombre.append(True)
nombre.append(10.45)
nombre.append(7)
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

#Tuplas son inmutables no se pueden modificar
cocina = ('cuchara', 'cuchillo','tenedor')
print(cocina)
print(len(cocina))

#Acceder a un elemento
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])

#acceder a un rango
print(cocina[0:1])

#ejemplo
verduras = ('papa',) #una tupla necesita aunqsea de un elemento: la coma

#recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar,end=' ')

cocinaLista = list(cocina)
cocinaLista[0]='plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina

#tipo set (conjuntos) No tienen indice van de manera aleatoria
planetas = {'Marte','Jupiter','Venus'}
print(planetas)
print(len(planetas))

#Revisar si un elemento existe dentro de set(Devuelve True o False)
print('Marte' in planetas) #True
print('Tierra' in planetas) #False
print('Tierra' not in planetas) #True

#Agregar elementos
planetas.add('Tierra')
print(planetas)

#Eliminar elementos, error si el elemento no existe
planetas.remove('Marte')#da error si no existe la palabra
print(planetas)
planetas.discard('tierra') #no da error si no existe la palabra
print(planetas)

#limpiar nuestro set o conjunto
planetas.clear()
print(planetas)

#eliminar set
del planetas
print(planetas


#'Maradona': 10 Un diccionario esta compuesto por dos elementos Llave y valor
#dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion orientada a objetos',
    'SABD': 'Sistema de administracion de Base de Datos'
}
#Verificar la cantidad de elementos
print(diccionario)
print(len(diccionario))

#acceder a un diccionario
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('POO'))

#modificar elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#recorrer elementos
for termino in diccionario:
    print(termino)

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario) #devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
print(diccionario)

#Concatenamos listas
lista1 = [1,2,3]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7,8,9])
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado

#cuantos valores estan repetidos adentro de la lista
print(lista3.count(1))

#poner lista al reves
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

#Metodos de ordenamiento
lista.sort() #Ordena ascendentemente
print(lista)
lista.sort(reverse=True) #Ordena desc
print(lista)

tupla = (4, 'Hola', 6.75 , [1,2,3], 4, 'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)
#Lo q podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

#Repaso de set o conjunto
conjunto = set()
conjunto1 = {'bye',}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto1.add(9)
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 No esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto == conjunto1) #Devuelve un valor boolean

#Operaciones en conjuntos
conjunto3 = conjunto | conjunto1 # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto & conjunto1 #Elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto - conjunto1 #asigna el valor q esta en el conjunto y no en el conjunto1
print(conjunto3)

conjunto3 = conjunto ^ conjunto1 #Elemento tienen son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto | conjunto1
print(conjunto.issubset(conjunto3)) # si un conjunto es un subconjunto dentro del otro
print(conjunto3.issuperset(conjunto)) #si un conjunto es un superconjunto del otro

#como saber si ambos conjuntos son disconexos, esto es si comparten elementos comun
print(conjunto.isdisjoint(conjunto1))

#convertir un conjunto totalmente en inmutable
conjunto = frozenset #no se peude agregar, modificar ni eliminar elementos del conjunto

#Repaso diccionario
diccionarioNuevo = {'Azul': 'blue', 'Rojo':'Red', 'amarillo': 'yellow','verde':'green'}
print(diccionarioNuevo)

#Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2= {'Ariel': {'edad': 40, 'Alura':1.64},'Osvaldo':[45,1.85],'Natalia':[35,1.68]}
print(diccionario2)

seleccionArg = {
    10: {'Nombre':'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion':'Extremo Derecho'},
    11: {'Nombre':'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion':'Extermo Derecho'},
    21: {'Nombre':'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion':'Media Punta'},
    19: {'Nombre':'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion':'Defensor Central'},
    1: {'Nombre':'Emiliano Martinez', 'Edad': 28, 'Altura': 1.90, 'Precio': '30 millones', 'Posicion':'Portero'}
}
print(seleccionArg[10])
print(seleccionArg.values())
for llave,valor in seleccionArg.items():
    print(llave, valor)
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end="")
print(len(seleccionArg))
seleccionArg[5] = {'Nombre':'Leandro Paredes', 'Edad': 27, 'Altura': 1.76, 'Precio': '29 millones', 'Posicion':'Mediocampista Central'}
seleccionArg[7] = {'Nombre':'Rodrigo De Paul', 'Edad': 26, 'Altura': 1.77, 'Precio': '25 millones', 'Posicion':'Mediocampista Ofensivo'}
seleccionArg[22] = {'Nombre':'Lautaro Martinez', 'Edad': 24, 'Altura': 1.72, 'Precio': '50 millones', 'Posicion':'Delantero Centro'}
seleccionArg[8] = {'Nombre':'Huevo Acuña', 'Edad': 26, 'Altura': 1.75, 'Precio': '32 millones', 'Posicion':'Lateral Izquierdo'}
print(seleccionArg)
print(len(seleccionArg))
'''

#Pilas usando listas
pila = [1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacar elemetnos desde el final
elementoBorrado = pila.pop() #Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

#Colas con listas
#Estructura de datos tipos fifo(Fist input / fist output)
cola= ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#scamos elementos de la cola
seRetira = cola.pop(0)
print(f'Antendido {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Antendido {seRetira}')
print(cola)