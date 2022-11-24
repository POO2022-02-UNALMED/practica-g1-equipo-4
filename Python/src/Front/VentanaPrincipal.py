from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox 



class VentanaSecundaria(Toplevel):








    
      
    def salirVentana(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

#-------------------------------------------------------------------------------------------------------------------------------------
    # Muestra un Message Box con los nombres de los autores de la aplicación.
    def ayuda(self):
        mensaje = messagebox.showinfo(title = "Mensaje", message = "Autores: \n\n Sebastián Olaya Pérez: \n solayap@unal.edu.co\n Camilo Echeverrí Castrillón\n cecheverric@unal.edu.co\n Tomás Gutierrez Orrego\n tguttierrez@unal.edu.co\n Juan Jose Marín\n jumarina@unal.edu.co\n Julian Orrego Martinez\n jorrego@unal.edu.co")



