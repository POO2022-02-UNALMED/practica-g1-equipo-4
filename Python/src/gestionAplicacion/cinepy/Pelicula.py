class Pelicula:

    pelicula = []

    def __init__(self, nombre, genero):
        self._nombre = nombre
        self._genero = genero

    def getNombre(self):
        return self._nombre
    
    def getGenero(self):        
        return self._genero
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def setGenero(self, genero):
        self._genero = genero

    @staticmethod
    def getPelicula():
        return Pelicula.pelicula
    
    @staticmethod
    def setPelicula(pelicula):
        Pelicula.pelicula.append(pelicula)
    
        