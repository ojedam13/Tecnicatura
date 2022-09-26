
package ejercicio_1;

import java.util.Scanner;

public class Ejercicio_1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratis = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro + " #" + idLibro);
        System.out.println("precioLibro: $" + precioLibro);
        System.out.println("El envio del libro es gratis: " + envioGratis);
        
    }
    
}
