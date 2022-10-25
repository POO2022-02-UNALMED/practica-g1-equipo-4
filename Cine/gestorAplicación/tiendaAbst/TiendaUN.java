package gestorAplicación.tiendaAbst;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import gestorAplicación.cine.Usuario;

public class TiendaUN extends Tienda implements Serializable{
	//atributos
	private static final long serialVersionUID = 1L;

    public TiendaUN(String nombre) {
        super(nombre);
        
    }

    protected Map<String, Integer> inventario = new HashMap<String, Integer >();
    protected Map<String, Integer> productos = new HashMap<String, Integer >();


    //constructor
    public void venderProducto(String nombre, Integer cantidad, Usuario usuario) {
        if (productos.get(nombre) >= cantidad) {
            productos.put(nombre, productos.get(nombre) - cantidad);
            if (usuario.verificarMembresia()) {
                usuario.setSaldo(usuario.getSaldo() - (int)((cantidad * inventario.get(nombre))*0.3) );
            }
            else {
                usuario.setSaldo(usuario.getSaldo() - (cantidad * inventario.get(nombre)));
            }
        }
    }
//metodos get y set
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
// sobreescritura de metodo abstract
    @Override
    public void saludo() {
        System.out.println("Bienvenido a la tienda del cine UNAL");
        
    }
    
}