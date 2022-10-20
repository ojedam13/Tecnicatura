class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase de python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return  self.operandoA + self.operandoB

    def multiplicar(self):
        return  self.operandoA * self.operandoB

    def dividir(self):
        return  self.operandoA / self.operandoB
aritmetica1 = Aritmetica(7, 9) #Le pasamos los argumentos para los operadores
print(aritmetica1.sumar())

print(f'La resta de los numero es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numero es: {aritmetica1.multiplicar()}')
print(f'La division de los numero es: {aritmetica1.dividir():.2f}')