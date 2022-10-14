package Cine.gestiorAplicacion.cine;

import java.util.Scanner;

public class Asiento {
  
  private String Letra;
  
  private int Numero;
  
  static Scanner entrada = new Scanner(System.in);
  
  public static void main(String[] args) {
	  
	  int t = 1, fila, columna;
	  
	  int [][] asiento = new int [10][20];
	  
	  while (t <= 200) {
		  
		  System.out.println( "Ingrese el número de fila (1-10)");
		  
		  fila = entrada.nextInt();
		  
		  System.out.println( "Ingrese el número de columna (1-20)");
		  
		  columna = entrada.nextInt();
		  
		  if (asiento [fila - 1] [columna - 1] == 0) {
			  
			  asiento [fila - 1] [columna - 1] = 1;
			  
			  t = t + 1;
			  
			  System.out.println( "Reserva exitosa");			  
			  
		  }else
			  System.out.println( "Asiento ocupado");
		  		  		  
	  }
	  for (int i = 0; i < 10; i++) {
		  
		  for (int j = 0; j < 20; j++)
			  
			  System.out.println(asiento[i][j] + "\t");
		  
		  System.out.println();
	  }
	  
  }
  
   
}
