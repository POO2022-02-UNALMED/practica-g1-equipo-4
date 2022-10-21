package IU;

import gestorAplicación.cine.Usuario;
import gestorAplicación.tiendaAbst.*;


import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Usuario usuario = new Usuario("Juan", 1152452 , 50000);
        //Create a new TiendaComida object and set its name
        TiendaComida tiendaComida = new TiendaComida("Tienda de comida");
        tiendaComida.setNombre("Comida Unal");
        //Add a new product and prices to the store Comida Unal
        tiendaComida.agregarMixto("Papas", 10, 5000);
        tiendaComida.agregarMixto("Papas con queso", 10, 6000);
        tiendaComida.agregarMixto("Papas con queso y tocino", 10, 7000);
        tiendaComida.agregarMixto("Crispetas", 10, 8000);
        tiendaComida.agregarMixto("Gaseosa", 10, 9000);


        //Create a new TiendaUN object and set its name
        TiendaUN tiendaUN = new TiendaUN("Tienda UN");
        //Add a new product to the store
        tiendaUN.agregarMixto("Camisetas", 10, 15);
        tiendaUN.agregarMixto("Pantalones", 10, 15);
        tiendaUN.agregarMixto("Termos", 10, 15);   
        tiendaUN.agregarMixto("Gorras", 10, 15);

        int opcion = 1;
        switch (opcion) {
            case 1:
            menuTienda(tiendaComida, tiendaUN, usuario);
            break;
        }
    }

    public static void menuTienda(TiendaComida tienda, TiendaUN tiendaUN, Usuario usuario) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Bienvenido a la tienda de comida del cine UNAL");
        System.out.println("1. Comprar productos");
        System.out.println("2. Salir");
        System.out.println("Ingrese una opción: ");
        int opcion = sc.nextInt();
        switch (opcion) {
            case 1:
                System.out.println("Productos disponibles: ");
                int i = 1;
                for (String producto : tienda.getProductos().keySet()) {
                    System.out.println(i+"."+producto + " - " + tienda.getInventario().get(producto));
                    i++;
                }
                System.out.println("Ingrese el numero del producto que desea comprar: ");
                String nombreProducto = sc.next();                
                if (nombreProducto.equals("1")) {
                    nombreProducto = "Papas";
                    System.out.println("Desea adicionar queso o tocino? (S/N)");
                    String opcion2 = sc.next();
                    if (opcion2.equals("S")) {
                        System.out.println("Desea adicionar tocino? (S/N)");
                        String opcion3 = sc.next();
                        if (opcion3.equals("S")) {
                            nombreProducto = "Papas con queso y tocino";
                        } else {
                            nombreProducto = "Papas con queso";
                        }
                    }
                } else if (nombreProducto.equals("2")) {
                    nombreProducto = "Papas con queso";
                }else if (nombreProducto.equals("3")) {
                    nombreProducto = "Gaseosa";
                }else if (nombreProducto.equals("4")) {
                    nombreProducto = "Papas con queso y tocino";
                } else if (nombreProducto.equals("5")) {
                    nombreProducto = "Crispetas";
                } 
                System.out.println("Ingrese la cantidad que desea comprar: ");
                int cantidad = sc.nextInt();
                if (tienda.getInventario().get(nombreProducto) >= cantidad) {
                    tienda.agregarInventario(nombreProducto, -cantidad);
                    usuario.setSaldo(usuario.getSaldo()-tienda.getProductos().get(nombreProducto)*cantidad);
                    System.out.println("Compra exitosa");
                } else {
                    System.out.println("No hay suficiente inventario");
                }
                menuTienda(tienda, tiendaUN, usuario);
                break;
            case 2:
                System.out.println("Gracias por su compra");
                break;
            default:
                System.out.println("Opción inválida");
                break;
        }
        sc.close();


        }

}   
    

