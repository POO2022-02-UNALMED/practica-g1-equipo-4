package baseDatos;

import java.io.*;

import gestorAplicación.cine.*;

import IU.*;

public class Serializador {
		
	public static void serializar() {
		
		try {
            FileOutputStream f = new FileOutputStream(new File(System.getProperty("user.dir")+"\\Cine\\baseDatos\\temp\\Usuario.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);
            o.writeObject(null);
            o.close();
            f.close();
        				
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}