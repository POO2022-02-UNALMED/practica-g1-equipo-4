package baseDatos;

import java.io.*;

import IU.main;

public class Serializador {{
	
	try {
		
		ObjectOutputStream guardandoDatos = new ObjectOutputStream(new FileOutputStream("Cine/baseDatos/temp/usuario.txt"));
		
		guardandoDatos.writeObject(usuario);
		
		guardandoDatos.close();
		
	}catch(Exception e) {
		
	}
}
}