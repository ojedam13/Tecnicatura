
package ciclowhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while (conteo<= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Aumentamos en 1 la variable    
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador<7);
        
        for(var contando= 0; contando < 7; contando++){
            if(contando % 2 == 0){
            System.out.println("contando = " + contando);
            break;
            }
        }
        
        for(var contando= 0; contando < 7; contando++){
            if(contando % 2 != 0){
           
            continue;//vamos a la siguiente iteracion
            }
             System.out.println("contando = " + contando);
        }
    }
}
