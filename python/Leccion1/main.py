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
'''

edadAdulto = 18
edadPersona = int(input("Escriba su edad: "))
if edadPersona >= edadPersona:
    print(f"Su edad es: {edadPersona}, entonces es mayor de edad")
else:
    print(f"Su edad es: {edadPersona}, entonces es menor de edad")

