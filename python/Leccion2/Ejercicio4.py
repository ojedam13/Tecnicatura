#Etapas de vida
edad = int(input("Ingrese su edad: "))

if (edad >= 0 and edad <= 10):
    print("La infancia es increible y bella")
elif (edad > 10 and edad < 20):
    print("Tienes muchos cambios, mucho que estudiar")
elif (edad >= 20 and edad < 30 ):
    print("Amor y comienza el trabajo")
elif (edad >= 30 and edad < 40 ):
    print("La mejor edad")
elif (edad >= 40 and edad < 50 ):
    print("los 40s")
elif (edad >= 50 and edad < 60 ):
    print("los 50s")
else:
    print("Estas al horno")
