package Cine.gestiorAplicacion.cine;

public class Usuario {
    private String nombre;
    private int cedula;
    private Boolean suscripcion = false;
    private Boleta boleta;

    public Usuario(String nombre, int cedula) {
        this.nombre = nombre;
        this.cedula = cedula;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCedula() {
        return cedula;
    }

    public Boolean getSuscripcion() {
        return suscripcion;
    }

    public void setSuscripcion(Boolean suscripcion) {
        this.suscripcion = suscripcion;
    }

    public Boleta getBoleta() {
        return boleta;
    }

    public void setBoleta(Boleta boleta) {
        this.boleta = boleta;
    }

    public void comprarBoleta(Boleta boleta) {
        this.boleta = boleta;
    }

    public void comprarBoleta(Boleta boleta, Boolean suscripcion) {
        this.boleta = boleta;
        this.suscripcion = suscripcion;
    }

    public void comprarBoleta(Boleta boleta, Boolean suscripcion, int cedula) {
        this.boleta = boleta;
        this.suscripcion = suscripcion;
        this.cedula = cedula;
    }

    public void comprarBoleta(Boleta boleta, int cedula) {
        this.boleta = boleta;
        this.cedula = cedula;
    }


    
}
