package gestorAplicación.tiendaAbst;

import java.util.HashMap;
import java.util.Map;
import gestorAplicación.cine.Usuario;

public abstract class Tienda {

    protected String nombre;
    protected Map<String, Integer> inventario = new HashMap<String, Integer >();
    protected Map<String, Integer> productos = new HashMap<String, Integer >();
    protected int repartidores = 3; 
    abstract public void saludo();

    abstract public void venderProducto(String nombre, Integer cantidad, Usuario usuario);

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
  
    public void agregarRepartidor(){
        repartidores++;
        
    }

    public int getRepartidores(){
        return repartidores;
        
    }

    public void agregarProducto(String nombre, Integer cantidad) {
        productos.put(nombre, cantidad);
        
    }

    public int getPrecio(String nombre) {
        return productos.get(nombre);
        
    }

    public void agregarInventario(String nombre, Integer cantidad) {
        inventario.put(nombre, cantidad);
        
    }

}