#Ej 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celcius
# a fahrenheit y viceversa.
# Investigar las formulas

#Funcion q convierte de celsius a fahrenheir
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #La presedencia: mult, division y suma

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Digite el valor de celcius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado2 = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C-> {resultado2:.2f}')