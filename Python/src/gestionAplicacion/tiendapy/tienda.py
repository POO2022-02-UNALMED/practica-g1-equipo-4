class tienda:
    def __init__(self, nombre, inventario, productos):
        self.nombre = nombre
        self.inventario = inventario
        self.productos = productos

    def getNombre(self):
        return self.nombre

    def getInventario(self):
        return self.inventario

    def getProductos(self):
        return self.productos

    def setNombre(self, nombre):
        self.nombre = nombre

    def setInventario(self, inventario):
        self.inventario = inventario

    def setProductos(self, productos):
        self.productos = productos

    def __str__(self):
        return self.nombre