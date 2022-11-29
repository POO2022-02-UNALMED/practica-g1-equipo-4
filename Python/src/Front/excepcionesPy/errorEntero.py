#import excepcionesFormato
from excepcionesPy.excepcionesFormato import excepcionesFormato

class errorEntero(excepcionesFormato):
    def __init__(self, error):
        super().__init__(f"El parametro {error} debe ser un numero entero")