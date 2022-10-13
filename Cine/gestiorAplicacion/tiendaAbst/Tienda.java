package Cine.gestiorAplicacion.tiendaAbst;

import java.util.HashMap;
import java.util.Map;

public abstract class Tienda {

    protected String nombre;
    protected Map<String, Integer> inventario = new HashMap<String, Integer >();
    protected Map<String, Integer> productos = new HashMap<String, Integer >();

    public Tienda(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Map<String, Integer> getInventario() {
        return inventario;
    }

    public Map<String, Integer> getProductos() {
        return productos;
    }

    public void setProductos(Map<String, Integer> productos) {
        this.productos = productos;
    }

    public void setInventario(Map<String, Integer> inventario) {
        this.inventario = inventario;
    }

    



}



