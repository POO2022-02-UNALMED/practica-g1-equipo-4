# importar clases de gestion de datos y funciones
from gestionAplicacion.cinepy.Boleta import Boleta
from gestionAplicacion.cinepy.Dia import Dia
from gestionAplicacion.cinepy.Horario import Horario
from gestionAplicacion.cinepy.Pelicula import Pelicula
from gestionAplicacion.cinepy.Sala import Sala
from gestionAplicacion.cinepy.Usuario import Usuario
from gestionAplicacion.tiendapy.Tienda import Tienda
from gestionAplicacion.tiendapy.TiendaUN import TiendaUN


import pickle

class Funcionalidades(object):

    pickle_salas = open('/baseDatos/salas', 'rb')
    pickle_usuario = open('/baseDatos/usuario', 'rb')
    pickle_tiendas = open('/baseDatos/tiendas', 'rb')
    pickle_boletas = open('/baseDatos/boletas', 'rb')
    
    Sala.sala = pickle.load(pickle_salas)
    Usuario.usuario = pickle.load(pickle_usuario)
    Tienda.tiendas = pickle.load(pickle_tiendas)
    TiendaUN.tiendaUN = pickle.load(pickle_tiendas)
    Boleta.boletas = pickle.load(pickle_boletas)

    







