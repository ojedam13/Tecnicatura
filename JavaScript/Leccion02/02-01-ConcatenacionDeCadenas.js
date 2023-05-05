var nombre = 'Jose';
var apellido = 'Montes';
var nombreCompleto = nombre + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel' + '' + 'Betancud';
console.log(nombreCompleto2);

nombre += apellido; //Tercera concatenacion
console.log(nombre);

//Se utiliza let y const
let nombre2 = 'Pedro';
console.log(nombre2);

const apellido2 = 'Lepes';
//apellido2 = 'Perez' Una constante no puede ser modificada
console.log(apellido2);

let x, y; //Se pueden crear varias variables dentro de una misma linea
x = 17, y = 21; //Se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y; //Se asigna el valor de la operacion
console.log(z); 

let _1num = 31; //No se puede empezar con un numero, puede ser mayuscula _ o letras ni palabras reservadas
let rompiendo = 'Rompe';

console.log(_1num);
console.log(rompiendo);