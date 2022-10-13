package Cine.gestiorAplicacion.tiendaAbst;

public class prueba {
    public static void name(String[] args) {
        //Create a new TiendaComida object and set its name
        TiendaComida tiendaComida = new TiendaComida("Tienda de comida");
        tiendaComida.setNombre("Tienda de comida");
        //Add a new product to the store
        tiendaComida.agregarProducto("Papas", 10);
        tiendaComida.agregarProducto("Gaseosa", 10);
        tiendaComida.agregarProducto("Caramelos", 10);
        tiendaComida.agregarProducto("Vino", 10);
        tiendaComida.agregarProducto("Chocolates", 10);
        tiendaComida.agregarProducto("Crispetas", 10");

        tiendaComida.agregarInventario("Papas", 10);
        tiendaComida.agregarInventario("Gaseosa", 10);
        tiendaComida.agregarInventario("Caramelos", 10);
        tiendaComida.agregarInventario("Vino", 10);
        tiendaComida.agregarInventario("Chocolates", 10);
        tiendaComida.agregarInventario("Crispetas", 10);


        //Print the name of the store
        System.out.println(tiendaComida.getNombre());
        //Print the name of the products
        System.out.println(tiendaComida.getProductos());
        
        //Print the quantity of the product
        System.out.println(tiendaComida.getProductos().values());





    }

}
