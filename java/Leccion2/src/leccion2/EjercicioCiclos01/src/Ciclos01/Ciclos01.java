/*
Ej1: Leer un numero y mostrar su cuadrado, repetir
el proceso hasta q se introduzca un numero negativo
*/
package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, cuadrado;
        System.out.println("Digite un numero: ");
        num = Integer.parseInt(entrada.nextLine());
        while(num >= 0){
            cuadrado = (int)Math.pow(num, 2);
            System.out.println("El numero "+ num + " elevado al cuadrado es: "+ cuadrado);
            System.out.println("Digite otro numero: ");
            num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El proceso a finalizado por numero negativo");
    }
}
