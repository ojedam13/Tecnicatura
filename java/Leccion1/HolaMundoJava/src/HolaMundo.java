
import java.util.Scanner;

public class HolaMundo {
    
    public static void main(String arg[]) {
        /*
        int miVariableEntera = 10;
        System.out.println(miVariableEntera);

        //Modificamos variable
        miVariableEntera = 5;
        System.out.println(miVariableEntera);

        //variavle string
        String miVariableString = "Saludos";
        System.out.println(miVariableString);

        miVariableString = "Adios";
        System.out.println(miVariableString);

        //var
        var miVariableEntera2 = 10;
        System.out.println(miVariableEntera2);

        var miVariableCadena = "Boca";
        System.out.println(miVariableCadena);
        System.out.println("miVariableCadena = " + miVariableCadena);

        //valores permitidos en el nombre de la vaariable
        var miVariable = 1;
        var _miVariable = 3;
        var $miVariable = 4;
        var MIVARIABLE = 2;
        var áVarialbe = 5; //no se recomienda utulizar

        //concatenacion
        var usuario = "martin";
        var titulo = "dev";

        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var i = 3;
        var j = 4;
        System.out.println(i + j);
        System.out.println(usuario + i + j);//de der a izq realiza suma
        System.out.println(usuario + i + j); //todo lo toma como cadena
        System.out.println(usuario + (i + j));//uso de parentesis modifican la prioridad de evaluacion

        //caracteres especiales
        var nombre = "Messi";
        System.out.println("Nueva linea: \n" + nombre);
        System.out.println("Tabulador: \t" + nombre);
         System.out.println("Retroceso: \b" + nombre);
         
         
        //scanner
        System.out.println("Escribe tu nombre");
        Scanner consola = new Scanner (System.in);
        var usuarios = consola.nextLine();
        System.out.println("usuario = " + usuarios);
        
        //Libro
        Scanner consola = new Scanner (System.in);
        System.out.println("Escribe el titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Escribe el autor: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + " fue escrito por " + autor);
        
        //tipos enteros
        
        byte numeroByte = (byte)129; //min -128 a 127
        System.out.println("valor byte: " + numeroByte);
        System.out.println("valor minimo byte:" + Byte.MIN_VALUE);
        System.out.println("valor minimo byte:" + Byte.MAX_VALUE);
        
        short numeroShort = (short)32768;
        System.out.println("valor byte: " + numeroShort);
        System.out.println("valor minimo byte:" + Short.MIN_VALUE);
        System.out.println("valor minimo byte:" + Short.MAX_VALUE);
        
        int numeroInt = (int)2147483647L;
        System.out.println("valor byte: " + numeroShort);
        System.out.println("valor minimo byte:" + Integer.MIN_VALUE);
        System.out.println("valor minimo byte:" + Integer.MAX_VALUE);
        
        long numeroLong = 9223372036854775807L;
        System.out.println("valor byte: " + numeroLong);
        System.out.println("valor minimo byte: " + Long.MIN_VALUE);
        System.out.println("valor minimo byte: " + Long.MAX_VALUE);

         //tipos floteantes:float y double
         float numeroFloat = (float)10.0;
         System.out.println("numeroFloat = " + numeroFloat);
         System.out.println("Valor minimo tipo float= " + Float.MIN_VALUE);
         System.out.println("Valor minimo tipo float= " + Float.MAX_VALUE);
         
         double numeroDouble = 10;
         System.out.println("numeroDouble = " + numeroDouble);
         System.out.println("Valor minimo tipo double= " + Double.MIN_VALUE);
         System.out.println("Valor minimo tipo double= " + Double.MAX_VALUE);     
         
         var numEntero = 10;
         System.out.println("numEntero = " + numEntero);
         
         var numDouble=10.0;
         System.out.println("numDouble = " + numDouble);
         
         var numFloat = 10.0F;
         System.out.println("numFloat = " + numFloat);
         
         
         char miCaracter = 'a';
         System.out.println("miCaracter = " + miCaracter);
         
         char varChar = '\u0021';
         System.out.println("varChar = " + varChar);

         char varCharDecimal = 33;
         System.out.println("varCharDecimal = " + varCharDecimal);
         
         char varCharSimbolo = '!';
         System.out.println("varCharSimbolo = " + varCharSimbolo);
         
         var edad = Integer.parseInt("20");
         System.out.println("edad = " + (edad + 1));
         var valorPI = Double.parseDouble("3.1416");
         System.out.println("valorPI = " + valorPI);
       
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var caracter = "hola".charAt(1);
        System.out.println("caracter = " + caracter);
        var consola = new Scanner(System.in);
        System.out.println("Proporciona un caracter: ");
        caracter = consola.nextLine().charAt(0);
        System.out.println("caracter = " + caracter);
        
         Scanner scanner = new Scanner(System.in);
        System.out.println("Proporciona el nombre:");
        String nombre = scanner.nextLine();
        System.out.println("Proporciona el id:");
        int id = Integer.parseInt(scanner.nextLine());
        System.out.println("Proporciona el precio:");
        double precio = Double.parseDouble(scanner.nextLine());
        System.out.println("Proporciona el envio gratuito:");
        boolean envioGratuito = Boolean.parseBoolean(scanner.nextLine());
 
        System.out.println(nombre + " #" + id);
        System.out.println("Precio: $" + precio);
        System.out.println("Envio Gratuito: " + envioGratuito);
        
         
         //operadores aritmeticas
         int a=3, b=2; //Definimos 2 variables (con var no se puede)
         var resultado= a + b;
         System.out.println("resultado = " + resultado);
         resultado= a - b;
         System.out.println("resultado = " + resultado);
         resultado= a * b;
         System.out.println("resultado = " + resultado);
         resultado= a / b;
         System.out.println("resultado = " + resultado);
         resultado= a % b;
         System.out.println("resultado = " + resultado);
    
         if(b%2 == 0)
             System.out.println("Es numero par");
         else
             System.out.println("Es numero impar");
         
         //operadores de asignacion
         int a=3, b=2;
         int c = a+ 5 - b;
         System.out.println("c = " + c);
         //incremento
         a += 1; //a = a + 1
         System.out.println("a = " + a);
         //decremento
          a -= 5; //a = a - 5
         System.out.println("a = " + a);
         
         //operador unarios
         var a = 3;
         var b = -a;
         System.out.println("a = " + a);
         System.out.println("b = " + b);
         
         var c = true;
         var d = !c;
         System.out.println("c = " + c);
         System.out.println("d = " + d);
         
         //preincremento
         var e = 3;
         var f = ++e;
         System.out.println("e = " + e);//valor 4
         System.out.println("f = " + f);//valor 4
         
         //postincremento
         var g = 5;
         var h = g++;
         System.out.println("g = " + g);//valor 6
         System.out.println("h = " + h);//valor 5
         //predecremento
         var q = 3;
         var w = --q;
         System.out.println("q = " + q);//valor 2
         System.out.println("w = " + w);//valor 2
         
         //postdecremento
         var z = 5;
         var r = z--;
         System.out.println("z = " + z);//valor 4
         System.out.println("r = " + r);//valor 5
         
         //operadores de igualdad y  relacionales
         var a= 3;
         var b= 4;
         
         var c = (a==b);
         System.out.println("c = " + c);
         var d = (a!=b);
         System.out.println("d = " + d);
         
         var cadena = "hola";
         var cadena2 = "adios";
         
         var e = cadena == cadena2;
         System.out.println("e = " + e);
         
         var f = cadena.equals(cadena2);//compara el valor de las cadenas
         System.out.println("f = " + f);
         
         var g = a >=b;
         System.out.println("g = " + g);
         
         if(a%2 ==0){
             System.out.println("Es numero par");
           
         }else{
             System.out.println("Es impar");
    }

         var edad = 30;
         var adulto = 18;
         if(edad >= adulto){
             System.out.println("Es adulto");
         }else{
             System.out.println("Es menor de edad");
         }
         
        //operadores condicionales 
        var a = 10;
        var valorMin = 0;
        var valorMax = 10;
        
        var resultado = a>=0 && a<=10;
        if(resultado){
            System.out.println("Dentro del rango");
        }else{
            System.out.println("Fuera del rango");
        }
        
        var vacaciones = false;
        var diaDescanso = false;
        
        if (vacaciones || diaDescanso){
            System.out.println("Padre va a al juego");
        }else{
            System.out.println("Padre ocupado");
        }
        
        //Operador ternario
        var resultado2 = (3>2)? "Es verdadero"  : "No es verdadero" ; 
         System.out.println("resultado2 = " + resultado2);
         
         
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
             
         
         //Tipos primitivos booleanos
         
         var varBool = false;
         System.out.println("varBool = " + varBool);
         
         if (varBool) {
             System.out.println("La bandera es verde");
        }else{
             System.out.println("La bandera es roja");
         }
                
        //Conversiones de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        var entrada = new Scanner(System.in);
        System.out.println("Escribe su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        var fraseChar = "programadores".charAt(3);
        System.out.println("fraseChar = " + fraseChar);
        //if/else
        var condicion = true;
        
        if(condicion){
            System.out.println("Condicion verdadera");
        }else{
            System.out.println("Condicion falsa");
        }
        
       var num = 2;
        var numTxt = "num desconicido";
        
        if(num == 1){
            numTxt = "num 1";
        }else if (num == 2){
            numTxt = "num 2";
        }else if(num == 3){
            numTxt = "nume3";
        }else {
            numTxt = "Numero no encontrado";
        } 
        System.out.println("numTxt = " + numTxt);
        
         var mes = 1;
         var estacion = "Estacion desconosida";
         if (mes == 1 || mes ==2 || mes == 12){
            estacion = "invierno";
         }
         else if (mes == 3 || mes == 4 || mes ==5){
             estacion ="primavera";
         }
         else{
             estacion = "verano o otoño";
         }
         System.out.println("estacion = " + estacion);
        
        var mes = 1;
        var estacion = "Estacion desconosida";
        
        switch(mes){
            case 1: case 2: case 12:
                estacion= "invierno";
                break;
            case 3: case 4: case 5:
                estacion="Primavera";
            case 6: case 7 : case 8:
                estacion = "Invierno";
            case 9: case 10: case 11:
                estacion = "otonio";
                break;
            
        }
        System.out.println("estacion = " + estacion);
        
        //inicializar variable al mismo tiempo
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2; //inferencia de tipo
        System.out.println("solucion de la suma = " + solucion);

        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);

        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);

        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);

        var solucion2 = 3.4 / num2; //double, le asigna automaticamente por inferencia de tipo
        System.out.println("solucion2 = " + solucion2);

        solucion = num1 % 2; //guarda residuo entero de la division
        System.out.println("solucion = " + solucion);

        if (num1 % 2 == 0) {
            System.out.println("Es par");
        } else {
            System.out.println("Numero impar");
        }
        
        int varNum1 = 2, varNum2 =4;
        int varNum3 = varNum1 + 6 - varNum2; //calculo de izq a derecha
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //varNum1 = varNum1 + 1; valor de composicion
        System.out.println("varNum1 = " + varNum1);
        varNum1 -= 2; 
        System.out.println("varNum1 = " + varNum1);
        varNum1 *= 3; 
        System.out.println("varNum1 = " + varNum1);
        varNum1 /= 4; 
        System.out.println("varNum1 = " + varNum1);
        varNum1 %= 5; 
        System.out.println("varNum1 = " + varNum1);
        
        //CLASE 8
        //operadores unarios: cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
        
        //Operador de Negacion
        var varC = true;//Esta literal es de tipo boolean
        var varD = !varC;//! invierte en valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores unarios : Preincremento
        var varE = 9; //Se va a modificar su valor
        var varF = ++varE;
        //Primero incrementa la variable y desp se usa el valor
        System.out.println("varE = " + varE);//se incrementa en la unidad
        System.out.println("varF = " + varF);//va a  sumar uno
        //Operadores unarios : Postincremento
        var varG = 3; 
        var varH = varG++; //Primero elvalor de la variable desp el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
         //Operadores unarios : Predecremento
        var varI = 4; //Se va a modificar su valor
        var varJ = --varI;
        //Primero decrementa la variable y desp se usa el valor
        System.out.println("varI = " + varI);//se decrementa en la unidad
        System.out.println("varJ = " + varJ);//va a  restar uno
        //Operadores unarios : Postdecremento
        var varK = 8; 
        var varL = varK--; //Primero elvalor de la variable desp el decremento
        System.out.println("varK = " + varK);//Decrementa en 1
        System.out.println("varL = " + varL);
        
        //Operadores de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);//dato de tipo booleano
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum; //dato tipo booleano
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "Chau";
        var cVar = cadenaA == cadenaB;//hace comparacion por referencia
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);// compara si el contenido es igual
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum > bNum; // >= mayor o igual
        System.out.println("gVar = " + gVar);
        var hNum = aNum < bNum; // <= menor o igual
        System.out.println("hNum = " + hNum);
        
        //si el numero es par o impar
        if (aNum % 2 == 0) {
            System.out.println("El n es par");
        }else{
            System.out.println("El n es impar");
        }
        //si es mayor de edad
        var edad = 30;
        var adulto = 18;
        if(edad > adulto){
            System.out.println("Mayor de edad");
        }else{
            System.out.println("Menor de edad");
        }
        
        //Operadore condicionales
        var valorA = 7;
        var valorMin = 0;
        var valorMax = 10;
        var rta = valorA > 0 && valorA <= 10;// SI LOS DOS SON V ES Verdadero
        if (rta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("esta fuerta del rango establecido");
        }
        
        var vacaciones = false;
        var diaLibre = false;
        if(vacaciones|| diaLibre){
            System.out.println("Puede asistir");
        }else{
            System.out.println("No puede asistir");
        }
        
        //Operador ternario
        var rtdo = ( 5>8) ? "Es verdadero" : "Es falso"; 
        System.out.println("rtdo = " + rtdo);
        
        var numT = 7;
        rtdo = (numT%2 ==0) ? "Es par" :"Es impar";
        System.out.println("rtdo = " + rtdo);
         
        //Precedencia de operadores
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x); //6
        System.out.println("y = " + y); // 9
        System.out.println("z = " + z);//16
        
        var solucionArit = 4 + 5 * 6 / 3;
        System.out.println("solucionArit = " + solucionArit);
        solucionArit = (4 + 5) * 6 / 3;
        System.out.println("solucionArit = " + solucionArit);
     */
      
    }
}
