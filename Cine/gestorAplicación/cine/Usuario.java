package gestorAplicación.cine;

import java.util.ArrayList;
import java.util.HashMap; 

public class Usuario {
	
		private String Nombre;
		private int Cedula;
		private boolean Membresia;
		private int Saldo;
		private ArrayList<Boleta> Boletas = new ArrayList<Boleta>();  
		private HashMap<String,Integer> Carrito = new HashMap<String,Integer>();
		//private static ArrayList<Usuario> PrimeraVez= new ArrayList<Usuario>();
		
		public Usuario (String Nombre, int Cedula, int Saldo) {
			this.Nombre = Nombre;
			this.Cedula = Cedula;
			this.Membresia = false;
			this.Saldo = Saldo;
			
		}
		
		public Usuario (String Nombre, int Cedula, int Saldo, ArrayList<Boleta> Boletas) {
			this.Nombre = Nombre;
			this.Cedula = Cedula;
			this.Membresia = false;
			this.Saldo = Saldo;
			this.Boletas =Boletas;
			
		}
		
		public boolean verificarMembresia() {
			return this.Membresia;
			
		}
		
		public void comprarMembresia() {
			this.Membresia = true;
			
		}
		
		public String getNombre() {
			return 	this.Nombre;
			
		}
		
		public void setNombre(String Nombre) {
			this.Nombre = Nombre;
			
		}

		public int getCedula() {
			return 	this.Cedula;
			
		}
		
		public void setCedula(int Cedula) {
			this.Cedula = Cedula;
			
		}

		public int getSaldo() {
			return 	this.Saldo;
			
		}

		public void setSaldo(int Saldo) {
			this.Saldo = Saldo;
			
		}

		public void agregarSaldo(int Saldo) {
			this.Saldo += Saldo;
			
		}

		public void agregarBoleta(Boleta Boleta) {
			this.Boletas.add(Boleta);
			
		}

		public ArrayList<Boleta> getBoletas() {
			return this.Boletas;
			
		}

		public void setBoletas(ArrayList<Boleta> Boletas) {
			this.Boletas = Boletas;
			
		}

		public HashMap<String, Integer> getCarrito() {
			return this.Carrito;
			
		}

		public void setCarrito(HashMap<String, Integer> Carrito) {
			this.Carrito = Carrito;
			
		}

		public void agregarCarrito(String Nombre, int Cantidad) {
			this.Carrito.put(Nombre, Cantidad);
			
		}

		public void eliminarCarrito(String Nombre) {
			this.Carrito.remove(Nombre);
			
		}

		public void vaciarCarrito() {
			this.Carrito.clear();
			
		}	

		//add a Boleta to the list of Boletas
		public void addBoleta(Boleta boleta) {
			this.Boletas.add(boleta);
		}



		
	
		
}	

