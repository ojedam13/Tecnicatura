/*Una compañia de venta de carros usados, paga a su personal de ventar un 
salario de $1000 por mes mas una comision de 150$ x c/carro vendido, mas el 5%
del valor de la venta por carro. Cada mes el capturista de la empresa ingresa
en la computadore los datos pertinentes. Hacer un programa q calcule e imprima
el salario mensual de un vendedor dado. El salario de 1000 lo vamos a manejar
como un dato constante, para asignarlo debemos usar la palabra reservada fianl*/
package ejercicio7;

import java.util.Scanner;


public class Ejercicio7 {

  
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salarioBasico = 1000;
        //System.out.println("Carro vendido por el empleado: ");
        //float carroVendido = Float.parseFloat(entrada.nextLine());
        //System.out.println("Valor del carro: ");
        //float precioCarro = Float.parseFloat(entrada.nextLine());
        
        int comision = 150, venta;
        float salarioM, ventaCarro, porcVenta, totalPrecio;
        System.out.println("Cantidad autos vendidos");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Valor del carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioM = salarioBasico + comision + porcVenta;
        System.out.println("totalPrecio = " + salarioM);
        
       // float salarioMensual = (carroVendido * 150) + salarioBasico + (precioCarro * 5 / 100);
       // System.out.println("salarioMensual = " + salarioMensual);
        
        
        
    }
    
}
