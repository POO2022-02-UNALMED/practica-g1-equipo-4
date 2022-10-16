package Cine.gestorAplicación.cine;

public class Horario {
	private String HoraInicio;
	private String HoraFinal;
	
	public Horario(String HoraInicio, String HoraFinal) {
		this.HoraInicio = HoraInicio;
		this.HoraFinal = HoraFinal;
	}
	
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
