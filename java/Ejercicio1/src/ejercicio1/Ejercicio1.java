
package ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {
        //area del rectangulo
         Scanner scanner = new Scanner(System.in);
         System.out.println("Proporciona el alto");
         int alto = Integer.parseInt(scanner.nextLine());
         System.out.println("Proporciona el ancho");
         int ancho = Integer.parseInt(scanner.nextLine());
         int area = alto * ancho;
         int perimetro = (alto + ancho) * 2;
         System.out.println("area = " + area);
         System.out.println("perimetro = " + perimetro);
    }
    
}
