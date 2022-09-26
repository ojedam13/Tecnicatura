/*
Ejercicios03: Leer numeros hasta que se introduzca un cero
Para cada unos indicar si es par o impar
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int num;
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        
        while (num != 0){
            if (num % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado "+num+" es par");
            }else{
                 JOptionPane.showMessageDialog(null,"El numero ingresado "+num+" es impar");
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado es "+num+ " finaliza el programa");
    }
}
