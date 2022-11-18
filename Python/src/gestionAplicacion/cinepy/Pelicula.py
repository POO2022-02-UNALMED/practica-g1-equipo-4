class Pelicula:
    def __init__(self, nombre, genero):
        self._nombre = nombre
        self._genero = genero

    def getNombre(self):
        return self._nombre
    
    def getGenero(self):        
        return self._genero
        