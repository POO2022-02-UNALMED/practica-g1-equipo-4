package Cine.gestorAplicación.cine;

public class Usuario {
	
		private String Nombre;
		private int Cedula;
		private Boolean Membresia;
		private int Saldo;
		
		public Usuario (String Nombre, int Cedula, int Saldo) {
			this.Nombre = Nombre;
			this.Cedula = Cedula;
			this.Membresia = false;
			this.Saldo = 0;
		}
		
		public Boolean verificarMembresia() {
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


		
}	

