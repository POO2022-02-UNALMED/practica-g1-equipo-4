from excepcionesPy.excepcionesFuncionalidad import excepcionesFuncionalidad

class errorDevolucion(excepcionesFuncionalidad):
    def __init__(self, consulta ,parametro):
        super().__init__(f"Su consulta de {consulta} con el parametro {parametro} falló\n Por favor contacte al administrador del sistema")