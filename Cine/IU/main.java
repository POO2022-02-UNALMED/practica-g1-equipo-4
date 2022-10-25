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
        Pelicula pelicula5 = new Pelicula("Matrix", "Accion" );
        Pelicula pelicula6 = new Pelicula("Jhon Wick", "Accion" );
        Pelicula pelicula7 = new Pelicula("Memento", "Drama" );
        Pelicula pelicula8 = new Pelicula("Nemo", "Infatil" );
        Pelicula pelicula9 = new Pelicula("El Conjuro", "Terror" );
        Pelicula pelicula10 = new Pelicula("El Paseo", "Comedia" );
        Pelicula pelicula11 = new Pelicula("Terminator", "Accion" );
        Pelicula pelicula12 = new Pelicula("Troya", "Accion" );
        Pelicula pelicula13= new Pelicula("Madagascar", "Infantil" );
        Pelicula pelicula14= new Pelicula("Los Pitufos", "Infantil" );
        Pelicula pelicula15= new Pelicula("Baki", "Accion" );
        Pelicula pelicula16= new Pelicula("Your Name", "Drama" );
        Pelicula pelicula17= new Pelicula("Taxi Driver", "Accion" );
        Pelicula pelicula18= new Pelicula("El Transportador", "Accion" );
        Pelicula pelicula19= new Pelicula("Transformers", "Accion" );
        Pelicula pelicula20= new Pelicula("Interestelar", "Ciencia Ficcion" );


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

        Map<Pelicula, Horario> cartelera2 = new HashMap<Pelicula, Horario>();
        cartelera2.put(pelicula5, horario);
        cartelera2.put(pelicula6, horario2);
        cartelera2.put(pelicula7, horario3);
        cartelera2.put(pelicula8, horario4);

        Map<Pelicula, Horario> cartelera3 = new HashMap<Pelicula, Horario>();
        cartelera3.put(pelicula9, horario);
        cartelera3.put(pelicula10, horario2);
        cartelera3.put(pelicula11, horario3);
        cartelera3.put(pelicula12, horario4);

        Map<Pelicula, Horario> cartelera4 = new HashMap<Pelicula, Horario>();
        cartelera4.put(pelicula13, horario);
        cartelera4.put(pelicula14, horario2);
        cartelera4.put(pelicula15, horario3);
        cartelera4.put(pelicula16, horario4);

        Map<Pelicula, Horario> cartelera5 = new HashMap<Pelicula, Horario>();
        cartelera5.put(pelicula17, horario);
        cartelera5.put(pelicula18, horario2);
        cartelera5.put(pelicula19, horario3);
        cartelera5.put(pelicula20, horario4);


        boolean[] arr = new boolean[28];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = false;
        }

        Map<String, boolean[]>  Asientos = new HashMap<String, boolean[]>();

        //fill Asientos with the movies names and the array of seats
        Asientos.put("Batman", arr.clone());
        Asientos.put("Avengers", arr.clone());
        Asientos.put("Spiderman", arr.clone());
        Asientos.put("Superman", arr.clone());

        Map<String, boolean[]>  Asientos2 = new HashMap<String, boolean[]>();

        //fill Asientos with the movies names and the array of seats
        Asientos2.put("Matrix", arr.clone());
        Asientos2.put("Jhon Wick", arr.clone());
        Asientos2.put("Memento", arr.clone());
        Asientos2.put("Nemo", arr.clone());

        Map<String, boolean[]>  Asientos3 = new HashMap<String, boolean[]>();

        //fill Asientos with the movies names and the array of seats
        Asientos3.put("El Conjuro", arr.clone());
        Asientos3.put("El Paseo", arr.clone());
        Asientos3.put("Terminator", arr.clone());
        Asientos3.put("Troya", arr.clone());
       
        Map<String, boolean[]>  Asientos4 = new HashMap<String, boolean[]>();

        //fill Asientos with the movies names and the array of seats
        Asientos4.put("Madagascar", arr.clone());
        Asientos4.put("Los Pitufos", arr.clone());
        Asientos4.put("Baki", arr.clone());
        Asientos4.put("Your Name", arr.clone());

        Map<String, boolean[]>  Asientos5 = new HashMap<String, boolean[]>();

        //fill Asientos with the movies names and the array of seats
        Asientos5.put("Taxi Driver", arr.clone());
        Asientos5.put("El Transportador", arr.clone());
        Asientos5.put("Transformers", arr.clone());
        Asientos5.put("Interestelar", arr.clone());

        //Create Sala
        Sala sala = new Sala("Sala", Asientos, cartelera);
        Sala sala2 = new Sala("Sala", Asientos2, cartelera2);
        Sala sala3 = new Sala("Sala", Asientos3, cartelera3);
        Sala sala4 = new Sala("Sala", Asientos4, cartelera4);
        Sala sala5 = new Sala("Sala", Asientos5, cartelera5);
        
        //Create Dia
        Dia dia = new Dia("Lunes", sala);
        Dia dia2 = new Dia("Martes", sala2);
        Dia dia3 = new Dia("Miercoles", sala3);
        Dia dia4 = new Dia("Jueves", sala4);
        Dia dia5 = new Dia("Viernes", sala5);

        ArrayList<Dia> dias = new ArrayList<Dia>();
        dias.add(dia);
        dias.add(dia2);
        dias.add(dia3);
        dias.add(dia4);
        dias.add(dia5);
        menu(sala, usuario, tiendaComida, tiendaUN, dias);
        
        
    }
    

    //Create a main menu for the user
    public static void menu(Sala sala, Usuario usuario, TiendaComida tiendaComida, TiendaUN tiendaUN, ArrayList<Dia> dias) {
        boolean cond = true;
        while (cond == true){
            System.out.println("\r\n"
                    + "░█████╗░██╗███╗░░██╗███████╗  ██╗░░░██╗███╗░░██╗\r\n"
                    + "██╔══██╗██║████╗░██║██╔════╝  ██║░░░██║████╗░██║\r\n"
                    + "██║░░╚═╝██║██╔██╗██║█████╗░░  ██║░░░██║██╔██╗██║\r\n"
                    + "██║░░██╗██║██║╚████║██╔══╝░░  ██║░░░██║██║╚████║\r\n"
                    + "╚█████╔╝██║██║░╚███║███████╗  ╚██████╔╝██║░╚███║\r\n"
                    + "░╚════╝░╚═╝╚═╝░░╚══╝╚══════╝  ░╚═════╝░╚═╝░░╚══╝");
            System.out.println("---- Bienvenido al cine unal----");
            System.out.println("¿Qué operación desea realizar? (Ingrese el número de la operación)");
            System.out.println("1. Comprar Boleta");
            System.out.println("2. Comprar comida");
            System.out.println("3. Comprar mercancia");
            System.out.println("4. Hacerse miembro VIP");
            System.out.println("5. Reembolso");
            System.out.println("6. Terminar");
            System.out.println("Por favor escoja una opción:");
            
            Scanner sc = new Scanner(System.in);
            int opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    comprarEntrada(dias, usuario);
                    break;
                case 2:
                    comprarComida(tiendaComida, usuario);
                    break;
                case 3: 
                    comprarMercancia(tiendaUN, usuario);
                    break;
                case 4:
                    VIP(tiendaComida, tiendaUN, usuario);
                    break;
                case 5: 
                    reembolso(usuario);
                    break;
                case 6:
                    System.out.println("Gracias por su visita");
                    salirDelSistema(usuario);
                    break;
                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }
    }

    public static void comprarComida(TiendaComida tiendaComida, Usuario usuario) {
        tiendaComida.saludo();        
        Scanner sc = new Scanner(System.in);
        System.out.println("Ofrecemos los siguientes productos:");
        int i = 1;
        for (Entry<String, Integer> entry : tiendaComida.getInventario().entrySet()) {
            System.out.println(i+". "+entry.getKey() + " - $: " + entry.getValue());
            i++;
        }
        
        System.out.println("ingrese el nombre del producto que desea comprar: ");
        String producto = sc.nextLine();
        System.out.println("ingrese la cantidad que desea comprar: ");
        int cantidad = sc.nextInt();

        int saldo = usuario.getSaldo();       
        
        if (tiendaComida.getInventario().containsKey(producto)) {
            int precio = tiendaComida.getInventario().get(producto);
            int total = precio * cantidad;
            if (saldo >= total) {
                tiendaComida.venderProducto(producto, cantidad, usuario);
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Producto no disponible");
        }
        
    }

    public static void  comprarMercancia(TiendaUN tienda, Usuario usuario ){
        tienda.saludo();        
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

        int saldo = usuario.getSaldo();       
        
        if (tienda.getInventario().containsKey(producto)) {
            int precio = tienda.getInventario().get(producto);
            int total = precio * cantidad;
            if (saldo >= total) {
                tienda.venderProducto(producto, cantidad, usuario);
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Producto no disponible");
        }
    }

    // public static void comprar (Tienda tienda, Usuario usuario) {
    //     Scanner sc = new Scanner(System.in);
    //     System.out.println("Ofrecemos los siguientes productos:");
    //     int i = 1;
    //     for (Entry<String, Integer> entry : tienda.getInventario().entrySet()) {
    //         System.out.println(i+". "+entry.getKey() + " - $: " + entry.getValue());
    //         i++;
    //     }
        
    //     System.out.println("ingrese el nombre del producto que desea comprar: ");
    //     String producto = sc.nextLine();
    //     System.out.println("ingrese la cantidad que desea comprar: ");
    //     int cantidad = sc.nextInt();
    //     tienda.venderProducto(producto, cantidad, usuario);
    //     usuario.agregarCarrito(producto, cantidad);
    //     System.out.println("Desea comprar algo mas? (1. Si, 2. No)");
    //     int opcion2 = sc.nextInt();
    //     if (opcion2 == 1) {
    //         comprar(tienda, usuario);
    //     } else {
    //         System.out.println("Factura: ");
    //         System.out.println("Nombre: "+usuario.getNombre());
    //         System.out.println("Cedula: "+usuario.getCedula());
    //         System.out.println("Productos: ");
    //         System.out.println("Producto - Cantidad - Precio");
    //         for (Entry<String, Integer> entry : usuario.getCarrito().entrySet()) {
    //             System.out.println(entry.getKey() + " - " + entry.getValue() + " - " + tienda.getPrecio(entry.getKey()));
    //         }
            
    //         System.out.println("Su saldo actual es: "+usuario.getSaldo());
            
    //        
    //     }
    // }


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
        System.out.println("Ingrese el NOMBRE de la pelicula que desea ver: ");
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
        Boleta boleta = new Boleta(usuario, pelicula, diaTemp.getSala() , asientosComprados, diaTemp.getSala().getCartelera().get(pelicula), diaTemp.getSala().getNombre());
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

    private static void reembolso(Usuario usuario){
        boolean vip = usuario.verificarMembresia();
        int devolucion;
        if (vip) {
            devolucion= (int) (10000 - 10000*0.40);
        } else {
            devolucion= 10000;
        }
        if (usuario.getBoletas().isEmpty()){
            System.out.println("No tiene boletas compradas");
        }else{
            int [] boletas = usuario.getBoletas().get(0).getAsiento();
            Scanner sc = new Scanner(System.in);
            System.out.println("Está apunto de reembolsar una boleta");
            System.out.println("Desea continuar");
            System.out.println("1. Si 2. No");
            int opcion = sc.nextInt();
            if (opcion == 1){

                System.out.println("Estas son las boletas que tiene compradas: ");
                for (int i = 0; i < usuario.getBoletas().size(); i++) {
                    System.out.println((i+1)+". "+usuario.getBoletas().get(i).getPelicula());
                    for (int j = 0; j < boletas.length; j++) {
                        System.out.println("Asiento: "+usuario.getBoletas().get(i).getAsiento()[j]);

                    }
                }
                System.out.println("Ingrese el NOMBRE de la pelicula que desea reembolsar");
                String pelicula = sc.next();
                System.out.println("Ingrese el numero del asiento que desea reembolsar");
                int asiento = sc.nextInt();

                for (int i = 0; i < usuario.getBoletas().size(); i++) {
                    if (usuario.getBoletas().get(i).getPelicula().equals(pelicula)){
                        for (int j = 0; j < usuario.getBoletas().get(i).getAsiento().length; j++) {
                            if (usuario.getBoletas().get(i).getAsiento()[j] == asiento){          
                                usuario.setSaldo(usuario.getSaldo() + devolucion);
                                System.out.println("Se ha reembolsado el asiento: "+asiento);
                                System.out.println("Su saldo actual es: "+usuario.getSaldo());
                                boolean[] nuevo = new boolean[28];
                                for (int q = 0; q < nuevo.length; q++) {
                                    for (int h = 0; h < usuario.getBoletas().get(i).getAsiento().length; h++)
                                        if (usuario.getBoletas().get(i).getAsiento()[h] == q && usuario.getBoletas().get(i).getAsiento()[j]!=q){
                                            nuevo[q-1] = true;
                                            System.out.println(usuario.getBoletas().get(i).getAsiento()[j]-1);
                                        }else{
                                            nuevo[q] = false;
                                        }
                                Map<String, boolean[]>  asientoextra = new HashMap<String, boolean[]>();
                                asientoextra.put(pelicula, nuevo);    
                                usuario.getBoletas().get(0).getSala().setAsientos(asientoextra);
                                System.out.println("Lamentamos tu partida, esperamos que vuelvas a elegirnos para tu proxima experiencia");
                                }
                            }
                        }
                    }
                }
            }
        }
    }      
}




    

