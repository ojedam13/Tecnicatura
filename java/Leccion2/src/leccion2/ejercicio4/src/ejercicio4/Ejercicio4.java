
package ejercicio4;

import java.util.Scanner;


public class Ejercicio4 {

    
    public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite otro numero: ");
        int numero2 = Integer.parseInt(entrada.nextLine());
        System.out.print("El numero mayor es: ");
        System.out.println(numero1 > numero2 ? numero1 : numero2);
    }
    
}
