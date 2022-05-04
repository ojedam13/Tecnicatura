
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
         */
         
         
    }
}
