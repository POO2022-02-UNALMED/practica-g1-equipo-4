class Horario:
    def __init__(self, horarioInicio, horarioFin):
        self._horarioInicio = horarioInicio
        self._horarioFin = horarioFin
    
    def getHorarioInicio(self):
        return self._horarioInicio

    def getHorarioFin(self):
        return self._horarioFin

    def setHorarioInicio(self, horarioInicio):
        self._horarioInicio = horarioInicio

    def setHorarioFin(self, horarioFin):
        self._horarioFin = horarioFin

