from gestionAplicacion.tiendapy.Tienda import Tienda


class TiendaUN(Tienda):

    tiendaUN = []
    # inventario is a dictionary of String:Integer
    # productos is a dictionary of String:Integer
    def __init__(self, nombre, inventario, productos):
        super.__init__(self, nombre, inventario, productos)
       
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

    def venderProducto(self, producto):
        if (self.productos[producto] > 0):
            if (usuario.getSaldo() >= self.productos[producto]):
                if (usuario.isVip()):
                    self.productos[producto] = self.productos[producto] - 1
                    usuario.setSaldo(usuario.getSaldo() - self.productos[producto]*0.8)
                    print("Gracias por su compra")
            else:
                print("No tiene suficiente dinero")
        else:
            print("No hay suficientes productos")

def agregarMixto(self, producto, cantidadUnidades, precio):
        self.productos[producto] = precio
        self.inventario[producto] = cantidadUnidades
    
def __str__(self):
    return "Bienvenido a la tienda de la UN"

def getTiendaUN():
    return Tienda.tienda

def setTiendaUN(tiendaUN):
    Tienda.tienda.append(tiendaUN)

