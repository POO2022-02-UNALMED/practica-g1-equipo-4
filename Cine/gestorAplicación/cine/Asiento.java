package gestorAplicación.cine;

import java.util.ArrayList;

public class Asiento {
	
	private boolean[] asientos;

	public Asiento() {
		
		asientos = new boolean[200];
		
		for (int i = 0; i < 200; i++) {
			
			asientos[i] = false;
		}
		
	}
	
	public boolean[] getAsientos() {
		
		return asientos;
		
	}
	
	public String comprarAsiento(String n_asiento) {
		
		String[] a = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
		
		ArrayList<String> lista = new ArrayList<String>();
		
		for (String e: a) {
			
			lista.add(e);
			
		}
		
		String inicial = n_asiento.substring(0,1);
		
		int numeros =  Integer.parseInt(n_asiento.substring(1));
		
		int posicion = numeros - 1 + lista.indexOf(inicial)*20;
		
		if (asientos[posicion] == false) {
			
			asientos[posicion] = true;
					
			return "Asiento " + n_asiento + " comprado con éxito.";
			
		}
		
		else {
			
			return "Asiento " + n_asiento + " ocupado.";
			
		}
		
	}
	
	public String compraAsientos(String x) {
		
		String[] silla = x.split(", ");
		
		boolean q = true;
		
		ArrayList<String> falla = new ArrayList<String>();
		
		for (String e: silla) {
			
			String inicial = e.substring(0,1);
			
			int numeros =  Integer.parseInt(e.substring(1));
			
			int posicion = numeros - 1 + e.indexOf(inicial)*20;
			
			if (asientos[posicion] == true) {
				
				q = false;
				
				falla.add(e);
			}
			
		}
		
		if (q) {
			for (String e: silla) {
				
				comprarAsiento(e);
				
			}
			
			return "Asientos " + x + " confirmados, gracias por su compra.";
			
		}
		
		else if (falla.size() == 1){
			
			return "No es posible reservar el asiento " + falla.get(0) + "; ya se encuentra ocupado.";
			
		}
		
		else {
			
			String w = falla.get(0);
			
			for (int i = 1; i < falla.size(); i++) {
				
				w = w + ", " + falla.get(i);
				
			}
			
			return "No es posible reservar los asientos " + w + "; ya se encuentran ocupados.";
			
		}
		
	}  
   
}
