// Tipos de Datos en JS
/*
Multiples
comentarios
*/

var nombre = "Martin"; // Tip str
console.log(nombre);
nombre = 7;
console.log(nombre)

var numero = 3000; //Tipo Numerico
console.log(numero);

var objeto = {
    nombre: "Martin",
    apellido: "Ojeda",
    telefono : 45454545
}

console.log(objeto);

//Tipo de datos boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion() {
    
}
console.log(miFuncion)

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase 
class Persona{
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato pero su origen es object
console.log(typeof y);

//Tipo de dato array y empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z) //Esto se refiere a q es una cadena vacia