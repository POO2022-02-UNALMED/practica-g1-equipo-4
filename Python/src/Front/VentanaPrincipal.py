from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox 



class VentanaSecundaria(Toplevel):








    
      
<<<<<<< HEAD
    


    #Esta funcione es para poder comprar boleteria 
    def prueba(self):

        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 
        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='##7FB3D5' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='##7FB3D5')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='##7FB3D5')
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)


        #Estas entradas es para pedir los datos al usuario
        self.nombre=StringVar()
              
        self.entryNombre = tk.Entry(self.frame2, textvariable=self.nombre)
        self.entryNombre.grid(column=4, row=2, sticky='ew', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame2, text="Nombre", font=("Arial",14))
        self.labelNombre.grid(column=3, columnspan=1,row=2, sticky='ew', padx=30, pady=10)
        self.labelinfo = tk.Label(self.frame2, text="Ingrese el nombre sin puntos y solo letras", font=("Arial",12),bg='#F98866')
        self.labelinfo.grid(column=6, columnspan=1,row=2, sticky='ew', padx=30, pady=10)
    
    
        self.cedula=StringVar()

        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=4, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=3, row=3, sticky='ew', padx=30, pady=10)
        self.labelinfo2 = tk.Label(self.frame2, text="Ingrese la cedula sin puntos y con enteros", font=("Arial",12),bg='#F98866')
        self.labelinfo2.grid(column=6, columnspan=1,row=3, sticky='ew', padx=30, pady=10)

        self.celular=StringVar()
        
        self.entryNombre = tk.Entry(self.frame2, textvariable=self.celular)
        self.entryNombre.grid(column=4, row=4, sticky='ew', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame2, text="Celular", font=("Arial",14))
        self.labelNombre.grid(column=3, columnspan=1,row=4, sticky='ew', padx=30, pady=10)
        self.labelinfo3 = tk.Label(self.frame2, text="Ingrese la celular sin puntos y con enteros", font=("Arial",12),bg='#F98866')
        self.labelinfo3.grid(column=6, columnspan=1,row=4, sticky='ew', padx=30, pady=10)
    

        
        self.combo = Combobox(self.frame2, state="readonly",values=["M", "F"])
        self.combo.place(x=142, y=159)
       
        self.labelSexo  = tk.Label(self.frame2, text="Sexo ", font=("Arial",14))
        self.labelSexo .grid(column=3,columnspan=1,  row=5, sticky='ew', padx=30, pady=10)
    
        self.edad=StringVar()
        
        self.entryEdad= tk.Entry(self.frame2, textvariable=self.edad)
        self.entryEdad.grid(column=4, row=6, sticky='w', padx=10, pady=10)
        self.labelEdad = tk.Label(self.frame2, text="Edad", font=("Arial",14))
        self.labelEdad.grid(column=3,columnspan=1,  row=6, sticky='w', padx=30, pady=10)
        self.labelinfo4 = tk.Label(self.frame2, text="Ingrese la edad sin puntos y con enteros", font=("Arial",12),bg='#F98866')
        self.labelinfo4.grid(column=6, columnspan=1,row=6, sticky='ew', padx=30, pady=10)

        self.saldo=StringVar()
        self.entrySaldo = tk.Entry(self.frame2, textvariable=self.saldo)
        self.entrySaldo.grid(column=4, row=7, sticky='w', padx=10, pady=10)
        self.labelSaldo = tk.Label(self.frame2, text="Saldo", font=("Arial",14))
        self.labelSaldo.grid(column=3, row=7, sticky='w', padx=30, pady=10)
        self.labelinfo5 = tk.Label(self.frame2, text="Ingrese el saldo sin puntos y con enteros", font=("Arial",12),bg='#F98866')
        self.labelinfo5.grid(column=6, columnspan=1,row=7, sticky='ew', padx=30, pady=10)



        #En esta parte vamos a pregunatrle a usuario si quiere ver una pelicula, y con base en eso se 
        # le saldra unas peliculas determinadas

        self.labelPelicula= Label(self.frame3, text="¿Quires ver peliculas 3D?", font=("Arial",14))
        self.labelPelicula.grid(column=1000, row=0, ipadx=0, ipady=0, padx=15, pady=0)



        self.combo = Combobox(self.frame3, state="readonly",values=["si", "no"])
        self.combo.place(x=60, y=49)




        self.labelVip= Label(self.frame4, text="¿Quires sillas Vip?", font=("Arial",14))
        self.labelVip.grid(column=0, columnspan=1,row=0,  padx=60, pady=40)



        self.combo2 = Combobox(self.frame4, state="readonly",values=["si", "no"])
        self.combo2.place(x=75, y=89)
        
        

        #Aqui guardamos al cliente en una lista temporal para ver luego registarlo en la lista serealizada
        #aqui hacemos el manejo de errores
        def siguiente():
            entero=self.nombre.get().isnumeric()
            entero2=self.cedula.get().isnumeric()  
            entero3=self.celular.get().isnumeric()  
            entero4=self.edad.get().isnumeric()  

         

            if entero==True:

                try:
                    raise ExcepcionEnteroString(entero)
                except ExcepcionEnteroString as e:
                    MessageBox.showerror(title="Error",message=e)
                    return
                
            if entero3==False or entero4==False or entero2==False:
                a=[]
                a.append(self.edad.get())
                a.append(self.celular.get())
                a.append(self.cedula.get())
                boleean=False
                for i in a:
                    
                    for j in i:
                        if j==".":
                            boleean=True
                            try:
                                raise ExcepcionEnteroFloat(entero3)
                            except ExcepcionEnteroFloat as e:
                                MessageBox.showerror(title="Error",message=e)
                            
                            if boleean==True:
                                return

                                                
                if boleean==False:
                    try:
                        raise ExcepcionStringNumero(entero3)
                    except ExcepcionStringNumero as e:
                        MessageBox.showerror(title="Error",message=e)
                    return


            #si los tipos de datos son ingresados correctamente crearemos una instacia de cliente
            newCliente=Cliente(self.cedula.get(), self.celular.get(), self.nombre.get(), self.combo2.get(), self.edad.get())
            if Funcionalidades.buscarCliente(newCliente)==None:
                self.clientesT.append(newCliente)
                messagebox.showinfo("Mensaje", "Se ha registrado") 
            else:
                MessageBox.showinfo("Mensaje", "Cliente antiguo") 
             
            #Aqui le van a salir un lista de peliculas dependiendo lo que haya selecionada antes, igual que las sillas
            self.frame2.pack_forget()
            self.frame4.pack_forget()
            self.frame3.pack_forget()
            self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
            self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

            self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
            self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

            selection = self.combo.get()        
            selection2 = self.combo2.get() 
            
            self.labelPelicula=Label(self.frame2, text="Selecione la Pelicula", font=("Arial",14))
            self.labelPelicula.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
            self.combo = Combobox(self.frame4, state="readonly",values=["si", "no"])
            self.combo.place(x=75, y=89)


            if selection=="si":
                self.combo = Combobox(self.frame2, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 1))
                self.combo.place(x=20, y=90)
            else:
                self.combo =Combobox(self.frame2, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 2))
                self.combo.place(x=20, y=90)
            
            botonSiguiente.destroy()
            
            #Aqui le van a salir las sillas disponibles
            def selecionar():
                titulo=tk.Label(self.frame3, text="Selecione la silla", font=("Arial",14))
                titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
                peli=self.combo.get()[0]
                if selection2=="si":
                    self.combo2 = Combobox(self.frame3, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 2,self.salas))
                    self.combo2.place(x=20, y=120)
                else:
                    self.combo2 =Combobox(self.frame3, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 1,self.salas)+Funcionalidades.buscarSillaLibre(int(peli), 3,self.salas))
                    self.combo2.place(x=20, y=120)

                #Esta funcion solo se ejecutara si el cliente pide un combo   
                def combo():
                    self.frame2.pack_forget()
                    self.frame4.pack_forget()
                    self.frame3.pack_forget()

                    self.frame2 = tk.Frame(self.frame, borderwidth=5, bg='#F98866' )

                    self.frame2.pack(expand=True,fill="x",ipadx = 0, ipady =0, padx = 2, pady= 2)

                    self.label= Label(self.frame2, text="¡¡Selecione en la imagen el combo que quiera!!", font=("Arial",25),bg='#F98866' )
                    self.label.pack()

                    self.frame3 = Frame(self.frame,width=400,borderwidth=15, height=350, bg='#F98866')
                    self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

                    self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
                    self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)


                    frameFoto1 = tk.Frame(self.frame3, width=200, height=170)
                    frameFoto1.place(x=50, y=0)

                    frameFoto2 = tk.Frame(self.frame3, width=200, height=170)
                    frameFoto2.place(x=310, y=0)

                    frameFoto3 = tk.Frame(self.frame3, width=200, height=170)
                    frameFoto3.place(x=570, y=0)

                    #guardmos en una lista las imagenes que van a aparecer en la seccion del combo   
                    fotosDesarolla = ['./imagenes/c1.png', './imagenes/c2.png', './imagenes/c3.png']
                    
                    for i in fotosDesarolla:
                        imagen = PhotoImage(file=i)
                        
                        self.listaFotos.append(imagen)
                
                    #si presiona una de las imagenes se realizara las siguiente funciones 
                    def combo1():
                        cliente= self.clientesT[len(self.clientesT)-1]

                        sala=Funcionalidades.buscarSala(1,self.salas)
                        cliente2=Funcionalidades.Combos(1,cliente,sala)
                        messagebox.showinfo("Mensaje", f"El cliente {cliente2.getNombre()} tiene que pagar: {cliente2.getCosto()}")
                    botonCambioa = Button(frameFoto1, image=self.listaFotos[0],command=combo1)
                    botonCambioa.pack()


                    def combo2():
                        cliente= self.clientesT[len(self.clientesT)-1]

                        sala=Funcionalidades.buscarSala(1,self.salas)
                        cliente2=Funcionalidades.Combos(2,cliente,sala)
                        messagebox.showinfo("Mensaje", f"El cliente {cliente2.getNombre()} tiene que pagar: {cliente2.getCosto()}")


                    botonCambioa = Button(frameFoto2, image=self.listaFotos[1],command=combo2)
                    botonCambioa.pack()





                    def combo3():
                        cliente= self.clientesT[len(self.clientesT)-1]

                        sala=Funcionalidades.buscarSala(1,self.salas)
                        cliente2=Funcionalidades.Combos(3,cliente,sala)
                        messagebox.showinfo("Mensaje", f"El cliente {cliente2.getNombre()} tiene que pagar: {cliente2.getCosto()}")

                        

                    
                    botonCambioa = Button(frameFoto3, image=self.listaFotos[2],command=combo3)
                    botonCambioa.pack()

                    botonSiguiente2.destroy()
                
                
                #EL boton de salir donde guardara la informacion y saldra de nuevo la pagina de inicio
                def salir():
                    self.frame2.pack_forget()
                    self.frame4.pack_forget()
                    self.frame3.pack_forget()
                    self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                    self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                    
                    self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                    self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                    
                    self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                    self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                    self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                    self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                    finalizar.destroy()
                    botonSiguiente2.destroy()

                finalizar=Button(self.frame, text="Finalizar", command=salir)
                finalizar.pack()
                    
                botonSiguiente2 = Button(self.frame,text= "Comparar combo",command=combo)
                botonSiguiente2.pack() 

            botonselecionar= Button(self.frame2, text="Selecionar",command=selecionar)
            botonselecionar.grid(column=0, row=12, ipadx=15, ipady=5, padx=25, pady=50)

        botonSiguiente = Button(self.frame,text= "Siguiente",command=siguiente)
        botonSiguiente.pack(ipadx = 0, ipady =0, padx = 2, pady= 2)           


