class Dia:
    dias = []
    def __init__ (self, nombre, sala):
        self.nombre = nombre
        self.sala = sala

    def getNombre(self):
        return self.nombre

    def getSala(self):
        return self.sala

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSala(self, sala):
        self.sala = sala

    @staticmethod
    def getDia():
        return Dia.dias
    
    @staticmethod
    def setDia(dia):
        Dia.dias.append(dia)
        

        