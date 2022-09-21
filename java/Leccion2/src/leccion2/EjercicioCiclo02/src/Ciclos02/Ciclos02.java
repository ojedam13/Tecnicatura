/*
Ejercicio2: Leer un num e indicar si es + o -.El proceso se repetira hasta
q se introduzca un 0
 */
package Ciclos02;

import java.util.Scanner;

public class Ciclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var num = Integer.parseInt(entrada.nextLine());
        while (num != 0) {
            if(num > 0){
            System.out.println("El numero "+ num + " es positivo");
            }else{
                System.out.println("El numero "+ num + " es negativo");
            }
            System.out.println("Digite otro numero");
            num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+num+ " finaliza el programa");
    }
}
