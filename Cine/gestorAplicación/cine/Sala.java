package gestorAplicación.cine;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Sala {

    private String nombre; // nombre de la sala, por ejemplo Sala 1
    
    private ArrayList<String> asientosOcupados = new ArrayList<String>(); // lista de asientos ocupados
    
    private Map<Pelicula, Horario> cartelera = new HashMap<Pelicula, Horario>(); // Cartelera de la sala | Pelicula, Horario

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
 
    public Map<Pelicula, Horario> getCartelera() {
        return cartelera;
        
    }

    // Agrega una pelicula a la cartelera de la sala
    public void agregarPelicula(Pelicula pelicula, Horario horario) {
        cartelera.put(pelicula, horario);
        
    }

}
