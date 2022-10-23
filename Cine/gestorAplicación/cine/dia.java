package gestorAplicación.cine;

import java.util.ArrayList; 
import java.util.random;

public class dia{

    private String nombreDelDiaDeLaSemana;
    private ArrayList<Sala> salasDisponibles=new arraylist<Sala>();


    public dia(String nombreDelDiaDeLaSemana, ArrayList<Sala> salasDisponibles){
        this.nombreDelDiaDeLaSemana=nombreDelDiaDeLaSemana;
        this.salasDisponibles=salasDisponibles;
    }

    public String getnombreDelDiaDeLaSemana(){
        return this.nombreDelDiaDeLaSemana;
    
    public void setnombreDelDiaDeLaSemana(String nombreDelDiaDeLaSemana){
        this.nombreDelDiaDeLaSemana=nombreDelDiaDeLaSemana;
    }

    public ArrayList<Sala> getSalasDisponibles(){
        return this.salasDisponibles;
    }

    public void setSalasDisponibles(ArrayList<Sala> salasDisponibles){
        this.salasDisponibles=salasDisponibles;
    } 





}