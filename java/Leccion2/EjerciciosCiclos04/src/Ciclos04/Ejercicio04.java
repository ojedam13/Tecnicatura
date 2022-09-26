/*
Ej 4 : Pedir numeros hasta q se teclee uno negativo, y mostrar cuantos numeros
se han introducido
 */
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        
        int numero, conteo = 0;  
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        while (numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+ numero +" es postivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            }
        JOptionPane.showMessageDialog(null,"A Ingresado "+conteo+ " numero q son positivos");
    }
}

   