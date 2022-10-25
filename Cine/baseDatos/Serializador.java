/*package baseDatos;

import java.io.*;


<<<<<<< Updated upstream
import gestorAplicación.tiendaAbst.*;

import IU.*;
=======


>>>>>>> Stashed changes

public class Serializador {

		private static File rutaTemp = new File("Cine\\baseDatos\\temp"); //definimos la ruta de los archivos donde se serializaran los objetos
		
		public static void serializar(Usuario usuario) {
			
			FileOutputStream fos;
			
			ObjectOutputStream oos;
			
			File[] docs = rutaTemp.listFiles();
			
			PrintWriter pw;
			
			for (File file: docs) { //Iteramos en los archivos que hallan en la ruta para vaciarlos creando un printwiter
			
				try	{
					
					pw = new PrintWriter(file);
					
				}catch (FileNotFoundException e){
					
					e.printStackTrace();
					
				}
			}
			
			for(File file: docs) {
				if (file.getAbsolutePath().contains("Boletas")) {
					try {
						fos = new FileOutputStream(file);
						oos = new ObjectOutputStream(fos);
						oos.writeObject(usuario.getBoletas());
						}catch (FileNotFoundException e) {
							e.printStackTrace();
						}catch (IOException e) {
							e.printStackTrace();
						}
				}
			}
		}
}	
*/		