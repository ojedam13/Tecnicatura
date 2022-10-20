class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # Decorador
    def nombre(self): #Metodo Getter
        #print('Estamos utlizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        #print('Estamos utlizando el metodo set')
        self._nombre = nombre

    @property  # Decorador
    def apellido(self):  # Metodo Getter
        #print('Estamos utlizando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        #print('Estamos utlizando el metodo set')
        self._apellido = apellido

    @property  # Decorador
    def edad(self):  # Metodo Getter
        #print('Estamos utlizando el metodo get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo Setter
       # print('Estamos utlizando el metodo set')
       self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Martin', 'Ojeda', 31)
    print(persona1.nombre) #Llamamos al metodos getter
    print(persona1.apellido)
    print(persona1.edad)
    persona1.nombre = 'Pepe' #Llamamos al metodo setter
    print(persona1.nombre) #El metodo getter
    print(persona1.mostrar_detalles()) #Llamamos el metodo mostrar detalles
    #Atributo read-only (solo lectura) seria la edad pq no tiene el metodo get
    print(persona1.edad)

    #Crear tres objetos mas, utilizando getter y setter para modificar y mostrar los cambios
    # con el metodo mostrar_detalles

    persona2 = Persona2('Lucas', 'Langoni', 20)
    persona2.nombre = 'Jorge'
    persona2.apellido = 'Ocampos'
    persona2.edad = 19
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Beto', 'Acosta', 40)
    persona3.nombre = 'Alberto'
    persona3.apellido = 'Acoust'
    persona3.edad = 51
    print(persona3.mostrar_detalles())

    persona4 = Persona2('Diego', 'Armando', 51)
    persona4.nombre = 'Dario'
    persona4.apellido = 'Maradona'
    persona4.edad = 62
    print(persona4.mostrar_detalles())

    print(__name__)