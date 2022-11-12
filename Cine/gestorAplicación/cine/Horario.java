package gestorAplicación.cine;

import java.io.*;

public class Horario implements Serializable{
	//atributos
	private static final long serialVersionUID = 1L;
	
	private String HoraInicio;
	
	private String HoraFinal;
	//constructor
	public Horario(String HoraInicio, String HoraFinal) {
		this.HoraInicio = HoraInicio;
		this.HoraFinal = HoraFinal;
		
	}
	//metodos get y set
	public String getHoraInicio() {
		return 	this.HoraInicio;
		
	}
	
	public String getHoraFinal() {
		return 	this.HoraFinal;
		
	}
	
	public void setHoraInicio(String HoraInicio) {
		this.HoraInicio = HoraInicio;
		
	}
	
	public void setHoraFinal(String HoraFinal) {
		this.HoraFinal = HoraFinal;
		
	}    
}