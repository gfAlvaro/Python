# ejercicio8.py
# Un vendedor recibe un sueldo base mas un 10%
# extra por comisión de sus ventas, el vendedor desea
# saber cuanto dinero obtendrá por concepto de comisiones
# por las tres ventas que realiza en el mes y el total que
# recibirá en el mes tomando en cuenta su sueldo base y comisiones.
# @author Alvaro Garcia Fuentes

base = (  float( input( "Introduzca el sueldo base: " ) )  )

comisiones = 3 * base * 0.1
total = base + comisiones

print( "Sueldo base:" , base , "Comisiones:" , comisiones , "Total:" , total )

# Fin del programa