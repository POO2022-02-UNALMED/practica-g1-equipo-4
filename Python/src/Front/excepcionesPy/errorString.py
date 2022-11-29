from excepcionesPy.excepcionesFormato import excepcionesFormato

class errorString(excepcionesFormato):
    def __init__(self, error):
        super().__init__(f"El parametro {error} debe ser un conjunto de caracteres")