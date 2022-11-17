package gestorAplicación.cine;

import java.io.Serializable;

public class Dia implements Serializable{
	
	private static final long serialVersionUID = 1L;
 //atributos
    private String nombreDelDiaDeLaSemana;
    private Sala sala;

//constructor: es lo que se ejecuta cuando se crea una nueva instancia
    public Dia(String nombreDelDiaDeLaSemana, Sala sala) {
        this.nombreDelDiaDeLaSemana=nombreDelDiaDeLaSemana;
        this.sala = sala;
    }
// metodos get y set
    public String getnombreDelDiaDeLaSemana(){
        return this.nombreDelDiaDeLaSemana;
    }
    
    public void setnombreDelDiaDeLaSemana(String nombreDelDiaDeLaSemana){
        this.nombreDelDiaDeLaSemana=nombreDelDiaDeLaSemana;
    }

    public Sala getSala(){
        return this.sala;
    }

    public void setSala(Sala sala){
        this.sala=sala;
    }

}
