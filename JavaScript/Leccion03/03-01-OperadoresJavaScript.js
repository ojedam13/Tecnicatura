//Ejercicio para encontrar numeros pares
let parImpar = 10;
if (parImpar % 2 == 0) {
    console.log('Es un numero par');
} else {
    console.log("Es un numero impar");
}

//Ejercicio: es mayor d edad
let edad = 14, adulto = 18;
if (edad >= adulto) {
    console.log('Usted es una persona adulta')
} else {
    console.log('Usted es menor de edad');
}

//Ejercicio: dentro de un rango
let dentroRango = 5; // Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log('Esta dentro del rango establecido');
} else {
    console.log("Esta fuera del rango establecido");
}