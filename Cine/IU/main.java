package IU;

import gestorAplicación.tiendaAbst.*;
import gestorAplicación.cine.*;

import java.io.Serializable;
import java.util.ArrayList;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;

// La funcionalidad de reembolso que tome la fecha del reembolso y la transforme al día de la semana correspondiente y lo
// compare con el día en el que se presenta la pélcula.

public class main implements Serializable{
	
    public static void main(String[] args) {

        if (true){
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
        
        //Create Peliculas
        Pelicula pelicula = new Pelicula("Avengers", "Accion" );
        Pelicula pelicula2 = new Pelicula("Spiderman", "Accion" );
        Pelicula pelicula3 = new Pelicula("Batman", "Accion" );
        Pelicula pelicula4 = new Pelicula("Superman", "Accion" );

        //Create Horarios
        Horario horario = new Horario("12:00", "14:00");
        Horario horario2 = new Horario("14:00", "16:00");
        Horario horario3 = new Horario("18:00", "20:00");
        Horario horario4 = new Horario("16:00", "18:00");

        //Create Cartelera
        Map<Pelicula, Horario> cartelera = new HashMap<Pelicula, Horario>();
        cartelera.put(pelicula, horario);
        cartelera.put(pelicula2, horario2);
        cartelera.put(pelicula3, horario3);
        cartelera.put(pelicula4, horario4);

        boolean[] arr = new boolean[28];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = false;
        }
        Map<String, boolean[]>  Asientos = new HashMap<String, boolean[]>();
        //fill Asientos with the movies names and the array of seats
        Asientos.put("Batman", arr);
        Asientos.put("Avengers", arr);
        Asientos.put("Spiderman", arr);
        Asientos.put("Superman", arr);

        //Create Sala
        Sala sala = new Sala("Sala", Asientos, cartelera);

        //Create Dia
        Dia dia = new Dia("Lunes", sala);
        Dia dia2 = new Dia("Martes", sala);
        Dia dia3 = new Dia("Miercoles", sala);
        Dia dia4 = new Dia("Jueves", sala);
        Dia dia5 = new Dia("Viernes", sala);

        ArrayList<Dia> dias = new ArrayList<Dia>();
        dias.add(dia);
        dias.add(dia2);
        dias.add(dia3);
        dias.add(dia4);
        dias.add(dia5);
        menu(sala, usuario, tiendaComida, tiendaUN, dias);
        }
        
    }

    //Create a main menu for the user
    public static void menu(Sala sala, Usuario usuario, TiendaComida tiendaComida, TiendaUN tiendaUN, ArrayList<Dia> dias) {
        System.out.println("Bienvenido a Cine UN");
        System.out.println("---- Bienvenido al cine unal----");
        System.out.println("¿Qué operación desea realizar? (Ingrese el número de la operación)");
        System.out.println("1. Comprar Boleta");
        System.out.println("2. Comprar comida");
        System.out.println("3. Reembolso");
        System.out.println("4. Hacerse miembro VIP");
        System.out.println("5. Terminar");
        System.out.println("Por favor escoja una opción:");
        
        Scanner sc = new Scanner(System.in);
        int opcion = sc.nextInt();

        switch (opcion) {
            case 1:
                comprarEntrada(dias, usuario);
                break;
            case 2:
                menuTienda(tiendaComida, tiendaUN, usuario);
                break;
            case 3:
                //reembolso(usuario);
                break;
            case 4:
                VIP(tiendaComida, tiendaUN, usuario);
                break;
            case 5:
                System.out.println("Gracias por su visita");
                salirDelSistema(usuario);
                break;
            default:
                System.out.println("Opción no válida");
                break;
        }
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
            sc.close();
            break;

            case 3: 
            comidaAsiento(usuario, tiendaComida);

            
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


    public static void comidaAsiento (Usuario usuario, TiendaComida tiendaComida){
        Scanner sc = new Scanner(System.in);
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
    }



    // -------------------------Comprar entrada-----------------------------

    public static void comprarEntrada(ArrayList<Dia> Dias, Usuario usuario) {
        boolean vip = usuario.verificarMembresia();
        Scanner sc = new Scanner (System.in);
        int precio = 0;
        System.out.println("Bienvenido a la compra de entradas");
        
        System.out.println("¿Cúantas entradas desea comprar?");
        int cantidad = sc.nextInt();
        
        System.out.println("Ingrese el número del día de la semana que desea comprar la entrada?");
        System.out.println("1. Lunes");
        System.out.println("2. Martes");
        System.out.println("3. Miercoles");
        System.out.println("4. Jueves");
        System.out.println("5. Viernes");
        int dia = sc.nextInt();    

        Dia diaTemp = Dias.get(dia-1);

        System.out.println("Para ese día tenemos las siguientes Peliculas:");
        int i = 1;
        for (Map.Entry<Pelicula, Horario> entry : diaTemp.getSala().getCartelera().entrySet()) {
            System.out.println(i+" "+entry.getKey().getnombre() + " - " + entry.getValue().getHoraInicio()+" - "+entry.getValue().getHoraFinal() );
            i++;
        }
        System.out.println("Ingrese el nombre de la pelicula que desea ver: ");
        String pelicula = sc.next();
        boolean[] asientos = diaTemp.getSala().getAsientos().get(pelicula);
        System.out.println("Los asientos disponibles son: ");

        // Imprimir asientos disponibles por filas de 7
        int exitos = 0;
        int [] asientosComprados = new int [cantidad];

        while(exitos < cantidad){
        int j = 0;
        System.out.println("\t - \t - Pantalla - \t - \t");
        for (int k = 0; k < asientos.length; k++) {
            if (asientos[k] == false) {
                System.out.print(k+1+"\t");
                j++;
            }else{
                System.out.print("X\t");
                j++;
            }
            if (j == 7) {
                System.out.println();
                j = 0;
            }
        }
        System.out.println();
        System.out.println("Ingrese el número del asiento que desea: ");
        int asiento = sc.nextInt();
        if (asientos[asiento-1] == false) {
            asientos[asiento-1] = true;
            System.out.println("Asiento reservado");
            if (vip) {
                precio = (int) (10000 - 10000*0.40);
            } else {
                precio = 10000;
            }
            System.out.println("El precio de la entrada es: "+precio);
            System.out.println("¿Desea comprar la entrada? (1. Si, 2. No)");
            int opcion = sc.nextInt();
            if (opcion == 1) {
                if (usuario.getSaldo() >= precio) {
                    usuario.setSaldo(usuario.getSaldo() - precio);
                    System.out.println("Su saldo actual es: "+usuario.getSaldo());
                    System.out.println("Gracias por su compra");
                    asientosComprados[exitos] = asiento;
                    exitos++;
                } else {
                    System.out.println("Lo sentimos, no tiene suficiente saldo para comprar la entrada");
                    asientos[asiento-1] = false;
                }
            } else {
                System.out.println("Gracias por su visita");
                asientos[asiento-1] = false;
            }
        } else {
            System.out.println("Lo sentimos, ese asiento ya está ocupado");

        }
    }

        System.out.println("Factura: ");
        System.out.println("Nombre: "+usuario.getNombre());
        System.out.println("Cedula: "+usuario.getCedula());
        System.out.println("Pelicula: "+pelicula);
        System.out.println("Dia: "+diaTemp.getnombreDelDiaDeLaSemana() );
        System.out.println("Asientos: ");
        for (int k = 0; k < asientosComprados.length; k++) {
            System.out.println(asientosComprados[k]);
        }
        System.out.println("Su saldo actual es: "+usuario.getSaldo());    
        Boleta boleta = new Boleta(usuario,  pelicula, diaTemp.getnombreDelDiaDeLaSemana(), asientosComprados, diaTemp.getSala().getCartelera().get(pelicula), diaTemp.getSala().getNombre());
        usuario.addBoleta(boleta);
        System.out.println("Gracias por su compra\n Volviendo al menú principal");
        

    }
    
    //metodo estatico que cierra el sistema de forma correcta
    private static void salirDelSistema(Usuario usuario) {
    	System.out.println("Vuelva Pronto");
    	//aqui iria la funcion del serializador
    	System.exit(0);
    }

    private static void VIP(TiendaComida tiendaComida, TiendaUN tiendaUN, Usuario usuario) {
	Scanner sc = new Scanner(System.in);
	System.out.println("Esta es la oportunidad para que pueda vivir una experiencia mejorada siendo VIP");
	System.out.println("Estos son los beneficios de volverse cliente VIP");
        System.out.println("Descuentos en la tienda UNAL");
        System.out.println("\t Cliente regular\t Cliente VIP");
        for (Entry<String, Integer> entry : tiendaUN.getInventario().entrySet()) {
            System.out.println(entry.getKey()+"\t"+ entry.getValue()+"\t" + (entry.getValue()*0.7 ));}
        System.out.println("Descuentos en comida");
        System.out.println("\t Cliente regular\t Cliente VIP");
        for (Entry<String, Integer> entry : tiendaComida.getInventario().entrySet()) {
            System.out.println(entry.getKey() + "\t" + entry.getValue() +"\t"+ (entry.getValue()*0.7));
        }
	System.out.println("Adicionalmente a esto, se tendra un descuento del  40% en la compra de tus boletas");
	System.out.println("Volverse VIP tiene un costo de $30000");
	System.out.println("Desea volverse cliente VIP? (1. Si, 2. No)");
	int opcion1 = sc.nextInt();
	if (opcion1 == 1) {
	    if(usuario.getSaldo()>=30000) {
            usuario.comprarMembresia();
	       	System.out.println("Se ha convertido en miembor VIP del cine unal"); 
            System.out.println("Su saldo actual es: "+usuario.getSaldo()); 
        }else {System.out.println("Saldo insuficente para volverse VIP");}
	       }
	    else {System.out.println("Esperamos que siga disfrutando de nuestros servicios ");}
	    }

        
}

    

