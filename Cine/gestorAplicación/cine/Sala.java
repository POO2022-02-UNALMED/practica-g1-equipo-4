package gestorAplicación.cine;

import java.io.*;

import java.util.HashMap;

import java.util.Map;


public class Sala implements Serializable {
	
	private static final long serialVersionUID = 1L;
	
    private String nombre; // nombre de la sala, por ejemplo Sala 1
    // lista de asientos ocupados
    private Map<Pelicula, Horario> cartelera = new HashMap<Pelicula, Horario>(); // Cartelera de la sala | Pelicula, Horario
    private Map<String, boolean[] > Asientos = new HashMap<String, boolean[]>();
//constructores
    public Sala ( Map<String, boolean[]> Asientos, Map<Pelicula, Horario> cartelera) {
    	this.nombre = "Sala Unal";
    	this.Asientos = Asientos;
        this.cartelera = cartelera;

        
    }
   
    public Sala (String nombre, Map<String, boolean[]> Asientos, Map<Pelicula, Horario> cartelera) {
        this.nombre = nombre;
        this.Asientos = Asientos;
        this.cartelera = cartelera;

    }
//metodos get y set
    public String getNombre() {
    	
        return nombre;
        
    }

    public void setNombre(String nombre) {
    	
        this.nombre = nombre;
        
    }

    public Map<Pelicula, Horario> getCartelera() {
        return cartelera;
        
    }

    public void setCartelera(Map<Pelicula, Horario> cartelera) {
        this.cartelera = cartelera;
        
    }

    public Map<String, boolean[] > getAsientos() {
        return Asientos;
        
    }

    public void setAsientos(Map<String, boolean[] > Asientos) {
        this.Asientos = Asientos;
        
    }
    //print the names of the movies and  the times in cartelera
}
