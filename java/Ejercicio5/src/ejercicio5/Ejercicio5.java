/* Hacer un programa que calcule e imprima la suma de 3 calificaciones.
Pedir las calificaiones al usuario*/ 
package ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un calificacion: ");
        float nota1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite una nueva calificacion: ");
        float nota2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite otra calificacion: ");
        float nota3 = Float.parseFloat(entrada.nextLine());
        float resultado = nota1+nota2+nota3;
        System.out.println("El resultado de las 3 calificaciones es = " + resultado);
        
    }
}
