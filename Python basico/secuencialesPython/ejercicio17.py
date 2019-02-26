# ejercicio17.py
# Un ciclista parte de una ciudad A
# a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B
# es de T segundos. Escribir un algoritmo
# que determine la hora de llegada a la ciudad B.
# @author Alvaro Garcia Fuentes

print( "Introduzca la hora." )
hora = (  int( input( " Horas: " ) )  )
minutos = (  int( input( " Minutos: " ) )  )
segundos = (  int( input( " Segundos: " ) )  )

tiempoViaje = (  int( input( "Introduzca el tiempo de viaje en segundos: " ) )  )

segundos = segundos + tiempoViaje
minutos = minutos + (  int( segundos / 60 )  )
hora = hora + (  int( minutos / 60 )  )

segundos = segundos % 60
minutos = minutos % 60
hora = hora % 24

print( "Hora de llegada:" , hora , ":" , minutos , ":" , segundos )

# Fin del programa
