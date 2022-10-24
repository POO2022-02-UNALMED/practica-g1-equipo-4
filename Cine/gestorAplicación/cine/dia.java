package gestorAplicación.cine;



public class Dia{

    private String nombreDelDiaDeLaSemana;
    private Sala sala;


    public Dia(String nombreDelDiaDeLaSemana, Sala sala) {
        this.nombreDelDiaDeLaSemana=nombreDelDiaDeLaSemana;
        this.sala = sala;
    }

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