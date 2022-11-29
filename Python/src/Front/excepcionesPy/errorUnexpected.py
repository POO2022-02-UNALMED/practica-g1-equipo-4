from excepcionesPy.excepcionesFuncionalidad import excepcionesFuncionalidad

class errorUnexpected(excepcionesFuncionalidad):
    def __init__(self, parametro):
        super().__init__(f"Error inesperado:{parametro} \n Por favor contacte al administrador del sistema")
        
