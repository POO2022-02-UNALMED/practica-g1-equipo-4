from excepcionesPy.errorAplicacion import errorAplicacion

class excepcionesFormato (errorAplicacion):
    def __init__(self, parametro):
        super().__init__(f"Error de formato:\n{parametro}")

 
    