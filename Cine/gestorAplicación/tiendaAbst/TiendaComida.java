package gestorAplicación.tiendaAbst;

import java.io.Serializable;

import java.util.HashMap;
import java.util.Map;
import gestorAplicación.cine.Usuario;

public class TiendaComida extends Tienda implements Serializable{
	
	private static final long serialVersionUID = 1L;

    public TiendaComida(String nombre) {
        super(nombre);
        
    }
    
    private Map <String, Integer> productos = new HashMap <String, Integer>();  // producto - cantidad en inventario
    private Map <String, Integer> inventario = new HashMap <String, Integer>(); // producto - precio
    private Map <Integer, Usuario> colaPedidos = new HashMap <Integer, Usuario>();     //  - usuario
    
    public void venderProducto(String nombre, Integer cantidad, Usuario usuario) {
        if (inventario.get(nombre) >= cantidad) {
            inventario.put(nombre, inventario.get(nombre) - cantidad);
            if (usuario.verificarMembresia()) {
                usuario.setSaldo(usuario.getSaldo() - (int)((cantidad * inventario.get(nombre))*0.40) );
            }
            else {
                usuario.setSaldo(usuario.getSaldo() - (cantidad * inventario.get(nombre)));
            }
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
    
    
    public int getPrecio(String nombre) {
        return productos.get(nombre);
        
    }

    public Map<Integer, Usuario> getColaPedidos() {
        return colaPedidos;
        
    }

    public void agregarColaPedidos(Usuario usuario) {
        // check if repartidor is available in repartidores[]
        // if available, remove repartidor from repartidores[]
        // else, add pedido to colaPedidos
        if (colaPedidos.size()<4) {
            colaPedidos.put(colaPedidos.size(), usuario);
       
        }
        else {
            System.out.println("No hay repartidores disponibles");
            
        }
            
    }

    @Override
    public void saludo() {
        System.out.println("Bienvenido a la tienda de comida del cine UNAL");
        
    }

    

}