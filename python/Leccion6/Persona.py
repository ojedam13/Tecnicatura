class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, edad): #Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 32

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Pipa', 'Benedetto', 32) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

persona2 = Persona('Aron', 'Molinas', 22)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}. Su edad es: {persona2.edad}')


persona1.nombre = "Juan"
persona1.apellido = "Roman"
persona1.edad = 43
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}. Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento q van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()