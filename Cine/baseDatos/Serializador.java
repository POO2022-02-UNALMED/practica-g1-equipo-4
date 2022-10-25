package baseDatos;

import java.io.*;

import gestorAplicación.cine.*;

import IU.*;

public class Serializador {

		private static File ruta = new File("Cine\\baseDatos\\temp"); //definimos la ruta de los archivos donde se serializaran los objetos
		
		public static void serializar() {
			
			FileOutputStream fos;
			
			ObjectOutputStream oos;
			
			File[] docs = ruta.listFiles();
			
			PrintWriter pw;
			
			for (File file: docs) //Iteramos en los archivos que hallan en la ruta para vaciarlos creando un printwiter
			{
				try
				{
					pw = new PrintWriter(file);
				}
				catch (FileNotFoundException e)
				{
					e.printStackTrace();
				}
			}
			
			for(File file: docs) {
				if (file.getAbsolutePath().contains("Usuario")) {
					try {
						fos = new FileOutputStream(file);
						oos = new ObjectOutputStream(fos);
						oos.writeObject(null);
						}catch (FileNotFoundException e) {
							e.printStackTrace();
						}catch (IOException e) {
							e.printStackTrace();
						}
				}
			}
		}
}			