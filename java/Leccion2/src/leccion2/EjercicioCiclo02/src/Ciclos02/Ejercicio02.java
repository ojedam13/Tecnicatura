/*
 Ejercicio2: Leer un num e indicar si es + o -.El proceso se repetira hasta
q se introduzca un 0
 */
package Ciclos02;

import javax.swing.JOptionPane;



public class Ejercicio02 {
    public static void main(String[] args) {
        System.out.println("Digite un numero: ");
        var num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (num != 0) {
            if(num > 0){
               JOptionPane.showMessageDialog(null, "El numero "+ num + " es positivo");
            }else{
                JOptionPane.showMessageDialog(null,"El numero "+ num + " es negativo");
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        JOptionPane.showMessageDialog(null,"El numero "+num+ " finaliza el programa");
    }
}
