#Funcion
#Definimos una funcion
#mi_funcion()  No se puede llamar antes de definir una funcion
def mi_funcion():
    print('Hola Mundo esto es una funcion')

mi_funcion() #Estamos llamando a la funcion
mi_funcion()

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' '+lastName)
person = ['Martin', 'Ojeda']
show(person[0],person[1]) #Pasamos uno por unos los datos de la lista a la funcion
show(*person) #Esto es lo mismo q lo anterio pero le pasamos todo junto
person2 = ("Martin", "Ojeda") #Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Messi", "name" : "Lionel"}
show(**person3)

numbers = [ 1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para q no se ejecute el else
else:
    print("Esto se termino")

#List comprehesion, lista de comprension
names = ["Jorge", "Pepe", "Rodrigo", "Lupe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)
bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de Argumentos (funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos")
    print(f'Nombre: {name}, Apellido: {lastname}')
mi_funcion2('Gabriel', "Batistuta")
mi_funcion2('Beto', "Acosta")
mi_funcion2('Pitu', "Barrientos")

#La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(78, 22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

def sumar2(a=0, b=0): #Le damos un valor por default
    return a + b
resultado2 = sumar2()
print(f'Resultado de la suma: {resultado2} ')
print(f'El resultado de la suma es: {sumar2(58,45)}')

#Argumento, variables en funciones
def listaNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: #Se va convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'jose', 'Claudia', 'Rosa')
listaNombres('Lucas2', 'jose2', 'Claudia2', 'Rosa2')
