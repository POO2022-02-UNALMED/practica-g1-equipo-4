package gestorAplicación.cine;

import java.io.*;

public class Pelicula implements Serializable {
	
	private static final long serialVersionUID = 1L;
	
	private String nombre;
	
	private String genero;
	

	public Pelicula(String nombre, String genero) {
		
		this.nombre = nombre;
		
		this.genero = genero;
		
	}
	
	public String getnombre() {
		
		return nombre;		
		
	}
	    
	public String getGenero() {
		
		return genero;		
		
	}

}
	