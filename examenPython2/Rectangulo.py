#_*_ coding=UTF-8 _*_
# ejercicio2.py
# Definicion de la clase Rectangulo
# @author Álvaro García Fuentes

class Rectangulo:

    # Constructor paramétrico
    # @param ancho
    # @param alto
    def __init__( self , ancho , alto ):
        self.ancho = ancho
        self.alto = alto

    # propiedades 
    @property
    def ancho( self ):
        return self.__ancho
    @property
    def alto( self ):
        return self.__alto

    # modificadores de las propiedades
    @ancho.setter
    def ancho( self, ancho ):
        if(  ( ancho <= 0 ) or ( ancho > 10 )  ):
            raise ArithmeticError
        else:
            self.__ancho = ancho

    @alto.setter
    def alto( self, alto ):
        if(  ( alto <= 0 ) or ( alto > 10 )  ):
            raise ArithmeticError
        else:
            self.__alto = alto

    # funcion para dibujar el rectángulo por pantalla
    def __str__( self ):
        i = 0
        rectangulo = ""
        while ( i < self.alto ):
            j = 0
            while( j < self.ancho ):
                rectangulo += "[]"
                j += 1
            rectangulo += '\n'
            i += 1

        return rectangulo

# Fin de la clase Rectangulo
