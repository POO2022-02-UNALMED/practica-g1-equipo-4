package gestorAplicación.cine;

import java.io.*;

public class Pelicula implements Serializable {
	//atributos
	private static final long serialVersionUID = 1L;
	
	private String nombre;
	
	private String genero;
	
	//constructor
	public Pelicula(String nombre, String genero) {
		this.nombre = nombre;
		this.genero = genero;
		
	}
	//metodos get
	public String getnombre() {
		
		return nombre;		
		
	}
	    
	public String getGenero() {
		
		return genero;		
		
	}

}
	