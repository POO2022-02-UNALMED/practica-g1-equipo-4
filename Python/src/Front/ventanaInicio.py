from VentanaPrincipal import VentanaSecundaria
from tkinter import messagebox as MessageBox, ttk 
from tkinter import *
import tkinter as tk
class ventanaInicio(tk.Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # Editamos nuestra ventana
        self.geometry("875x565")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.resizable(False,False)
        self.iconbitmap('./Python/src/Front/imagenes/icono.ico')
        
        #Variables donde va la descripción desarolladores
        self.var1 = tk.StringVar()
        self.var1.set("Los Integrantes del grupo 4")
        self.var2 =tk.StringVar()
        
        #crearemos nuestros frames.
        #frame del texto de bievenidatextoHDV
        self.frame1 = tk.Frame(self, width=400, height=500,borderwidth=15, bg="Black")
        self.frame1.pack(side="left", expand=True)
        self.frame1.config(relief="sunken")
        self.frame2 = tk.Frame(self.frame1, width=400, borderwidth=5,height=150, bg="steel blue")
        self.frame2.grid(row=0, column=0) 
        self.frame2.config(relief="ridge")       
        self.etiquetaBienvenida = Label(self.frame2, text="¡¡HOLA!!\n Bienvenido al cine \n UNAL", font=("", 20))
        self.etiquetaBienvenida.place(x=200, y=75, anchor="center")
        self.etiquetaBienvenida.config(fg="black", bg="light goldenrod")


        self.frame3 = tk.Frame(self.frame1, width=400, height=380, bg="light goldenrod")
        self.frame3.grid(row=1, column=0)
        
        self.frame4 = tk.Frame(self, width=400, height=500,borderwidth=15, bg="black")
        self.frame4.pack(side="right")
        self.frame4.config(relief="sunken")
        
        
        self.frame5 = tk.Frame(self.frame4, width=400, height=160,borderwidth=5, bg="steel blue")
        self.frame5.grid(row=0, column=0)
        self.frame5.config(relief="ridge")
        self.textoDescripcion = Label(self.frame5, textvariable=self.var1, font = ("Segoe UI", 10))
        self.textoDescripcion.bind('<ButtonPress-1>', self.cambioDescripcion)
        self.textoDescripcion.place(x=200, y=75, anchor="center")
        
        self.frame6 = tk.Frame(self.frame4, width=400,borderwidth=5, height=350, bg="black")
        self.frame6.grid(row = 1, column = 0)
        self.frame6.config(relief="ridge")           
        

        #El menu superior
        self.menubar = tk.Menu(self)
        self.menuInicio = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Inicio", menu=self.menuInicio)
        self.menuInicio.add_command(label="Salir",command=self.salir)
        self.menuInicio.add_command(label="Descripción",command=self.desno)
        self["menu"] = self.menubar
        


        #Frames con las fotos de los desarrolladores
        self.frameFoto1 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto1.place(x=0, y=0)
        self.frameFoto2 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto2.place(x=208, y=0)
        self.frameFoto3 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto3.place(x=0, y=168)
        self.frameFoto4 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto4.place(x=208, y=168)
        
        
        #Lista para cargar las fotos
        self.fotosDesarolla = ['./Python/src/Front/imagenes/S.png', './Python/src/Front/imagenes/S1.png', './Python/src/Front/imagenes/S2.png', './Python/src/Front/imagenes/S3.png','./Python/src/Front/imagenes/TOMAS.png', './Python/src/Front/imagenes/TOMAS1.png', './Python/src/Front/imagenes/TOMAS2.png', './Python/src/Front/imagenes/TOMAS3.png',
         './Python/src/Front/imagenes/CAMILO.png', './Python/src/Front/imagenes/CAMILO1.png', './Python/src/Front/imagenes/CAMILO2.png', './Python/src/Front/imagenes/CAMILO3.png','./Python/src/Front/imagenes/JUANJO1.png', './Python/src/Front/imagenes/JUANJO.png', './Python/src/Front/imagenes/JUANJO2.png', './Python/src/Front/imagenes/JUANJO3.png',
         './Python/src/Front/imagenes/JULIAN.png', './Python/src/Front/imagenes/JULIAN1.png', './Python/src/Front/imagenes/JULIAN2.png', './Python/src/Front/imagenes/JULIAN3.png','./Python/src/Front/imagenes/U1.png', './Python/src/Front/imagenes/U2.png', './Python/src/Front/imagenes/U3.png', './Python/src/Front/imagenes/U4.png']
        self.listaFotos = []
        

        for i in self.fotosDesarolla:
            imagen = PhotoImage(file=i)
            self.listaFotos.append(imagen)

        self.p1 = Label(self.frameFoto1)
        self.p2 = Label(self.frameFoto2)
        self.p3 = Label(self.frameFoto3)
        self.p4 = Label(self.frameFoto4)


        self.p1["image"] = self.listaFotos[20]
        
        self.p1.pack()
        self.p2["image"] = self.listaFotos[21]
        self.p2.pack()
        
        self.p3["image"] = self.listaFotos[22]
        self.p3.pack()
        
        self.p4["image"] = self.listaFotos[23]
        self.p4.pack()
        self.contador = 0

        #Imagenes del cine para ir cambiando
        self.fotosApp = ['./Python/src/Front/imagenes/p1.png', './Python/src/Front/imagenes/p2.png', './Python/src/Front/imagenes/p3.png','./Python/src/Front/imagenes/p4.png']
        self.listaFotosApp = []
        for i in self.fotosApp:
            imagen = PhotoImage(file=i)
            self.listaFotosApp.append(imagen)

        #Boton para dirgirse a la ventana de usuario
        self.botonCambioa = Button(self.frame3, image=self.listaFotosApp[0],command=self.abrirVentanaSecundaria)
        self.botonCambioa.pack()
        self.botonCambioa.bind('<Enter>', self.cambio)
        
        self.acumulador = 0
        self.numClicks = 0
        
    #Descripción
    def desno(self):
        descripcion = MessageBox.showinfo(title = "Mensaje", message = "Información de la App",
        detail = "Con esta app podrás hacer todo lo que se puede realizar en un portal de cine virtual, con todas la funcionalidades principales que podrías desear" )
        
    
    def cambioDescripcion(self,cont):
        self.numClicks += 1
        if (self.numClicks == 1):
            self.var1.set("Nombre: Sebastián Olaya Pérez \n"" Me gusta el fútbol \n""Estudiante de Ingeniería de Sistemas e Informática\n""Vive en Medellín")
            self.evento(1)
        elif (self.numClicks == 2):
            self.var1.set("Nombre: Tomás Gutiérrez Orrego \n"" Me gustan los caballos \n""Estudiante de Ingeniería de Sistemas e Informática\n""Vive en Medellín")
            self.evento(2)
        elif (self.numClicks == 3):
            self.var1.set("Nombre: Camilo Echeverri Castrillón \n"" Me gusta el Valorant \n""Estudiante de Ingeniería de Sistemas e Informática\n""Vive en Medellín")
            self.evento(3)
        elif (self.numClicks == 4):
            self.var1.set("Nombre: Juan Jose Marín Álvarez \n"" Me gusta jugar Lol \n""Estudiante de Ingeniería de Sistemas e Informática\n""Vive en Medellín")
            self.evento(4)
        elif (self.numClicks == 5):
            self.var1.set("Nombre: Julián Orrego Martínez \n"" Me gusta ser rubio y los gatos \n""Estudiante de Ingeniería de Sistemas e Informática\n""Vive en Medellín")
            self.evento(5)
            self.numClicks = 0

    #Selecciona la imagen a pryectar dependiendo del contador que entra al evento
    def evento(self, cont):
        foto1 = 0
        foto2 = 0
        foto3 = 0
        foto4 = 0
        self.contador += 1
        if self.contador == 1:
            foto1 = self.contador - 1
            foto2 = self.contador
            foto3 = self.contador + 1
            foto4 = self.contador + 2
        elif self.contador == 2:
            foto1 = self.contador + 2
            foto2 = self.contador + 3
            foto3 = self.contador + 4
            foto4 = self.contador + 5
        elif self.contador == 3:
            foto1 = self.contador + 5
            foto2 = self.contador + 6
            foto3 = self.contador + 7
            foto4 = self.contador + 8
        elif self.contador == 4:
            foto1 = self.contador + 8
            foto2 = self.contador + 9
            foto3 = self.contador + 10
            foto4 = self.contador + 11
        elif self.contador == 5:
            foto1 = self.contador + 11
            foto2 = self.contador + 12
            foto3 = self.contador + 13
            foto4 = self.contador + 14
        self.p1.config(image=self.listaFotos[foto1])
        self.p2.config(image=self.listaFotos[foto2])
        self.p3.config(image=self.listaFotos[foto3])
        self.p4.config(image=self.listaFotos[foto4])
        if self.contador == 5:
            self.contador = 0

    #con esta funcion cambiamos las imagenes
    def cambio(self,conts):
        self.acumulador += 1
        if self.acumulador == 4:
            self.acumulador = 0
        self.botonCambioa.config(image=self.listaFotosApp[self.acumulador])
    
    #con este metodo abrimos la ventana de usario, la cual se abre por medio de un evento
    def abrirVentanaSecundaria(self):
         #if not VentanaSecundaria.en_uso:
            self.ventanaUsuario = VentanaSecundaria()
            self.ventanaUsuario.ventanaInicio = self
            self.iconify()
    
    #con esto nos salimos 
    def salir(self):
        return super().destroy()