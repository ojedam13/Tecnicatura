class Persona: #Creamos una clase
    def __init__(self, nombre, apellido,dni, edad, *args, **kwargs): #Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad},la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Pipa', 'Benedetto', 35353535, 32) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

persona2 = Persona('Aron', 'Molinas',353535, 22)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')


persona1.nombre = "Juan"
persona1.apellido = "Roman"
persona1.edad = 43
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento q van a tener los objetos (acciones)
persona1.mostrar_detalle() #La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dará error
persona1.telefono = '4545454545'
print(persona1.telefono)
print(f'Este el el telefono de: {persona1.nombre} {persona1.telefono} ')
#print(persona2.telefono) persona2 no tiene este atributo, da un error

persona3 = Persona('Rogelio', 'Romero',354563636, 22, 'Telefono', '4545454','calle Lopez', 823, 'Manzana', 77,'casa', 18, Altura=1.83, Peso=105, CFav= 'Azul',Auto='Citroen',Modelo= 2021)
persona3.mostrar_detalle()
#print(persona3._dni) No se debe utlizar en python(esta encapsulado), esto dice q lo desconocemos
# persona3.__nombre Esta totalmente encapsulado no se puede ejecutar
