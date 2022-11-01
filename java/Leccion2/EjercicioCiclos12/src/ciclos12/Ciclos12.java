/*
Ej 12: Pedir un numero y calcular su factorial
 */
package ciclos12;

import javax.swing.JOptionPane;

public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner (System.in);
        long factorial = 1;
        //System.out.printIn("Digite un numero: ");
        int num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        for(int i= 1; i<= num; i++){
        factorial *= i;
        }
        //System.out.println("\n El factorial del numero ingresado es: "+factorial);
        JOptionPane.showMessageDialog(null, "El factorial del numero ingresado es: "+factorial);
    }
}
