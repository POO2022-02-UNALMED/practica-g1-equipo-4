# cre
class boleta:

    @staticmethod
    def getPrecio():
        return 10000

    def __init__(self, usuario, pelicula, sala, asientos, horario, dia):
        self._usuario = usuario
        self._pelicula = pelicula
        self._sala = sala      
        self._asientos = asientos
        self._horario = horario
        self._dia = dia

    def getUsuario(self):
        return self._usuario

    def getPelicula(self):
        return self._pelicula

    def getSala(self):

        return self._sala

    def getAsientos(self):
        return self._asientos

    def getHorario(self):
        return self._horario

    def getDia(self):
        return self._dia

    def setUsuario(self, usuario):
        self._usuario = usuario

    def setPelicula(self, pelicula):
        self._pelicula = pelicula

    def setSala(self, sala):
        self._sala = sala

    def setAsientos(self, asientos):
        self._asientos = asientos

    def setHorario(self, horario):
        self._horario = horario

    def setDia(self, dia):
        self._dia = dia

    