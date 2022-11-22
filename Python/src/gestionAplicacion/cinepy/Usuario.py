class Usuario:
    def __init__(self,nombre,cedula,membresia,saldo,boletas,carrito,cantidadUsuarios):
        self._nombre = nombre
        self._cedula = cedula
        self._membresia = membresia
        self._saldo = saldo
        self._boletas = boletas
        self._carrito = carrito
        self._cantidadUsuarios = cantidadUsuarios

    def getcantidadUsuarios(self):
            return self._cantidadUsuarios

    def __init__(self,nombre,cedula,saldo):
        self._nombre = nombre
        self._cedula = cedula
        self._saldo = saldo

    def __init__(self,nombre,cedula,saldo,boletas):
        self._nombre = nombre
        self._cedula = cedula
        self._saldo = saldo
        self._boletas = boletas
    
    def verificacionMemnresia(self):
        if self._membresia == True:
            return True
        else:
            return False

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getCedula(self):
        return self._cedula
    
    def setCeluda(self,cedula):
        self._cedula = cedula
    
    
    def getSaldo(self):
        return self._saldo
    
    def setSaldo(self,saldo):
        self._saldo = saldo
    
    def addSaldo(self,saldo):
        self._saldo += saldo

    def addBoleta(self,boleta):
        self._boletas.append(boleta)
    
    def getBoletas(self):
        return self._boletas
    
    def setBoletas(self,boletas):
        self._boletas = boletas
   
    def getcarrito(self):
        return self._carrito
            
    def setCarrito(self,carrito):
        self._carrito = carrito

    def addCarrito(self,carrito):
        self._carrito.append(carrito)

    def eliminarCarrito(self,carrito):
        self._carrito.remove(carrito)

    def vaciarCarrito(self):
        self._carrito = []

    def getBoletas(self):
        return self._boletas

    
    