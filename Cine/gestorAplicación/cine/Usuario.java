package Cine.gestiorAplicacion.cine;

public class Usuario {
	public class Usuario {
		private String Nombre;
		private int Cedula;
		private Boolean Membresia;
		private int veces;
		
		public Usuario (String Nombre, int Cedula, Boolean Membresia) {
			this.Nombre = Nombre;
			this.Cedula = Cedula;
			this.Membresia = Membresia;
		
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
		
		
}
