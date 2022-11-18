# importar clases de gestion de datos y funciones
from gestionAplicacion.cinepy.Boleta import Boleta
from gestionAplicacion.cinepy.Dia import Dia
from gestionAplicacion.cinepy.Horario import Horario
from gestionAplicacion.cinepy.Pelicula import Pelicula
from gestionAplicacion.cinepy.Sala import Sala
from gestionAplicacion.cinepy.Usuario import Usuario
import pickle

class Funcionalidades(object):

    pickle_file = open('/baseDatos/salas', 'rb')
    pickle_file = open('/baseDatos/Usuario', 'rb')
    pickle_file = open('/baseDatos/tiendaUN', 'rb')
    pickle_file = open('/baseDatos/tiendaComida', 'rb')
    
    Sala = pickle.load(pickle_file)


