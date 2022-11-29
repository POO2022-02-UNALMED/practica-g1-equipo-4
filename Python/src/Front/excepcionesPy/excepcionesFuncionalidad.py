from excepcionesPy.errorAplicacion import errorAplicacion

class excepcionesFuncionalidad(errorAplicacion):
    def __init__(self, parametro):
        super().__init__(f"Error de la funcionalidad:\n{parametro}")

    