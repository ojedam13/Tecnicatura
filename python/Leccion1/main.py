'''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)

a ="Hola mundo"
print(type(a))

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f"El resultado de la suma es: {suma}")
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El rdo de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El rtdo de la division es: {division}")

division2= operandoA // operandoB
print(f"el rdo de la division (int) es: {division2}")

modulo = operandoA % operandoB
print(f"el modulo es: {modulo}")

exponente = operandoA ** operandoB
print(f"el resultado del exponente es: {exponente}")

#Procesar la entrada del usuario
#funcion input
resultado = input("Escriba un numero: ") #Regrasa dato tipo String
print(resultado)

#Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado= numero1 + numero2
print("El resultado de la suma es: ", resultado)

#Califica tu dia
dia = int(input("¿Como estuvo tu dia ( 1 al 10)?"))
print("Mi dia estuvo de", dia)

#Informacion acerca del libro
titulo = input("Escriba el nombre del libro: ")
autor = input("Escriba el autor del libro: ")

print("El titulo del libro es: ", titulo)
print("El autor del libro es: ", autor)

alto = int(input("Escribe el alto del rectangulo: "))
ancho = int(input("Escribe el ancho del rectangulo: "))
area = alto * ancho
print(f"El área del rectangulo es: {area}")
perimetro = (alto + ancho) * 2
print(f"El perimetro del reactangulo es: {perimetro}")


miVariable3 = 10
print(miVariable3)
#operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 +=1
print(miVariable3)

miVariable3 -=2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 /= 2
print(miVariable3)

#operadores de comparacion
d = 4
b = 2

resultado = d == b #comprobamos si es igual
print(resultado)

#operador diferente
resultado = d != b #comprobamos si es diferente
print(resultado)

resultado = d > b #mayor que
print(resultado)

resultado = d < b #menor que
print(resultado)

a = int(input("digite un numero:"))
print(f"el residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero Par")
else:
    print(f"El valor de a es: {a} es un numero impar")


edadAdulto = 18
edadPersona = int(input("Escriba su edad: "))
if edadPersona >= edadPersona:
    print(f"Su edad es: {edadPersona}, entonces es mayor de edad")
else:
    print(f"Su edad es: {edadPersona}, entonces es menor de edad")


#Operadores logicos
a= True
b = False
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not -> cambia el valor
resultado = not a
print(resultado)




#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un numero dentro del rango 0 al 5: "))
valorMin = 0
valorMax = 5
dentroRango = (valor >= valorMin and valor <= valorMax)

if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} esta fiera del rango")



vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")



#Ejercicio: rango entre 20 y 30 años
edad = int(input("Digite su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

#if veinte or treinta:
if (edad >= 20 and edad < 30) or (edad >= 30 and edad <= 40):
    print("Estas dentro del rango de los (20\'0) a (30\'0)")
#    if veinte:
 #       print("Esta dentro del rango de los (20\'0)")
  #  elif treinta:
   #     print("Esta dentro del rango de los (30\'0)")
else:
    print("No estas dentro del rango de los (20\'0) a (30\'0)")


#Ejercicio: el mayor de dos numeros

numero1 = int(input('Digite un numero para el numero 1: '))
numero2 = int(input('Digite otro valor para el numero 2: '))

if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
else:
    print(f"El numero mayor es: {numero2}")


#ejercicio: Tienda de libros
print("Digite los siguientes datos del libro")
nombre = input('Digite el nombre del libro: ')
id= int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el envio es gratis (True/False): ')

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"

print(f'''
    # Nombre = {nombre}
   # ID = {id}
  #  Precio = {precio}
 #   Envio Gratuito?: {envioGratuito}
''')
'''
