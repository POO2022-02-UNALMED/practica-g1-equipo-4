
class errorAplicacion(Exception):
    def __init__(self, error):
        super().__init__(f"Manejo de errores de la aplicacion:\n{error}")