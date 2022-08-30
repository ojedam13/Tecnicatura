'''Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
Realizar un algoritmo para calcular la calificacion promedio y la mas baja de
todo el grupo '''
x= 1
suma = 0
baja = 9999
while x <= 10:
     calificacion = int(input("Ingresar su calificacion: "))
     x+=1

     suma = suma + calificacion

     if calificacion < baja:
         baja = calificacion
promedio = suma / 10
print(f'la suma de de las calificaciones es {promedio} ')
print(f'la calificacion mas baja es {baja} ')
