/*
Ej1: Leer un numero y mostrar su cuadrado, repetir
el proceso hasta q se introduzca un numero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int num, cuadrado;
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(num >= 0){
            cuadrado = (int)Math.pow(num, 2);
            System.out.println("El numero "+ num + " elevado al cuadrado es: "+ cuadrado);
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El proceso a finalizado por numero negativo");
    }
}
