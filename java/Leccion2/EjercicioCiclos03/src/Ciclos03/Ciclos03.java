/*
Ejercicios03: Leer numeros hasta que se introduzca un cero
Para cada unos indicar si es par o impar
 */
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        
        while (num != 0){
            if (num % 2 == 0){
                System.out.println("El numero ingresado "+num+" es par");
            }else{
                System.out.println("El numero ingresado "+num+" es impar");
            }
            System.out.println("Digite otro numero ");
        num = Integer.parseInt(entrada.nextLine());
        }
        
        System.out.println("El numero ingresado es "+num+ " finaliza el programa");
    }
    
}
