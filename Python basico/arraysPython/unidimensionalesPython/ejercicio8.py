# -*- coding: utf-8 -*-
# ejercicio8.py
# Programa que pide la temperatura media que ha hecho en cada mes
# de un determinado año y muestra a continuación un diagrama de barras
# horizontales con esos datos. Las barras del diagrama se dibujan a base
# de asteriscos.

# entrada de datos
year = []
for i in range( 0 , 12 ):
    print( "Introducir temperatura del " + str( i+1 ) + "er mes" , end=" " )
    year.append(  int( input() )  )
 
# crear diagrama de barras   
for i in range( 0 , 12 ):
    for j in range(  int( year[i] / 2 )  ):
        print( "*" , end="" )
    print(  " " + str( year[i] )  )

# Fin del programa