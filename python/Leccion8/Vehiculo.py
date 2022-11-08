class Vehiculo:
    '''
    Definir una clase Padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales herean de la calse padre Vehiculo.
    La clase padre debe tener los siguiente atributos y metodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad(km/hr))
    -Metodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña,etc))
    -Metodos(__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase
    '''
    def __init__(self,color, ruedas):
       self.color = color
       self.ruedas = ruedas

    def __str__(self):
        return f' Color: {self.color}, Ruedas: {self.ruedas}'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, vel):
        super().__init__(color, ruedas)
        self.vel = vel

    def __str__(self):
        return super().__str__() + f', Velocidad(km/h): {self.vel}'

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + f', Tipo: {self.tipo} '

vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

auto = Auto('Negro', 4, 160)
print(auto)

bici = Bicicleta('Verde', 2, 'MountainBike')
print(bici)