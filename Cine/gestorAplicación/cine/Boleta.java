package gestorAplicación.cine;

public class Boleta {
	
    private Usuario usuario;    
    private String pelicula;
    private String sala;
    private Horario horario;
    private String dia;
    //attribute Asiento as an array of Integers
    private int[] asiento;
  
    public Boleta(Usuario usuario, String pelicula, String sala, int [] asiento, Horario horario, String dia) {
        this.usuario = usuario;
        this.pelicula = pelicula;
        this.sala = sala;
        this.horario = horario;
        this.asiento = asiento;
        this.dia = dia;

    }
    
    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public String getPelicula() {
        return pelicula;
    }

    public void setPelicula(String pelicula) {
        this.pelicula = pelicula;
    }

    public String getSala() {
        return sala;
    }

    public void setSala(String sala) {
        this.sala = sala;
    }

    public Horario getHorario() {
        return horario;
    }

    public void setHorario(Horario horario) {
        this.horario = horario;
    }

    public String getDia() {
        return dia;
    }

    public void setDia(String dia) {
        this.dia = dia;
    }

    public int[] getAsiento() {
        return asiento;
    }

    public void setAsiento(int[] asiento) {
        this.asiento = asiento;
    }


    
}
