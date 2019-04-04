#_*_ coding:utf-8 _*_
# Bicicleta.py
# @author Álvaro García Fuentes

from vehiculos import Vehiculo

class Bicicleta( Vehiculo.Vehiculo ):
    
    # Constructor de la clase
    def __init__( self ):
        super().__init__()
    
    # Función que muestra por pantalla
    # el mensaje de que la bici hace un caballito
    def caballito( self ):
        print( "La bici hace un caballito." )
    
    # Fin de la clase Bicicleta
