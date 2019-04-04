# _*_ coding:utf-8 _*_
# Coche.java
# @author Álvaro García Fuentes

from vehiculos import Vehiculo

class Coche( Vehiculo.Vehiculo ):
    
    # Constructor de la clase
    def __init__( self ):
        super().__init__()
    
    # Función que muestra el mensaje 
    # de que el coche quema rueda
    def quemaRueda( self ):
        print( "El coche quema rueda." )

    # Fin de la clase Coche
