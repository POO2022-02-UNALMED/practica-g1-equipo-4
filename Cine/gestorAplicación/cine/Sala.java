package gestorAplicación.cine;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Sala {

    private String nombre; // nombre de la sala, por ejemplo Sala 1
    private ArrayList<Asiento> Asiento = new ArrayList<Asiento>(); // lista de asientos ocupados
    private Map<Pelicula, Horario> cartelera = new HashMap<Pelicula, Horario>(); // Cartelera de la sala | Pelicula, Horario

    public Sala(String nombre, ArrayList<Asiento> Asiento, Map<Pelicula, Horario> cartelera) {
        this.nombre = nombre;
        this.Asiento = Asiento;
        this.cartelera = cartelera;

    }

    public String getNombre() {
        return nombre;
        
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
        
    }

    public ArrayList<Asiento> getAsiento() {
        return Asiento;
        
    }

    public void setAsiento(ArrayList<Asiento> Asiento) {
        this.Asiento = Asiento;
        
    }

    public Map<Pelicula, Horario> getCartelera() {
        return cartelera;
        
    }

    public void setCartelera(Map<Pelicula, Horario> cartelera) {
        this.cartelera = cartelera;
        
    }
 
    

}