#-----------------------------------------------------------------------------------------------------------------
    #Con este metodo realizaremos una busqueda en nuestra lista de cliente ya serealizada
    #aqui realizamos los frame correspondientes a esta funcion
    def buscarReserva(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        titulo=tk.Label(self.frame2, text="Ingrse la cedula del cliente", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        self.cedula=StringVar()
        self.cedula.set("")
        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=0, row=3, sticky='ew', padx=30, pady=10)

    #aqui vamos a buscar al cliente , llamando a la funcionalidad de buscar el cliente mediante la cecula que solictamos 
    #anteriormente
        def confirmar():
                       
            cliente=Funcionalidades.buscarClien(self.cedula.get())
            self.frame3.pack_forget()
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#FFFFFF')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            if cliente!=None:
                lanombre=tk.Label(self.frame3, text="Nombre", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)
                nombre=tk.Label(self.frame3, text=f"{cliente.getNombre()}", font=("Arial",14))
                nombre.grid(column=1,columnspan=4, row=1, padx=5, pady=5)
                
                lacedula=tk.Label(self.frame3, text="Cedula", font=("Arial",14))
                lacedula.grid(column=5,columnspan=9, row=0, padx=58, pady=5)
                cedula=tk.Label(self.frame3, text=f"{cliente.getCedula()}", font=("Arial",14))
                cedula.grid(column=5,columnspan=9, row=1, padx=5, pady=5)
            else:
                nombre=tk.Label(self.frame3, text="No existe", font=("Arial",14))
                nombre.grid(column=1,columnspan=4, row=0, padx=10, pady=50)
            
            botonconf.destroy()
            #Aqui vamos a restaurar nuestra ventana usuario principal
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()
            
        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack()

 
#----------------------------------------------------------------------------------------------------------
    #con este metodo vamos hacer una devolucion al cliente asigando a una determinda silla
 
    def devolucion(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        
        
        titulo=tk.Label(self.frame2, text="Ingrse la cedula del cliente", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        self.cedula=StringVar()
        self.cedula.set("")
        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=0, row=3, sticky='ew', padx=30, pady=10)

        #aqui llamos a la funcionalidad correspondiente
        def confirmar():
            buscar=Funcionalidades.buscarClien(self.cedula.get())
            if buscar!=None:
                cliente=Funcionalidades.devolucion(buscar,self.salas)
            else:
                cliente=None
            self.frame3.pack_forget()
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#FFFFFF')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            print(buscar)

            if cliente != None:
                lanombre=tk.Label(self.frame3, text=f"{cliente}", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)

            else:
                lanombre=tk.Label(self.frame3, text="No existe", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)
            botonconf.destroy()
            
            
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()

                

        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #con este metodo vamos a imprimir la lista de peliculas que hay en el cine
    def verCartelera(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        self.labelPelicula= Label(self.frame2, font=("Arial",14))
        self.labelPelicula.grid(column=0, row=0, ipadx=0, ipady=0, padx=15, pady=55)
        # l=Funcionalidades.verCartelera(self.labelPelicula)
        
        #restauramos la ventana de usuario
        def salir2():
            self.frame2.pack_forget()
            self.frame4.pack_forget()
            self.frame3.pack_forget()
            self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
            self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
            
            self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
            self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
            
            self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
            self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

            self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
            self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            botonsalir.destroy()

    
        botonsalir=Button(self.frame, text="Salir", command=salir2)
        botonsalir.pack(ipadx = 0, ipady =0, padx = 0, pady= 0)
    
#--------------------------------------------------------------------------------------------------------------
    #este metodo muestra una breve descripcion de la app

    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Mensaje", message = "Administrador de Cine",
        detail = "El sistema permite brindar las funcionalidades que mas se desarían en un portal virtual en el cine.")

#--------------------------------------------------------------------------------------------------------------
    # Retorna a la Ventana de Inicio del programa.

=======
>>>>>>> 0afa54539bcaa05fec9a62d3c9523de89988c549
    def salirVentana(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

#-------------------------------------------------------------------------------------------------------------------------------------
    # Muestra un Message Box con los nombres de los autores de la aplicación.
    def ayuda(self):
        mensaje = messagebox.showinfo(title = "Mensaje", message = "Autores: \n\n Sebastián Olaya Pérez: \n solayap@unal.edu.co\n Camilo Echeverrí Castrillón\n cecheverric@unal.edu.co\n Tomás Gutierrez Orrego\n tguttierrez@unal.edu.co\n Juan Jose Marín\n jumarina@unal.edu.co\n Julian Orrego Martinez\n jorrego@unal.edu.co")



