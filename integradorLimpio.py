
# ... (otros imports)
from Cargar_API_y_CSV import cargar_paises, ARCHIVO_CSV
from fsc_buscar_mostrar import mostrar_paises, buscar_pais, mostrar_resultados, mostrar_estadisticas, agregar_o_eliminar_pais, mostrar_menu
from fsc_filtrado import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from fsc_ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie





########################################################MENÚ DE OPCIONES############################################################################################################
def ejecutar_programa():
    paises = cargar_paises()

    
    # Si no se cargaron países (p.ej. archivo no encontrado), no continuamos.
    if not paises:
        print("No se pudieron cargar los datos de países. Saliendo del programa.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                mostrar_paises(paises)
            case "2":
                # buscar_pais(paises) # <--- Función de Mateo
                lista_resultados = buscar_pais(paises)
                mostrar_resultados(lista_resultados)
            case "3":
                # filtrar_por_continente(paises) # <--- Función de Mateo
                filtrar_por_continente(paises)
            case "4":
                # filtrar_por_poblacion(paises) # <--- Función de Mateo
                filtrar_por_poblacion(paises)
            case "5":
                filtrar_por_superficie(paises)
            case "6":
                ordenar_por_nombre(paises)
            case "7":
                ordenar_por_poblacion(paises)
            
            case "8":
                # pass # <--- Función de Amanda
                ordenar_por_superficie(paises)
            case "9":
                # pass # <--- Función de Amanda
                mostrar_estadisticas(paises)
            case "10":
                # pass # <--- Función de Amanda
                agregar_o_eliminar_pais(paises)
            case "11":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
################################################################################################################################################################################

if __name__ == "__main__":
    ejecutar_programa()


