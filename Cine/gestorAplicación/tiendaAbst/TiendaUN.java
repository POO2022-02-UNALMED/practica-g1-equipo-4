package gestorAplicación.tiendaAbst;

import java.util.HashMap;
import java.util.Map;
import gestorAplicación.cine.Usuario;

public class TiendaUN extends Tienda {

    public TiendaUN(String nombre) {
        super(nombre);
        
    }

    protected Map<String, Integer> inventario = new HashMap<String, Integer >();
    protected Map<String, Integer> productos = new HashMap<String, Integer >();


    
    public void venderProducto(String nombre, Integer cantidad, Usuario usuario) {
        if (inventario.get(nombre) >= cantidad) {
            inventario.put(nombre, inventario.get(nombre) - cantidad);
            usuario.setSaldo(usuario.getSaldo() - (cantidad * inventario.get(nombre)));
            
        }   
    }

    public Map<String, Integer> getInventario() {
        return inventario;
        
    }

    public void setInventario(Map<String, Integer> inventario) {
        this.inventario = inventario;
        
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

    public void agregarInventario(String nombre, Integer cantidad) {
        inventario.put(nombre, cantidad);
        
    }

    public void agregarMixto (String nombre, Integer cantidadProducto, Integer precioDelProducto) {
        productos.put(nombre, cantidadProducto);
        inventario.put(nombre, precioDelProducto);
        
    }

    public int getPrecio(String nombre) {
        return productos.get(nombre);
        
    }

    @Override
    public void saludo() {
        System.out.println("Bienvenido a la tienda del cine UNAL");
        
    }
    
}