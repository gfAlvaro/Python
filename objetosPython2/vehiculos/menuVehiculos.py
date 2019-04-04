# _*_ coding:utf-8 _*_
# menuVehiculos.java
# @author Álvaro Garía Fuentes

from vehiculos import Vehiculo
from vehiculos import Bicicleta
from vehiculos import Coche

# Función para mostrar un menú en pantalla.
def mostrarMenu():
    print( "VEHÍCULOS" )
    print( "=========" )
    print( "1. Anda con la bicicleta" )
    print( "2. Haz el caballito con la bicicleta" )
    print( "3. Anda con el coche" )
    print( "4. Quema rueda con el coche" )
    print( "5. Ver kilometraje de la bicicleta" )
    print( "6. Ver kilometraje del coche" )
    print( "7. Ver kilometraje total" )
    print( "8. Salir" )
    print( "Elige una opción (1-8): " )

#
# Programa principal de menuVehiculos
#
if __name__ == '__main__':
    salir = False
    bici = Bicicleta.Bicicleta()
    cochazo = Coche.Coche()
        
    while salir == False:
        mostrarMenu();
        opcion = int( input() )
    
        if( opcion == 1 ):
            bici.andar()
        elif( opcion == 2 ):
            bici.caballito()
        elif( opcion == 3 ):
            cochazo.andar()
        elif( opcion == 4 ):
            cochazo.quemaRueda()
        elif( opcion == 5 ):
            print( bici.kilometrosRecorridos )
        elif( opcion == 6 ):
            print( cochazo.kilometrosRecorridos )
        elif( opcion == 7 ):
            print(  Vehiculo.Vehiculo.kilometrosTotales  )
        elif( opcion == 8 ):
            salir = True;
            print( "Saliendo..." )
        else:
            print( "Opción Incorrecta." )
    
        print()

# Fin del programa
