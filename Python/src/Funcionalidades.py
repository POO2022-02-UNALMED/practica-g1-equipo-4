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
    
    #Funcion para cuando le demos salir empiece a serializar el programa y guarde la informacion

    @staticmethod
    def salirDelSistema():
        pickle_salas = open('/baseDatos/salas', 'wb')
        pickle_usuario = open('/baseDatos/usuario', 'wb')
        pickle_tiendas = open('/baseDatos/tiendas', 'wb')
        pickle_boletas = open('/baseDatos/boletas', 'wb')
        
        pickle.dump(Sala.sala, pickle_salas)
        pickle.dump(Usuario.usuario, pickle_usuario)
        pickle.dump(Tienda.tiendas, pickle_tiendas)
        pickle.dump(TiendaUN.tiendaUN, pickle_tiendas)
        pickle.dump(Boleta.boletas, pickle_boletas)
        
        pickle_salas.close()
        pickle_usuario.close()
        pickle_tiendas.close()
        pickle_boletas.close()
        
        exit()









