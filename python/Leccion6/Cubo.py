'''
Crear la clase Cubo con los atributos,ancho,alto y profundidad, con un metodo calcular_volumen
que tendra la formula: volumen = ancho * altura * profundidad
que el usuario ingrese los valores.
'''
class Cubo:
    def __init__(self,altura, ancho, profundidad):
        self.altura = altura
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad

altura = int(input('Digite el numero para la altura del cubo: '))
ancho = int(input('Digite el numero para el ancho del cubo: '))
profundidad = int(input('Digite el numero para la profundidad del cubo: '))

cubo1 = Cubo(altura, ancho, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')

