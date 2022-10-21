package gestorAplicación.tiendaAbst;

public class prueba {
    
    public static void main(String[] args) {

        //Create a new TiendaComida object and set its name
        TiendaComida tiendaComida = new TiendaComida("Tienda de comida");
        tiendaComida.setNombre("Comida Unal");
        //Add a new product to the store
        tiendaComida.agregarProducto("Papas", 10);
        tiendaComida.agregarProducto("Gaseosa", 10);
        tiendaComida.agregarProducto("Caramelos", 10);
        tiendaComida.agregarProducto("Vino", 10);
        tiendaComida.agregarProducto("Chocolates", 10);
        tiendaComida.agregarProducto("Crispetas", 10);

        tiendaComida.agregarInventario("Papas", 10);
        tiendaComida.agregarInventario("Gaseosa", 10);
        tiendaComida.agregarInventario("Caramelos", 10);
        tiendaComida.agregarInventario("Vino", 10);
        tiendaComida.agregarInventario("Chocolates", 10);
        tiendaComida.agregarInventario("Crispetas", 10);

        //Create a new TiendaUN object and set its name
        TiendaUN tiendaUN = new TiendaUN("Tienda de la UN");
        //Add a new product to the store
        tiendaUN.agregarMixto("Camisetas", 10, 15);
        tiendaUN.agregarMixto("Pantalones", 10, 15);
        tiendaUN.agregarMixto("Termos", 10, 15);   
        tiendaUN.agregarMixto("Gorras", 10, 15);


        //Print the name of the store
        System.out.println(tiendaComida.getNombre());
        //Print the name of the products
        System.out.println(tiendaComida.getProductos());
        
        //Print the quantity of the product
        System.out.println(tiendaComida.getProductos().values());

        //Print the name of the store
        System.out.println(tiendaUN.getNombre());

        //Print the name of the products
        for (String key : tiendaUN.getProductos().keySet()) {
            System.out.println(key);
        }




    }

}
