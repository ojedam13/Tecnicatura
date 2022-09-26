
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona();//llamamos al contructor
        persona1.nombre = "Martin";
        persona1.apellido = "Ojeda";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Lionel";
        persona2.apellido = "Messi";
        persona2.obtenerInformacion();
    }
}
