from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox, ttk 
from fieldframe import FieldFrame
import sys
from excepciones.excepcionesUsuario import excepcionesUsuario
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
        
        framePantallaInicio = Frame(self, bg='ghost white')
        nombrePantallaInicio = Label(framePantallaInicio, text="Cine UNAL", font=("Segoe UI", 16), bg='yellow')
        insPantallaInicio = Label(framePantallaInicio, text="La aplicación funciona así:", font=("Segoe UI", 10), bg='green')
        nombrePantallaInicio.pack()
        insPantallaInicio.pack(fill=X, expand=True, padx=10)
        self.framesEnPantalla.append(framePantallaInicio)
        cambiarVista(framePantallaInicio)
        
        
        #Frame Comprar boletas
    
        def comprobarBoleta():
            try:
                nombre = FFCompraBoleta.getValue("Nombre")
                cedula = FFCompraBoleta.getValue("Cedula")
                cantidadBoletas = FFCompraBoleta.getValue("Cantidad de boletas")
                diaFuncion = FFCompraBoleta.getValue("Dia de la funcion")
                nombrePelicula = FFCompraBoleta.getValue("Nombre de la pelicula")

                if nombre == "" or cedula == "" or cantidadBoletas == "" or diaFuncion == "" or nombrePelicula == "":
                    if esUnNumero(cedula) == False or esUnNumero(cantidadBoletas) == False or esString(nombre) == False or esString(nombrePelicula) == False:
                        MessageBox.showinfo("Error", "Por favor ingrese los datos en el fromato correcto")
                    MessageBox.showerror("Error", "Por favor llene todos los campos")
                    
                # ---- Aqui va la funcionalidad de comprar boleta ----

            except excepcionesUsuario as e:
                MessageBox.showerror("Error", e)
                
        frameCompra = Frame(self,bg='ghost white')
        nombreCompra = Label(frameCompra, text="Compra tus boletas", font=("Segoe UI", 16), bg= 'yellow')
        descCompra = Label(frameCompra, text="Digite los campos para comprar las boletas", font=("Segoe UI", 12), background= 'White')
        
        frameformulario = Frame(frameCompra, height=200,bg='BLACK')

        FFCompraBoleta = FieldFrame(frameformulario, "", ["Nombre", "Cedula", "Cantidad de boletas","Dia de la funcion", "Nombre de la pelicula"], "Informacion Personal", None, [True, True, True,True, True])

        framebotones = Frame(frameCompra, bg='ghost white')
        
        BotonComprar = Button(framebotones, text="Comprar", command=comprobarBoleta)
        Botonlimpiar = Button(framebotones, text="Limpiar")
        Botonsalir = Button(framebotones, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreCompra.pack(pady=15) 
        descCompra.pack(pady=15)
        frameformulario.pack(anchor='center',pady=10)
        framebotones.pack(anchor='s',pady=15)
        BotonComprar.grid(column=0, row=0, padx = 10,pady=15)
        Botonlimpiar.grid(column=1, row=0, padx = 15,pady=15)
        Botonsalir.grid(column=3, row=0, padx = 15,pady=15)
        FFCompraBoleta.pack(pady=15)

        self.framesEnPantalla.append(frameCompra)

        #frame consulta reserva
        def comprobarReserva():
            try:
                nombre = FFReserva.getValue("Nombre")
                cedula = FFReserva.getValue("Cedula")
                diaFuncion = FFReserva.getValue("Dia de la funcion")
                
                if nombre == "" or cedula == "" or diaFuncion == "" :
                    MessageBox.showerror("Error", "Por favor llene todos los campos")
                if esUnNumero(cedula) == False or esString(nombre) == False :
                    MessageBox.showinfo("Error", "Por favor ingrese los datos en el fromato correcto")

                # ---- Aqui va la funcionalidad de consultar reserva ----
                         
            except excepcionesUsuario as e:
                MessageBox.showerror("Error", e)

        frameReserva = Frame(self,bg='ghost white')
        nombreReserva = Label(frameReserva, text="Consulta si tiene reserva", font=("Segoe UI", 16), bg= 'yellow')
        descReserva = Label(frameReserva, text="Ingrese la siguinete informacion para consultar su asiento", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario2 = Frame(frameReserva,height=200,bg='green')
        FFReserva= FieldFrame(frameformulario2, None, ["Nombre", "Cedula", "ID Boleta"],"Información", None, [True, True, True])
        framebotones2 = Frame(frameReserva, bg='ghost white')
        BotonComprar2 = Button(framebotones2, text="Consultar", command=comprobarReserva)
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
        def comprobarDevolucion():
            try:
                cedula = FFDevolucion.getValue("Cedula")
                IDBoleta = FFDevolucion.getValue("ID Boleta")
         
                if IDBoleta == "" or cedula == "" :
                    MessageBox.showerror("Error", "Por favor llene todos los campos")
                if esUnNumero(cedula) == False or esString(IDBoleta) == False:
                    MessageBox.showinfo("Error", "Por favor ingrese los datos en el fromato correcto")

                # ---- Aqui va la funcionalidad de devolución ----
            except excepcionesUsuario as e:
                MessageBox.showerror("Error", e)

        frameDevolucion= Frame(self,bg='ghost white')
        nombreDevolucion = Label(frameDevolucion, text="Solicita la devolución", font=("Segoe UI", 16), bg= 'yellow')
        descDevolucion = Label(frameDevolucion, text="Ingrese su documento para saber si se puede realizar la devolución de su dinero", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario3 = Frame(frameDevolucion,height=200,bg='green')
        FFDevolucion= FieldFrame(frameformulario3, None, ["Cédula", "ID Boleta"], None, None, [True, True])
        framebotones3 = Frame(frameDevolucion, bg='ghost white')
        BotonComprar3 = Button(framebotones3, text="Devolución", command=comprobarDevolucion)
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
        def comprobarVIP():
            try:
                nombre = FFVIP.getValue("Nombre")
                cedula = FFVIP.getValue("Cedula")
                diaFuncion = FFVIP.getValue("Dia de la funcion")
                if nombre == "" or cedula == "" or diaFuncion == "" :
                    MessageBox.showerror("Error", "Por favor llene todos los campos")
                if esUnNumero(cedula) == False or esString(nombre) == False :
                    MessageBox.showinfo("Error", "Por favor ingrese los datos en el fromato correcto")

                # ---- Aqui va la funcionalidad de VIP ----
            except excepcionesUsuario as e:
                MessageBox.showerror("Error", e)


        frameVIP= Frame(self,bg='ghost white')
        nombreVIP= Label(frameVIP, text="Hazte miembor VIP", font=("Segoe UI", 16), bg= 'yellow')
        descVIP = Label(frameVIP, text="Ingrese su documento para volverse VIP", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario5 = Frame(frameVIP,height=200,bg='green')
        FFVIP= FieldFrame(frameformulario5, None, ["Cédula", "ID Boleta"], None, None, [True, True])
        framebotones5 = Frame(frameVIP, bg='ghost white')
        
        BotonComprar5 = Button(framebotones5, text="VIP", command=comprobarVIP)
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
        #funcion que cambie el nombre cartelera por el dia seleccionado

        diasSemana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        frameCartelera = Frame(self,bg='ghost white')
        frameCartelera.columnconfigure(0, weight=1)
        frameCartelera.columnconfigure(1, weight=1)
        frameCartelera.columnconfigure(2, weight=1)
        frameCartelera.rowconfigure(0, weight=1)
        frameCartelera.rowconfigure(1, weight=1)
        frameCartelera.rowconfigure(2, weight=1)
        frameCartelera.rowconfigure(3, weight=1)
        frameCartelera.rowconfigure(4, weight=1)
        nombreCartelera = Label(frameCartelera, text="Dia de cartelera", font=("Segoe UI", 16), bg= 'yellow')
        seleccion= Label(frameCartelera, text="Por favor selesccione el dia", font=("Segoe UI", 16), bg= "RED")
        descCartelera = Label(frameCartelera, text="La Cartelera el día de hoy", font=("Segoe UI", 12), background= 'ghost white')
        framePeliculas = Label(frameCartelera,text="Aqui aparceran la cartelera del dia seleccionado",bg="blue")
        framebotones6 = Frame(frameCartelera, bg='ghost white')
        Botonsalir6 = Button(framebotones6, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        diasbox=Combobox(frameCartelera,values=diasSemana,state="readonly",width=10,)
        nombreCartelera.grid(row=0, column=1,rowspan=2,columnspan=2,sticky="nsew")
        seleccion.grid(row=0, column=0,sticky="nsew")        
        diasbox.grid(row=1, column=0,sticky="nsew")
        descCartelera.grid(row=2, column=0,sticky="nsew")
        framePeliculas.grid(row=2, column=1,columnspan=2,rowspan=3,sticky="nsew")
        Botonsalir6.pack()
        framebotones6.grid(row=4, column=0,sticky="nsew")
        self.framesEnPantalla.append(frameCartelera)
        #hacer que el combobox cambie el nombre de cartelera por el dia seleccionado y que tenga la cartelera del dia seleccionado
        diasbox.bind("<<ComboboxSelected>>",lambda event: cambiarNombreCartelera(event,diasbox,nombreCartelera))
        
        def cambiarNombreCartelera(event,diasbox,nombreCartelera):
            nombreCartelera.config(text=diasbox.get())
            if   diasbox.get()=="Lunes           ":
                framePeliculas.config(text="Pelicula 1")
            elif diasbox.get()=="Martes          ":
                #nombre de las pelicula y ubicarlo arriba a la izquierda letra arial tamaño 12
                framePeliculas.config(text="Pelicula 2:14:00-16:00\n Pelicula 3: 20:00-22:00\n Pelicula 4: 00:00-00:00\n Pelicula 5: 02:00-00:00",anchor="nw",  font=("Arial", 20))      
            elif diasbox.get()=="Miercoles       ":
                framePeliculas.config(text="Pelicula 3")
            elif diasbox.get()=="Jueves          ":
                framePeliculas.config(text="Pelicula 4")
            elif diasbox.get()=="Viernes         ":
                framePeliculas.config(text="Pelicula 5")   
            elif diasbox.get()=="Sabado          ":
                framePeliculas.config(text="Pelicula 6")
            elif diasbox.get()=="Domingo         ":
                framePeliculas.config(text="Pelicula 7")




        #frame tienda
        def comboboSeleccion(event):
            comboboxProducto.set("")
            comboboxProducto.config(values=opciones[comboboxTienda.get()])        
        opciones = {
            "Comida": ("Papas", "hambuerguesa", "Palomitas"), 
            "Unal": ("Buso", "Gorra", "termo")
        }   
        frameTienda =  Frame(self,bg='ghost white')
        nombreTienda = Label(frameTienda, text="Tienda", font=("Segoe UI", 16), bg= 'yellow')
        descTienda = Label(frameTienda, text="Para comprar tus productos favoritos", font=("Segoe UI", 12), background= 'ghost white')
        comboboxTienda= Combobox(frameTienda,values=tuple(opciones.keys()),state="readonly")
        comboboxProducto= Combobox(frameTienda,state="readonly")
        framebotones4 = Frame(frameTienda, bg='ghost white')
        BotonComprar4 = Button(framebotones4, text="Comprar")
        Botonsalir4 = Button(framebotones4, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreTienda.grid(row=0, column=0,sticky="nsew")
        descTienda.grid(row=1, column=0,sticky="nsew")
        comboboxTienda.grid(row=2, column=0,sticky="nsew")
        comboboxTienda.bind("<<ComboboxSelected>>",comboboSeleccion)
        comboboxProducto.grid(row=3, column=0,sticky="nsew")
        framebotones4.grid(row=4, column=0,sticky="nsew")
        BotonComprar4.grid(column=0, row=0, padx = 10,pady=10)
        Botonsalir4.grid(column=1, row=0, padx = 10,pady=10)
        self.framesEnPantalla.append(frameTienda)

    

        def esUnNumero(numero):
            try:
                int(numero)
                return True
            except:
                return False
        
        def esString(string):
            try:
                str(string)
                return True
            except:
                return False


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
        mensaje = messagebox.showinfo(title = "Mensaje", message = "Autores: \n\n\n Sebastián Olaya Pérez: \n solayap@unal.edu.co\n\n Camilo Echeverrí Castrillón\n cecheverric@unal.edu.co\n\n Tomás Gutierrez Orrego\n tgutierrez@unal.edu.co\n\n Juan Jose Marín\n jumarina@unal.edu.co\n\n Julian Orrego Martinez\n jorrego@unal.edu.co")

#-------------------------------------------------------------------------------------------------------------------------------------
    def eventofuncionalidad(self):
        pass