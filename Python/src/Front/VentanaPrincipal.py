from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox, ttk 
from fieldframe import FieldFrame

class VentanaSecundaria(tk.Tk):
    framesEnPantalla = []
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Cine UNAL')
        self.option_add("*tearOff",  False)
        self.geometry("875x565")
        self.iconbitmap('./Python/src/Front/imagenes/icono.ico')
        
        #Barras de menus 
        self.menubar = Menu(self)

        self.menuArchivo = Menu(self.menubar)
        self.menuArchivo.add_command(label = "Aplicación", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)

        #Ponemos nuestras funcionalidades en el menu de procesos
        self.menuProceso = Menu(self.menubar)
        self.menuProceso.add_command(label = "Comprar boletería", command = lambda: cambiarVista(frameCompra))        
        self.menuProceso.add_command(label = "Buscar una reserva", command = lambda: cambiarVista(frameReserva))        
        self.menuProceso.add_command(label = "Hacer devolución",command=lambda: cambiarVista(frameDevolucion))
        self.menuProceso.add_command(label= "Hacerse VIP",command=lambda: cambiarVista(frameVIP))
        self.menuProceso.add_command(label= "Ver cartelera",command=lambda: cambiarVista(frameCartelera))
        self.menuProceso.add_command(label= "Comprar producto", command = lambda: cambiarVista(frameTienda))
        
        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Contactos", command = self.ayuda)
       
        #Para varias pestañas 
        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProceso)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar

        def cambiarVista(frameUtilizado):
            for frame in self.framesEnPantalla:
                frame.pack_forget()
            frameUtilizado.pack(fill=BOTH,expand=True, pady = 10)
        
       
    #------------------------------------------------------------------------------------------------------------------------
        self.fotosfun = ['./Python/src/Front/imagenes/cartelera.png']
        self.listaFotos = []
        

        for i in self.fotosfun:
            imagen = PhotoImage(file=i)
            self.listaFotos.append(imagen)

        
    #---------------------------------------------------------------------------------------------------------------------- 
    #Se organizan los frames
        
        #Frame Inicio
        
        framePantallaInicio = Frame(self, bg='purple')
        nombrePantallaInicio = Label(framePantallaInicio, text="Cine UNAL", font=("Segoe UI", 16), bg='yellow')
        insPantallaInicio = Label(framePantallaInicio, text="La aplicación funciona así:", font=("Segoe UI", 10), bg='green')
        nombrePantallaInicio.pack()
        insPantallaInicio.pack(fill=X, expand=True, padx=10)
        self.framesEnPantalla.append(framePantallaInicio)
        cambiarVista(framePantallaInicio)
        
        
        #Frame Comprar boletas
        
        frameCompra = Frame(self,bg='purple')
        nombreCompra = Label(frameCompra, text="Compra tus boletas", font=("Segoe UI", 16), bg= 'yellow')
        descCompra = Label(frameCompra, text="Digite los campos para comprar las boletas", font=("Segoe UI", 12), background= 'White')
        
        frameformulario = Frame(frameCompra, height=200,bg='BLACK')

        FFCompra = FieldFrame(frameformulario, "", ["Nombre", "Cédula", "Cantidad de boletas","Dia"], "Información Personal", None, [True, True, True,True])

        framebotones = Frame(frameCompra, bg='purple')
        
        BotonComprar = Button(framebotones, text="Comprar")
        Botonlimpiar = Button(framebotones, text="Limpiar")
        Botonsalir = Button(framebotones, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreCompra.pack(pady=15) 
        descCompra.pack(pady=15)
        frameformulario.pack(anchor='center',pady=10)
        framebotones.pack(anchor='s',pady=15)
        BotonComprar.grid(column=0, row=0, padx = 10,pady=15)
        Botonlimpiar.grid(column=1, row=0, padx = 15,pady=15)
        Botonsalir.grid(column=3, row=0, padx = 15,pady=15)
        FFCompra.pack(pady=15)
        self.framesEnPantalla.append(frameCompra)


        #frame reserva
        frameReserva = Frame(self,bg='purple')
        nombreReserva = Label(frameReserva, text="Consulta si tiene reserva", font=("Segoe UI", 16), bg= 'yellow')
        descReserva = Label(frameReserva, text="Ingrese su documento para saber su asiento", font=("Segoe UI", 12), background= 'purple')
        frameformulario2 = Frame(frameReserva,height=200,bg='green')
        FFReserva= FieldFrame(frameformulario2, None, ["Cédula"],"Información", None, [True])
        framebotones2 = Frame(frameReserva, bg='purple')
        
        BotonComprar2 = Button(framebotones2, text="Devolución")
        Botonlimpiar2 = Button(framebotones2, text="Limpiar")
        Botonsalir2 = Button(framebotones2, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreReserva.pack(pady=(10,80))
        descReserva.pack(pady=10)
        frameformulario2.pack(anchor='center')
        
        framebotones2.pack(anchor='s')
        BotonComprar2.grid(column=0, row=0, padx = 10,pady=15)
        Botonlimpiar2.grid(column=1, row=0, padx = 10,pady=15)
        Botonsalir2.grid(column=3, row=0, padx = 10,pady=15)
        FFReserva.pack(pady=10)
        self.framesEnPantalla.append(frameReserva)

        
        #frame devolución
        frameDevolucion= Frame(self,bg='purple')
        nombreDevolucion = Label(frameDevolucion, text="Solicita la devolución", font=("Segoe UI", 16), bg= 'yellow')
        descDevolucion = Label(frameDevolucion, text="Ingrese su documento para saber si se puede realizar la devolución de su dinero", font=("Segoe UI", 12), background= 'purple')
        frameformulario3 = Frame(frameDevolucion,height=200,bg='green')
        FFDevolucion= FieldFrame(frameformulario3, None, ["Cédula"], None, None, [True])
        framebotones3 = Frame(frameDevolucion, bg='purple')
        
        BotonComprar3 = Button(framebotones3, text="Devolución")
        Botonlimpiar3 = Button(framebotones3, text="Limpiar")
        Botonsalir3 = Button(framebotones3, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreDevolucion.pack(pady=(10,80))
        descDevolucion.pack(pady=15)
        frameformulario3.pack(anchor='center')
       
        framebotones3.pack(anchor='s')
        BotonComprar3.grid(column=0, row=0, padx = 10,pady=10)
        Botonlimpiar3.grid(column=1, row=0, padx = 10,pady=10)
        Botonsalir3.grid(column=3, row=0, padx = 10,pady=10)
        FFDevolucion.pack(pady=10)
        self.framesEnPantalla.append(frameDevolucion)

        #frame VIP
        frameVIP= Frame(self,bg='purple')
        nombreVIP= Label(frameVIP, text="Hazte miembor VIP", font=("Segoe UI", 16), bg= 'yellow')
        descVIP = Label(frameVIP, text="Ingrese su documento para volverse VIP", font=("Segoe UI", 12), background= 'purple')
        frameformulario5 = Frame(frameVIP,height=200,bg='green')
        FFVIP= FieldFrame(frameformulario5, None, ["Cédula"], None, None, [True])
        framebotones5 = Frame(frameVIP, bg='purple')
        
        BotonComprar5 = Button(framebotones5, text="Devolución")
        Botonlimpiar5 = Button(framebotones5, text="Limpiar")
        Botonsalir5 = Button(framebotones5, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreVIP.pack(pady=(10,80))
        descVIP.pack(pady=15)
        frameformulario5.pack(anchor='center')
        
        framebotones5.pack(anchor='s')
        BotonComprar5.grid(column=0, row=0, padx = 10, pady=15)
        Botonlimpiar5.grid(column=1, row=0, padx = 10, pady=15)
        Botonsalir5.grid(column=3, row=0, padx = 10, pady=15)
        FFVIP.pack()
        self.framesEnPantalla.append(frameVIP)
         
        
        #frame cartelera
        frameCartelera = Frame(self,bg='purple')
        nombreCartelera = Label(frameCartelera, text="Cartelera", font=("Segoe UI", 16), bg= 'yellow')
        descCartelera = Label(frameCartelera, text="La Cartelera el día de hoy", font=("Segoe UI", 12), background= 'purple')
        frameimagen = Frame(frameCartelera,width=150, height=300,bg="black")
        framebotones6 = Frame(frameCartelera, bg='purple')
        Botonsalir6 = Button(framebotones6, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreCartelera.pack()
        descCartelera.pack()
        frameimagen.pack()
        Botonsalir6.pack()
        framebotones6.pack(anchor='s')
        self.framesEnPantalla.append(frameCartelera)

        #frame tienda
        frameTienda =  Frame(self,bg='purple')
        nombreTienda = Label(frameTienda, text="Tienda", font=("Segoe UI", 16), bg= 'yellow')
        descTienda = Label(frameTienda, text="Para comprar tus productos favoritos", font=("Segoe UI", 12), background= 'purple')
        frameformulario4 = Frame(frameTienda,height=200,bg='green')
        FFTienda= FieldFrame(frameformulario4, None, ["Saldo"], None, None, [True])
        framebotones4 = Frame(frameTienda, bg='purple')
      
        BotonComprar4 = Button(framebotones4, text="Comprar")
        Botonlimpiar4 = Button(framebotones4, text="Limpiar")
        Botonsalir4 = Button(framebotones4, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreTienda.pack(pady=(10,80))
        descTienda.pack(pady=15)
        frameformulario4.pack(anchor='center')

        framebotones4.pack(anchor='s')
        BotonComprar4.grid(column=0, row=0, padx = 10,pady=10)
        Botonlimpiar4.grid(column=1, row=0, padx = 10,pady=10)
        Botonsalir4.grid(column=3, row=0, padx = 10,pady=10)
        FFTienda.pack()
        self.framesEnPantalla.append(frameTienda)




#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para la compra de la boleta
    def mostraroutput(self,lugar,texto):
        output = Label(lugar,text=texto,font=("Segoe UI", 12), bg= 'green')
        output.pack(anchor="center")
#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para la compra de la boleta
    def comprarBoleta(self):
        pass

#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para buscar reserva
    def buscarReserva(self):
        pass
#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para hacer de la devolucion
    def hacerDevolucion(self):
        pass
#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para ver cartelera
    def verCartelera(self):
        pass

#--------------------------------------------------------------------------------------------------------------
    #Este metodo es para comprar producto
    def comprarProducto(self):
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

#-------------------------------------------------------------------------------------------------------------------------------------
    def eventofuncionalidad(self):
        pass