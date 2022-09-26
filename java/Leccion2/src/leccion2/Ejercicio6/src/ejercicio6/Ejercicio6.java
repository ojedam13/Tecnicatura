/*Guillermo tiene N dolares. Luis tiene la mitad de lo que posee Guillermo.
Juan tiene la mitad de lo que posee Luis y Guillermo juntos. 
Hacer un programa que calcule e imprima la cantidad de dinero que tiene entre
los 3*/
package ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba cuantos dolares tiene Guillermo: ");
        float guille = Float.parseFloat(entrada.nextLine());
        float luis = guille / 2; 
        float juan = (guille + luis)/2;
        float total = guille + luis + juan;
        System.out.println("Luis tiene = " + luis + "dolares");
        System.out.println("Juan tiene = " + juan + "dolares");
        System.out.println("La cantidad de dinero que tiene es = " + total + "dolares");
        
    }
    
}
