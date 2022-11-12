class Usuario:
    def __init__(self,nombre,cedula,membresia,saldo,boletas,carrito,cantidadUsuarios):
        self._nombre = nombre
        self._cedula = cedula
        self._membresia = membresia
        self._saldo = saldo
        self._boletas = boletas
        self._carrito = carrito
        self._cantidadUsuarios = cantidadUsuarios

    def getNombre(self):
        return self._nombre
        
    def getCedula(self):
        return self._cedula
    
    def getMembresia(self):
        return self._membresia
    
    def getSaldo(self):
        return self._saldo
    
    def getBoletas(self):
        return self._boletas
    
    def getCarrito(self):
        return self._carrito
    
    