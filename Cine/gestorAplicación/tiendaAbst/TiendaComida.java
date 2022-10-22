package gestorAplicación.tiendaAbst;

import java.util.HashMap;
import java.util.Map;
import gestorAplicación.cine.Usuario;

public class TiendaComida extends Tienda{

    public TiendaComida(String nombre) {
    	
        super(nombre);
        
    }
    
    private Map <String, Integer> productos = new HashMap <String, Integer>();  // producto - cantidad en inventario
    
    private Map <String, Integer> inventario = new HashMap <String, Integer>(); // producto - precio
    
    public int repartidores = 3;
    
    @Override
    public void saludo() {
    	
        System.out.println("Bienvenido a la tienda de comida del cine UNAL");
        
    }

    @Override
    public void venderProducto(String nombre, Integer cantidad) {
    	
        if (inventario.get(nombre) >= cantidad) {
        	
            inventario.put(nombre, inventario.get(nombre) - cantidad);
            
        }
        
    }

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

    public void agregarMixto (String nombre, Integer cantidadProducto, Integer precioDelProducto) {
    	
        productos.put(nombre, cantidadProducto);
        
        inventario.put(nombre, precioDelProducto);
        
    }

}