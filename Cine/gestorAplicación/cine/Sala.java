package Cine.gestorAplicación.cine;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Sala {

    String nombre; // nombre de la sala, por ejemplo Sala 1
    private ArrayList<String> asientosOcupados = new ArrayList<String>(); // lista de asientos ocupados
    


    public Sala(String nombre) {
        this.nombre = nombre;
    }

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

    

}
