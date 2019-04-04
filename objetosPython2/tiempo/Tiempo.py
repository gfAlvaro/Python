#_*_ coding:utf-8 _*_
# Tiempo.py
# Clase Tiempo con los métodos suma y resta.
# Los objetos de la clase Tiempo son intervalos de tiempo
# y se crean de la forma Tiempo t = new Tiempo(1, 20, 30)
# donde los parámetros que se le pasan al constructor
# son las horas, los minutos y los segundos respectivamente.
# Contiene el método toString para ver los intervalos de tiempo
# de la forma 10h 35m 5s. Si se suman por ejemplo 30m 40s y
# 35m 20s el resultado debería ser 1h 6m 0s.
# @author Álvaro García Fuentes

class Tiempo:
	
	# constructor paramétrico 
	def __init__( self , horas , minutos , segundos ):
		
		self.segundos = segundos	
		self.minutos = minutos
		self.horas = horas
		
		if( self.segundos < 0 ):
			self.segundos = 0
		if( self.minutos < 0 ):
			self.minutos = 0
		if( self.horas < 0 ):
			self.horas = 0
			
		if( segundos >= 60 ):
			self.minutos += int( segundos / 60 )
			self.segundos = segundos % 60
		if( minutos >= 60 ):
			self.horas += int( minutos / 60 )
			self.minutos = minutos % 60
		if( horas >= 24 ):
			self.horas += horas  % 24
	
	# método toString
	def __str__( self ):
		return str( self.horas ) + "h " + str( self.minutos ) + "m " + str( self.segundos ) + "s"
	
	# métodos de la clase
	def suma( self , tiempo ):
		
		self.segundos += tiempo.segundos
		self.minutos += tiempo.minutos
		self.horas += tiempo.horas

		if( self.segundos >= 60 ):
			self.segundos -= 60
			self.minutos += 1
		
		if( self.minutos >= 60 ):
			self.minutos -= 60
			self.horas += 1
		
		if( self.horas >= 24 ):
			self.horas += tiempo.horas - 24
	
	def resta( self , tiempo ):
		
		self.horas -= tiempo.horas
		self.minutos -= tiempo.minutos
		self.segundos -= tiempo.segundos
		
		if( self.segundos < 0 ):
			self.segundos += 60
			self.minutos -= 1	
		
		if( self.minutos < 0 ):
			self.minutos += 60
			self.horas -= 1

		if( self.horas < 0 ):
			self.horas += 24
	
	# Fin de la clase Tiempo

