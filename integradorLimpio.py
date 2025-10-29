
# ... (otros imports)
from Cargar_API_y_CSV import cargar_paises, ARCHIVO_CSV
from fsc_buscar_mostrar import mostrar_paises, buscar_pais, mostrar_resultados, mostrar_estadisticas, agregar_o_eliminar_pais
from fsc_filtrado import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from fsc_ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
# ... (el resto de tus imports)
####################################################################CARGAMOS EL CSV############################################################################################################
#TRATAR DE MODULARIZAR ANTES QUE COMENZAR A CAMBIAR LOS NOMBRES DE LAS VARIABLES ASI SE HACE MAS COMODO CAMBIARLAS DESPUES
#MODIFICAR LAS FUNCIONES Y VARIABLES PARA QUE FUNCIONEN CORRECTAMENTE (FIJENSE BIEN COMO ESTÁN ESCRITAS EN LA OPCION FINAL (MOSTRAR PAISES Y COMO ESTA EN LA OPCION 2 FILTRAR POR NOMBRE))
#MODULARIZAR TODAS LAS FUNCIONES Y HACERLAS POR EJEMPLO (UNA FUNCION LLAMADA DATOS_PAISES, TIENE QUE TENER LA FUNCION "BUSCAR PAISES" Y "BUSCAR PAIS POR NOMBRE")
#CREAR UNA OPCION DE OS POR SI EL ARCHIVO NO EXISTE, YA QUE ESTAMOS CARGANDO UNA API, O SEA EL ARCHIVO SIEMPRE VA A EXISTIR, PERO EN CASO DE QUE NO EXISTA, QUE LO CREE
#SOLUCIONAR EL PROBLEMA (con ayuda de los profes si es posible y IA) COMO CARGAR LA SUPERFICIE DENTRO DEL CSV, YA QUE LA API NO LA TRAE, POR LO TANTO HAY QUE BUSCAR OTRA FORMA DE CONSEGUIRLA
#AGREGAR UNA NUEVA VARIABLE QUE SE LLAME "CAPITAL"
#MODIFICAR LAS FUNCIONES PARA QUE TRAIGAN LA CAPITAL Y LA MUESTREN EN PANTALLA (VA A QUEDAR VER LO DE LA SUPERFICIE, PARA LO QUE ACABO DE DECIR MIREN LA OPCION 1 (AL FINAL DEL TODO)

import Cargar_API_y_CSV
import fsc_buscar_mostrar

########################################################MENÚ DE OPCIONES############################################################################################################
def ejecutar_programa():
    paises = cargar_paises()

    
    # Si no se cargaron países (p.ej. archivo no encontrado), no continuamos.
    if not paises:
        print("No se pudieron cargar los datos de países. Saliendo del programa.")
        return

    while True:
        fsc_buscar_mostrar.mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            match opcion:
                case 1:
                    fsc_buscar_mostrar.mostrar_paises(paises)
                case 2:
                    resultados = fsc_buscar_mostrar.buscar_pais(paises)
                    fsc_buscar_mostrar.mostrar_resultados(resultados)
                case 3:
                    # filtrar_por_continente(paises) # <--- Función de Mateo
                    #filtrar_por_continente(paises)
                    pass
                case 4:
                    # filtrar_por_poblacion(paises) # <--- Función de Mateo
                    # filtrar_por_poblacion(paises)i
                    pass
                case 5:
                    # filtrar_por_superficie(paises)
                    pass
                case 6:
                    # ordenar_por_nombre(paises)
                    pass
                case 7:
                    # ordenar_por_poblacion(paises)
                    pass
                case 8:
                    # pass # <--- Función de Amanda
                    # ordenar_por_superficie(paises)
                    pass
                case 9:
                    # pass # <--- Función de Amanda
                    # mostrar_estadisticas(paises)
                    pass
                case 10:
                    # pass # <--- Función de Amanda
                    # agregar_o_eliminar_pais(paises)
                    pass
                case 11:
                    print("¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Opcion Invalida")
################################################################################################################################################################################

if __name__ == "__main__":
    ejecutar_programa()


