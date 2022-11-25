from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox, ttk 


class VentanaSecundaria(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Cine UNAL')
        self.option_add("*tearOff",  False)
        self.geometry("875x565")
        self.resizable(False,False)
        # self.iconbitmap('./imagenes/icono.ico')
        
        #Barras de menus 
        self.menubar = Menu(self)

        self.menuArchivo = Menu(self.menubar)
        self.menuArchivo.add_command(label = "Aplicación", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)

        #Ponemos nuestras funcionalidades en el menu de procesos
        self.menuProceso = Menu(self.menubar)
        self.menuProceso.add_command(label = "Comprar boletería")        
        self.menuProceso.add_command(label = "Buscar una reserva")        
        self.menuProceso.add_command(label = "Hacer devolución")
        self.menuProceso.add_command(label= "Ver cartelera")
        self.menuProceso.add_command(label= "Comprar producto")
        
        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Contactos", command = self.ayuda)
       
        #Para varias pestañas 
        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProceso)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar

        #Se organizan los frames
        self.frame1 = tk.Frame(self, width=430, height= 250,borderwidth=15, bg="purple")
        self.frame1.pack(side="top", expand=True, fill= BOTH)
        self.frame1.config(relief="sunken")

        self.frame2 = tk.Frame(self, width=430, height=250,borderwidth=15, bg="yellow")
        self.frame2.pack(side="left", anchor="sw", expand=True, fill=BOTH)
        self.frame2.config(relief="sunken")

        self.frame3 = tk.Frame(self, width=430, height=250,borderwidth=15, bg="red")
        self.frame3.pack(side="right", anchor="se", expand=True, fill=BOTH)
        self.frame3.config(relief="sunken")

        #Letrero asignatura
        self.asignatura= Label(self.frame2, text="Programación Orientada\n a Objetos", font=("Segoe UI", 17))
        self.asignatura.place(x=200, y=75, anchor="center")
        
        self.asignatura= Label(self.frame3, text="El mejor cine\n del MUNDO", font=("Segoe UI", 17))
        self.asignatura.place(x=200, y=75, anchor="center")

        self.fotosfun = ['./imagenes/cartel.png']
        
        self.listaFotos = []
        for i in self.fotosfun:
            imagen = PhotoImage(file=i)
            self.listaFotos.append(imagen)

        #frame cartel
        self.frameFoto1 = tk.Frame(self.frame1, width=400, height=200,bg="black")
        self.frameFoto1.place(x=225, y=30)

        #Cartel
        self.p1 = Label(self.frameFoto1, image=self.listaFotos[0])
        self.p1.pack()


#--------------------------------------------------------------------------------------------------------------
    def comprarBoleta(self):
        pass
#--------------------------------------------------------------------------------------------------------------
     # Este metodo muestra una breve descripcion de la app
    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Mensaje", message = "Administrador de Cine",
        detail = "El sistema permite brindar las funcionalidades que mas se desarían en un portal virtual de cine.")

#--------------------------------------------------------------------------------------------------------------
    # Retorna a la Ventana de Inicio del programa.
    def salirVentana(self):
        return super().destroy()

#-------------------------------------------------------------------------------------------------------------------------------------
    # Muestra un Message Box con los nombres de los autores de la aplicación.
    def ayuda(self):
        mensaje = messagebox.showinfo(title = "Mensaje", message = "Autores: \n\n\n Sebastián Olaya Pérez: \n solayap@unal.edu.co\n\n Camilo Echeverrí Castrillón\n cecheverric@unal.edu.co\n\n Tomás Gutierrez Orrego\n tguttierrez@unal.edu.co\n\n Juan Jose Marín\n jumarina@unal.edu.co\n\n Julian Orrego Martinez\n jorrego@unal.edu.co")
