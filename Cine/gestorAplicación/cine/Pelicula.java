package gestorAplicación.cine;

public class Pelicula {
	
	private String nombre;
	private String genero;
	

	public Pelicula(String nombre, String genero) {
		this.nombre = nombre;
		this.genero = genero;
	}

	
	public String getnombre() {
		return nombre;		
		
	}
	
    public void setNombre(String nombre) {
        this.nombre = nombre;
        
    }
    
	public String getGenero() {
		return genero;		
		
	}
	
    public void setGenero(String genero) {
        this.genero = genero;
        
    }
    
}
	