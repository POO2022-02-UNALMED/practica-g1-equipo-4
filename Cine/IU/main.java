package IU;

import gestorAplicación.tiendaAbst.*;
import gestorAplicación.cine.*;


// La funcionalidad de reembolso que tome la fecha del reembolso y la transforme al día de la semana correspondiente y lo
// compare con el día en el que se presenta la pélcula.


import java.util.Scanner;
import java.util.Map.Entry;
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
        tiendaComida.agregarMixto("Agua", 10, 1000);
        tiendaComida.agregarMixto("Perro Caliente", 10, 20000);


        //Create a new TiendaUN object and set its name
        TiendaUN tiendaUN = new TiendaUN("Tienda UN");
        //Add a new product to the store
        tiendaUN.agregarMixto("Camisetas", 10, 15);
        tiendaUN.agregarMixto("Pantalones", 10, 15);
        tiendaUN.agregarMixto("Termos", 10, 15);   
        tiendaUN.agregarMixto("Gorras", 10, 15);

        
        int opcion;
        
        do {
            System.out.println("---- Bienvenido al cine unal----");
            System.out.println("¿Que operación desea realizar? ");
            System.out.println("1. Comprar Boleta");
     
            System.out.println("2. Comprar comida");
           
            System.out.println("3. Reembolso");
            
            System.out.println("4. Encargar comida");
           
            System.out.println("5. Hacerse miembro VIP");
            
            System.out.println("6. Terminar");
           
            System.out.println("Por favor escoja una opción:");
            
            opcion = entrada.nextInt();
        
        
            switch (opcion) {
            	case 1: break;
            	case 2: comprar(tienda, usuario) break;
            	case 3:	break;
            	case 4: menuTienda(tiendaComida, tiendaUN, usuario); break;
            	case 5: break;
            	case 6: salirDelSistema(usuario); break;
            }
          } while (opcion != 6); 
       }

    public static void menuTienda(TiendaComida tiendaComida, TiendaUN tiendaUN, Usuario usuario) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Bienvenido a la tienda de comida del cine UNAL");
        System.out.println("1. Ver Menú de la tienda");
        System.out.println("2. Ver souvenirs de la tienda UN");
        System.out.println("3. Encargar comida durante la funcion"); 
        System.out.println("4. Salir");
        int opcion = sc.nextInt();
        do{
        switch (opcion) {
            case 1: //Menu de la tienda de comida
            tiendaComida.saludo();
            System.out.println("Productos disponibles:");
            for (Entry<String, Integer> entry : tiendaComida.getInventario().entrySet()) {
                System.out.println(entry.getKey() + " - " + entry.getValue());
            }
            System.out.println("Desea comprar algo? (1. Si, 2. No)");
            int opcion2 = sc.nextInt();
            if (opcion2 == 1) {
                comprar(tiendaComida, usuario);
            } else {
                menuTienda(tiendaComida, tiendaUN, usuario);
            }
            break;

            case 2:// souvenirs de la tienda UN
            int i = 1;
            System.out.println("En la tienda UNAL ofrecemos los siguientes productos:");
            for (Entry<String, Integer> entry : tiendaUN.getInventario().entrySet()) {
                System.out.println(i+". "+entry.getKey() + " - " + entry.getValue());
                i++;

            }
            
            System.out.println("Desea comprar algo? (1. Si, 2. No)");
            int opcion3 = sc.nextInt();
            if (opcion3 == 1) {
                comprar(tiendaUN, usuario);
            } else {
                break;
            }
            break;

            case 3: //Encargar comida durante la funcion
            System.out.println("Hola! Esta nueva opción te permite encargar comida facilmente y te será traída"+
            " durante la función por uno de nuestros repartidores.");
            System.out.println("Solo debes ingresar el nombre del producto que deseas y la cantidad");
            System.out.println("¿Qué producto deseas?");
            String producto = sc.next();
            System.out.println("¿Cuántos deseas?");
            int cantidad = sc.nextInt();
            if (cantidad < tiendaComida.getInventario().get(producto)) {
                System.out.println("Su pedido ha sido registrado, en unos minutos llegará a su asiento");
                tiendaComida.getInventario().put(producto, tiendaComida.getInventario().get(producto) - cantidad);
                usuario.agregarCarrito(producto, cantidad);
                tiendaComida.agregarColaPedidos(usuario);
            } else {
                System.out.println("Lo sentimos, no tenemos suficiente producto en inventario");
            }
            break;
        }
        }while(opcion != 4);
    }

    public static void comprar (Tienda tienda, Usuario usuario) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Ofrecemos los siguientes productos:");
        int i = 1;
        for (Entry<String, Integer> entry : tienda.getInventario().entrySet()) {
            System.out.println(i+". "+entry.getKey() + " - $: " + entry.getValue());
            i++;
        }
        
        System.out.println("ingrese el nombre del producto que desea comprar: ");
        String producto = sc.nextLine();
        System.out.println("ingrese la cantidad que desea comprar: ");
        int cantidad = sc.nextInt();
        tienda.venderProducto(producto, cantidad, usuario);
        usuario.agregarCarrito(producto, cantidad);
        System.out.println("Desea comprar algo mas? (1. Si, 2. No)");
        int opcion2 = sc.nextInt();
        if (opcion2 == 1) {
            comprar(tienda, usuario);
        } else {
            System.out.println("Factura: ");
            System.out.println("Nombre: "+usuario.getNombre());
            System.out.println("Cedula: "+usuario.getCedula());
            System.out.println("Productos: ");
            System.out.println("Producto - Cantidad - Precio");
            for (Entry<String, Integer> entry : usuario.getCarrito().entrySet()) {
                System.out.println(entry.getKey() + " - " + entry.getValue() + " - " + tienda.getPrecio(entry.getKey()));
            }
            
            System.out.println("Su saldo actual es: "+usuario.getSaldo());
            
            menuTienda((TiendaComida) tienda, (TiendaUN) tienda, usuario);
        }
    }
    //Comprar entrada
    public void comprarEntrada(Asiento asiento, Boleta boleta, Sala sala, Usuario usuario) {
        Scanner sc = new Scanner (System.in);
        int precio = 0;
        
        if (asientos == 0) {
            System.out.println("No hay asientos");
        } else {
            System.out.println("Indicar tipo de membresia: Regular = A / VIP = B");
            String tipoMembresia = sc.nextLine();
            System.out.println("Indique cuantas entradas desea: ");
            int cantidadEntradas = sc.nextInt();
            if (cantidadEntradas > asientos) {
                System.out.println("NO HAY ASIENTOS LIBRES");
            } else {
                System.out.println("Elija metodo de pago: E - Efectivo / T - Tarjeta");
                String metodoPago = sc.nextLine();
                if (tipoMembresia.equalsIgnoreCase("A")) {
                    precio = 0;
                }
                if (tipoMembresia.equalsIgnoreCase("B")) {
                    precio = 0;
                }
                if (metodoPago.equalsIgnoreCase("T")) {
                    precio = (int) (precio + precio*0.18);
                    System.out.println("VENTA REALIZADA. PRECIO FINAL: " + precio);
                }
                asientos = asientos - cantidadEntradas;
                System.out.println("QUEDAN " + asientos + "asientos.");
            }
        }
    //metodo estatico que cierra el sistema de forma correcta
    private static void salirDelSistema(Usuario usuario) {
    	System.out.println("Vuelva Pronto");
    	//aqui iria la funcion del serializador
    	System.exit(0);
    }
}



    

