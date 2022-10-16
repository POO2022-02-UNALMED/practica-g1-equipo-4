package Cine.gestorAplicación.tiendaAbst;

import java.util.HashMap;
import java.util.Map;

public class TiendaComida extends Tienda{

    public TiendaComida(String nombre) {
        super(nombre);
    }
    
    private Map <String, Integer> productos = new HashMap <String, Integer>();
    private Map <String, Integer> inventario = new HashMap <String, Integer>();

    public Map<String, Integer> getProductos() {
        return productos;
    }

    public void setProductos(Map<String, Integer> productos) {
        this.productos = productos;
    }

    public void agregarProducto(String nombre, Integer cantidad) {
        productos.put(nombre, cantidad);
    }

    public Map<String, Integer> getInventario() {
        return inventario;
    }

    public void setInventario(Map<String, Integer> inventario) {
        this.inventario = inventario;
    }

    public void agregarInventario(String nombre, Integer cantidad) {
        inventario.put(nombre, cantidad);
    }

    public void venderProducto(String nombre, Integer cantidad) {
        if (inventario.get(nombre) >= cantidad) {
            inventario.put(nombre, inventario.get(nombre) - cantidad);
            
        }
    }

   


}
