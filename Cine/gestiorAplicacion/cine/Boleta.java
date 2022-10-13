package Cine.gestiorAplicacion.cine;

public class Boleta {
    private Usuario usuario;
    private Pelicula pelicula;
    private Sala sala;
    private Asiento asiento;
    private Horario horario;
    
    public Boleta(Usuario usuario, Pelicula pelicula, Sala sala, Asiento asiento, Horario horario) {
        this.usuario = usuario;
        this.pelicula = pelicula;
        this.sala = sala;
        this.asiento = asiento;
        this.horario = horario;
    }
    
    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public Pelicula getPelicula() {
        return pelicula;
    }

    public void setPelicula(Pelicula pelicula) {
        this.pelicula = pelicula;
    }

    public Sala getSala() {
        return sala;
    }

    public void setSala(Sala sala) {
        this.sala = sala;
    }

    public Asiento getAsiento() {
        return asiento;
    }

    public void setAsiento(Asiento asiento) {
        this.asiento = asiento;
    }

    public Horario getHorario() {
        return horario;
    }

    public void setHorario(Horario horario) {
        this.horario = horario;
    }


}
