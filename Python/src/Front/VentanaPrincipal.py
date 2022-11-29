from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox, ttk 
from fieldframe import FieldFrame
import sys

from excepcionesPy.errorAplicacion import errorAplicacion
from excepcionesPy.errorEntero import errorEntero
from excepcionesPy.errorString import errorString
from excepcionesPy.errorUnexpected import errorUnexpected
from excepcionesPy.excepcionesFuncionalidad import excepcionesFuncionalidad
from excepcionesPy.excepcionesFormato import excepcionesFormato
from excepcionesPy.errorDevolucion import errorDevolucion

import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())


class VentanaSecundaria(tk.Tk):

    framesEnPantalla = []
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Cine UNAL')
        self.option_add("*tearOff",  False)
        self.geometry("875x565")
        self.iconbitmap(path+'\imagenes\icono.ico')
        
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
        

        
    #---------------------------------------------------------------------------------------------------------------------- 
    #Se organizan los frames
        
        #Frame Inicio
        
        framePantallaInicio = Frame(self, bg='brown')
        nombrePantallaInicio = Label(framePantallaInicio, text="CINE UNAL", font=("Segoe UI", 50), bg='seashell2')
        insPantallaInicio = Label(framePantallaInicio, text="Presiona el menú Procesos y Consultas", font=("Segoe UI", 30), bg='bisque')
        nombrePantallaInicio.pack()
        insPantallaInicio.pack(fill=X, expand=True, padx=10)
        self.framesEnPantalla.append(framePantallaInicio)
        cambiarVista(framePantallaInicio)
        
        
        #Frame Comprar boletas
        def esUnNumero(numero):
            if numero.isnumeric():
               return True 
                
        def esString(string):
            if string.isalpha():
                return True
            
        def comprobarBoleta():
            try:
                nombre = FFCompraBoleta.getValue("Nombre")
                cedula = FFCompraBoleta.getValue("Cedula")
                cantidadBoletas = FFCompraBoleta.getValue("Cantidad de boletas")
                diaFuncion = FFCompraBoleta.getValue("Dia de la funcion")
                nombrePelicula = FFCompraBoleta.getValue("Nombre de la pelicula")

                if not esString(nombre):
                    raise errorString(nombre)
                
                if not esUnNumero(cedula):
                    raise errorEntero(cedula)
                
                if not esUnNumero(cantidadBoletas):
                    raise errorEntero(cantidadBoletas)
                
                if not esString(nombrePelicula):
                    raise errorString(nombrePelicula)
                
                if not esString(diaFuncion):
                    raise errorString(diaFuncion)
            

                # ---- Aqui va la funcionalidad de comprar boleta ---- 
                MessageBox.showinfo("Compra de boletas", "Compra exitosa")
                

            except errorAplicacion as e:
                MessageBox.showerror("Error", e)
                
        frameCompra = Frame(self,bg='brown')
        nombreCompra = Label(frameCompra, text="Compra tus boletas", font=("Segoe UI", 16), bg= 'bisque')
        descCompra = Label(frameCompra, text="Digite los campos para comprar las boletas", font=("Segoe UI", 12), background= 'White')
        
        frameformulario = Frame(frameCompra, height=200,bg='BLACK')

        FFCompraBoleta = FieldFrame(frameformulario, "", ["Nombre", "Cedula", "Cantidad de boletas","Dia de la funcion", "Nombre de la pelicula"], "Información Personal", None, [True, True, True,True, True])

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
                IDBoleta = FFReserva.getValue("ID Boleta")
                
                if not esString(nombre):
                    raise errorString(nombre)
                
                if not esUnNumero(cedula):
                    raise errorEntero(cedula)
                
                if not esUnNumero(IDBoleta):
                    raise errorEntero(IDBoleta)
                
                # ---- Aqui va la funcionalidad de consultar reserva ----
                         
            except excepcionesFormato as e:
                MessageBox.showerror("Error", e)

        frameReserva = Frame(self,bg='brown')
        nombreReserva = Label(frameReserva, text="Consultar si tiene reserva", font=("Segoe UI", 16), bg= 'bisque')
        descReserva = Label(frameReserva, text="Ingrese la siguinete información para consultar su asiento", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario2 = Frame(frameReserva,height=200,bg='firebrick')
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
         
                if not esUnNumero(cedula):
                    raise errorEntero(cedula)
                
                if not esUnNumero(IDBoleta):
                    raise errorEntero(IDBoleta)
                
                # ---- Aqui va la funcionalidad de devolución ----
            except errorAplicacion as e:
                MessageBox.showerror("Error", e)

        frameDevolucion= Frame(self,bg='brown')
        nombreDevolucion = Label(frameDevolucion, text="Solicita la devolución", font=("Segoe UI", 16), bg= 'bisque')
        descDevolucion = Label(frameDevolucion, text="Ingrese su documento para saber si se puede realizar la devolución de su dinero", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario3 = Frame(frameDevolucion,height=200,bg='black')
        FFDevolucion= FieldFrame(frameformulario3, None, ["Cedula", "ID Boleta"], None, None, [True, True])
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
            cedula = FFVIP.getValue("Cedula")
            try:
                if not esUnNumero(cedula):
                    raise errorEntero(cedula)
                
                # ---- Aqui va la funcionalidad de VIP ----
            except errorAplicacion as e:
                MessageBox.showerror("Error", e)


        frameVIP= Frame(self,bg='brown')
        nombreVIP= Label(frameVIP, text="Hazte miembro VIP", font=("Segoe UI", 16), bg= 'bisque')
        descVIP = Label(frameVIP, text="Ingrese su documento para volverse VIP", font=("Segoe UI", 12), background= 'ghost white')
        frameformulario5 = Frame(frameVIP,height=200,bg='green')
        FFVIP= FieldFrame(frameformulario5, None, ["Cedula"], None, None, [True])
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
        nombreCartelera = Label(frameCartelera, text="Día",font=("Arabic Transparent", 30),anchor="sw", bg= 'brown')
        seleccion= Label(frameCartelera, text="Por favor seleccione el día", font=("Constantia", 25), bg= "bisque")
        descCartelera = Label(frameCartelera, text="La Cartelera el día de hoy", font=("Constantia", 18), background= 'salmon')
        framePeliculas = Label(frameCartelera,text="Aquí aparcerá la cartelera del día seleccionado",bg="indian red", font=("Comic Sans MS", 25))
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
            nombreCartelera.config(text=diasbox.get(),font=("Arabic Transparent", 30),anchor="sw")
            if   diasbox.get()=="Lunes":
                framePeliculas.config(text="THE BOYS:14:00-16:00\n\nONE PIECE:16:00-20:00\n\nBARBIE:20:00-22:00\n\nIT:22:00-24:00  ",  font=("Comic Sans MS", 25))
            elif diasbox.get()=="Martes":
                framePeliculas.config(text="AVENGERS:14:00-16:00\n\nROGUE:16:00-20:00\n\nRATATUILLE:20:00-22:00\n\nSHAFT:22:00-24:00  ",  font=("Comic Sans MS", 25))      
            elif diasbox.get()=="Miercoles":
                framePeliculas.config(text="IT 2:14:00-16:00\n\nUP:16:00-20:00\n\nRATATUILLE:20:00-22:00\n\nLA SIRENITA:22:00-24:00  ",  font=("Comic Sans MS", 25))
            elif diasbox.get()=="Jueves":
                framePeliculas.config(text="RANGO:14:00-16:00\n\nEL PASEO:16:00-20:00\n\nHALLOWEEN:20:00-22:00\n\nREVENANT:22:00-24:00  ",  font=("Comic Sans MS", 25))
            elif diasbox.get()=="Viernes":
                framePeliculas.config(text="SCREAM 5:14:00-16:00\n\nMAD MAX:16:00-20:00\n\nAPOLO 13:20:00-22:00\n\nMATRIX:22:00-24:00  ",  font=("Comic Sans MS", 25))   
            elif diasbox.get()=="Sabado":
                framePeliculas.config(text="STAR WARS:14:00-16:00\n\nEL EXORCISTA:16:00-20:00\n\nDUNA:20:00-22:00\n\n1917:22:00-24:00  ",  font=("Comic Sans MS", 25))
            elif diasbox.get()=="Domingo":
                framePeliculas.config(text="EL ORIGEN:14:00-16:00\n\nSILENCE:16:00-20:00\n\nSINIESTRO:20:00-22:00\n\nEL RITUAL:22:00-24:00  ",  font=("Comic Sans MS", 25))

        #frame tienda
        def comboboSeleccion(event):
            comboboxProducto.set("")
            comboboxProducto.config(values=opciones[comboboxTienda.get()])
        def comboboSeleccion2(event):
            global Comida
            global Unal
            Comida = [["Papas","2000"], ["hambuerguesa","23000"], ["Palomitas","15000"]]
            Unal = [["Buso","20000"], ["Gorra","24000"], ["termo","13000"]]
            if comboboxProducto.get()=="":
                precio.configure(text="Precio: ")
            else:
                if comboboxTienda.get()=="Comida":
                    for i in Comida:
                        if comboboxProducto.get()==i[0]:
                                precio.configure(text="Precio: "+i[1])
                elif comboboxTienda.get()=="Unal":
                    for i in Unal:
                        if comboboxProducto.get()==i[0]:
                            precio.configure(text="Precio: "+i[1])
        def comprar():
            if comboboxTienda.get()=="":
                messagebox.showerror("Error","Debe seleccionar una tienda")
            elif comboboxProducto.get()=="":
                messagebox.showerror("Error","Debe seleccionar un producto")
            else:
                if comboboxTienda.get()=="Comida":
                    for i in Comida:
                        if comboboxProducto.get()==i[0]:
                            messagebox.showinfo("Compra exitosa","Su compra de "+i[0]+" por "+i[1]+" ha sido exitosa")
                elif comboboxTienda.get()=="Unal":
                    for i in Unal:
                        if comboboxProducto.get()==i[0]:
                            messagebox.showinfo("Compra exitosa","Su compra de "+i[0]+" por "+i[1]+" ha sido exitosa")
        opciones = {
            "Comida": ("Papas", "hambuerguesa", "Palomitas"), 
            "Unal": ("Buso", "Gorra", "termo")
        }
        frameTienda =  Frame(self,bg='brown')
        frameTienda.rowconfigure(0, weight=1)
        frameTienda.rowconfigure(1, weight=1)
        frameTienda.rowconfigure(2, weight=1)
        frameTienda.rowconfigure(3, weight=1)
        frameTienda.rowconfigure(4, weight=1)
        frameTienda.rowconfigure(5, weight=1)
        frameTienda.columnconfigure(0, weight=1)
        nombreTienda = Label(frameTienda, text="Tienda", font=("Segoe UI", 16), bg= 'bisque')
        descTienda = Label(frameTienda, text="¡Aqui puedes comprar tus productos favoritos!", font=("Segoe UI", 12), background= 'brown')
        comboboxTienda= Combobox(frameTienda,values=tuple(opciones.keys()),state="readonly")
        comboboxProducto= Combobox(frameTienda,state="readonly")
        precio=Label(frameTienda,text="Aqui dira el precio del producto")
        framebotones4 = Frame(frameTienda, bg='brown')
        BotonComprar4 = Button(framebotones4, text="Comprar",command=comprar)
        Botonsalir4 = Button(framebotones4, text="Salir", command=lambda: cambiarVista(framePantallaInicio))
        nombreTienda.grid(row=0, column=0,sticky="nsew")
        descTienda.grid(row=1, column=0,sticky="nsew")
        comboboxTienda.grid(row=2, column=0,sticky="nsew")
        comboboxTienda.bind("<<ComboboxSelected>>",comboboSeleccion)
        comboboxProducto.grid(row=3, column=0,sticky="nsew")
        comboboxProducto.bind("<<ComboboxSelected>>",comboboSeleccion2)
        precio.grid(row=4, column=0,sticky="nsew")
        framebotones4.grid(row=5, column=0,sticky="nsew")
        BotonComprar4.pack(padx = 10,pady=10)
        Botonsalir4.pack(padx = 10,pady=10)
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
        detail = "El sistema permite brindar las funcionalidades que más se desarían en un portal virtual de cine.")

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