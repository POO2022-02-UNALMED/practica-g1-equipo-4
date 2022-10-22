package gestorAplicación.cine;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Sala {

    private String nombre; // nombre de la sala, por ejemplo Sala 1
    
    private ArrayList<String> asientosOcupados = new ArrayList<String>(); // lista de asientos ocupados
    
    private Map<String, String> cartelera = new HashMap<String, String>(); // Cartelera de la sala | Pelicula, Horario

    public String getNombre() {
    	
        return nombre;
        
    }

    public void setNombre(String nombre) {
    	
        this.nombre = nombre;
        
    }

    public ArrayList<String> getAsientosOcupados() {
    	
        return asientosOcupados;
        
    }

    public void setAsientosOcupados(ArrayList<String> asientosOcupados) {
    	
        this.asientosOcupados = asientosOcupados;
        
    }

    public void setCartelera(Map<String, String> cartelera) {
    	
        this.cartelera = cartelera;
        
    }

    public Map<String, String> getCartelera() {
    	
        return cartelera;
        
    }

    public Sala(String nombre) {
    	
        this.nombre = nombre;
        
    }   

    public void agregarCartelera(String pelicula, String horario) {
    	
        this.cartelera.put(pelicula, horario);
        
    }    

}
