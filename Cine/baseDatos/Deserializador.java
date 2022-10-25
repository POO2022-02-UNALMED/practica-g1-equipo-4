package baseDatos;

import gestorAplicación.cine.*;
import gestorAplicación.tiendaAbst.*;

import java.io.*;
import java.util.ArrayList;

public class Deserializador {
    private static File rutaTemp = new File("Cine\\baseDatos\\temp");

    /**
     * Carga las listas de objetos que hay almacenados
     */
    public static void deserializar(Usuario usuario){
        File[] docs = rutaTemp.listFiles();
        FileInputStream fis;
        ObjectInputStream ois;

        for (File file : docs) {
            if (file.getAbsolutePath().contains("Boletas")){
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    usuario.setBoletas((ArrayList<Boleta>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            }
        }
    }
}