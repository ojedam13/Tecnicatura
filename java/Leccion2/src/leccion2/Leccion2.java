package Leccion2;

import java.util.Scanner;

public class Leccion2 {

    public static void main(String[] args) {
        /*
        var condicion = true;
        if(condicion){
            System.out.println("Condicion verdadera"); // condicional simple
        }
        else{
            System.out.println("Condicion Falsa"); //condicional doble
        }
        
        var numero = 2;
        var numeroTxt = "numero desconocido";
        
        if (numero == 1){
            numeroTxt = "Numero 1";
        }
        else if(numero == 2){
              numeroTxt = "Numero 2";         
        }
        else if(numero == 3){
              numeroTxt = "Numero 3";         
        }
        else if(numero ==4){
              numeroTxt = "Numero 4";         
        }
        else{
              numeroTxt = "Numero no encontrado";         
        }
        System.out.println("numeroTxt = " + numeroTxt);  
         */
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTxt = "numero desconocido";
        switch (numero) {
            case 1:
                numeroTxt = "Numero 1";
                break;
            case 2:
                numeroTxt = "Numero 2";
                break;
            case 3:
                numeroTxt = "Numero 3";
                break;

            case 4:
                numeroTxt = "Numero 4";
                break;
            default:
                numeroTxt = "Numero no encontrado";
           
        }
         System.out.println("numeroTxt = " + numeroTxt);
    }
}
