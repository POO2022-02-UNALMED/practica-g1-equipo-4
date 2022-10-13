package Cine.gestiorAplicacion.cine;

import java.util.ArrayList;

public class Sala {
    ArrayList<Pelicula> pelicula = new ArrayList<Pelicula>();
    ArrayList<Asiento> asientos = new ArrayList<Asiento>();
    int numero;

    public Sala(ArrayList<Pelicula> pelicula, ArrayList<Asiento> asientos, int numero) {
        this.pelicula = pelicula;
        this.asientos = asientos;
        this.numero = numero;
    }
    
    public ArrayList<Pelicula> getPeliculas() {
        return pelicula;
    }


    public ArrayList<Asiento> getAsientos() {
        return asientos;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

}
