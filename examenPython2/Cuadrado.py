#_*_ coding=UTF-8 _*_
# ejercicio1.py
# Definicion de la clase Cuadrado,
# que hereda de la clase Rectangulo
# @author Álvaro García Fuentes

from Rectangulo import Rectangulo

class Cuadrado ( Rectangulo ):

    # Constructor paramétrico
    # @param lado
    def __init__( self , lado ):
        super().__init__( lado , lado );

    # propiedad de la clase
    # que hereda las propiedades de Rectangulo
    # @return int
    @property
    def lado( self ):
        return super().alto

    # modificador de la propiedad de la clase
    # que hereda las propiedades de Rectangulo
    # @return int
    @lado.setter
    def lado( self, l ):
        super().alto(l)
        super().ancho(l)

    # operador de sobrecarga para comparar dos Cuadrados
    # @param cuadrado
    # @return boolean
    def __eq__( self , cuadrado ):
        return self.lado == cuadrado.lado

    # operador de sobrecarga para comparar dos Cuadrados
    # @param cuadrado
    # @return boolean
    def __gt__( self , cuadrado ):
        return self.lado > cuadrado.lado

    # operador de sobrecarga para comparar dos Cuadrados
    # @param cuadrado
    # @return boolean
    def __lt__( self , cuadrado ):
        return self.lado < cuadrado.lado

# Fin de la clase Cuadrado
