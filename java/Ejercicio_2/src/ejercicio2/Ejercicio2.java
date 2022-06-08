import java.util.Scanner;

public class Ejercicio_2 {

    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
        
        int horasSemanales;
        float salarioHora, salarioTotal;
        
        System.out.println("Digite las horas semanales trabajadas: ");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite salario que cobra por hora: ");
        salarioHora = Float.parseFloat(entrada.nextLine());
        
        salarioTotal = horasSemanales * salarioHora;
        System.out.println("El salario semanal es: U$$" + salarioTotal);
    }
    
}