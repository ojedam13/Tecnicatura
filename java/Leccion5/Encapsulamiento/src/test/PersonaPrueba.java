
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1: "+persona1);
        System.out.println("persona1 su nombre es: "+ persona1.getNombre());
        //Modificar a través de métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacion"; // Ya no se puede utilizar
        //System.out.println("Nombre es:"+persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado es: "+ persona1.getNombre());
        System.out.println("persona1 el sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 el boolean es " + persona1.isEliminado());
        
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial 
        // e imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Martin", 185000, false);
        System.out.println("persona2 su nombre es: "+ persona2.getNombre());
        System.out.println("persona2 el sueldo es: "+persona2.getSueldo());
        System.out.println("persona2 el boolean es " + persona2.isEliminado());
        //Modificar Valores
        persona2.setNombre("Messi");
        persona2.setSueldo(10000000);
        persona2.setEliminado(true);
        System.out.println("persona2 con su nombre modificado es: "+ persona2.getNombre());
        System.out.println("persona2 con el sueldo modifciado es: "+persona2.getSueldo());
        System.out.println("persona2 con el boolean mpdificado es " + persona2.isEliminado());
        
        System.out.println("persona1: "+persona1);
    }
}
