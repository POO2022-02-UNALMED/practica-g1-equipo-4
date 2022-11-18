class Sala:
    def __init__(self, nombre, asientos, cartelera):
        self.nombre = nombre
        self.asientos = asientos
        self.cartelera = cartelera


    def getNombre(self):
        return self.nombre

    def getAsientos(self):
        return self.asientos

    def getCartelera(self):
        return self.cartelera

    def setNombre(self, nombre):
        self.nombre = nombre

    def setAsientos(self, asientos):
        self.asientos = asientos

    def setCartelera(self, cartelera):
        self.cartelera = cartelera

    def __str__(self):
        return self.nombre 

    