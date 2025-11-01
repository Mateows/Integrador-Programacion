
from Cargar_API_y_CSV import cargar_paises, ARCHIVO_CSV
from fsc_buscar_mostrar import mostrar_paises, buscar_pais, mostrar_resultados, mostrar_menu, mostrar_idiomas
from fsc_filtrado import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from fsc_ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from fsc_estadisticas import mostrar_estadisticas
from fsc_agregar_borrar_paises import agregar_editar_eliminar_pais




########################################################MENÚ DE OPCIONES############################################################################################################
def ejecutar_programa():
    paises = cargar_paises()

    
    # Si no se cargaron países (p.ej. archivo no encontrado), no continuamos.
    if not paises:
        print("No se pudieron cargar los datos de países.")
        print("Continuando con una lista vacia")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                mostrar_paises(paises) #Muestra todos los paises -> se llama desde fsc_buscar_mostrar
            case "2":
                # Busca paises por coincidencia parcial o total -> Se llama desde fsc_buscar_mostrar
                buscar_pais(paises)
            case "3":
                # Filtra todos los continentes -> Se llama desde fsc_filtado
                filtrar_por_continente(paises)
            case "4":
                # filtrar_por_poblacion(paises) # Se llama desde fsc_filtrados
                filtrar_por_poblacion(paises)
            case "5":
                #Filtra las poblaciones (se puede elegir cantidad de paises a filtrar) -> Se llama desde fsc_filtrado
                filtrar_por_superficie(paises)
            case "6":
                #Ordena los paises de forma ascendente/descendente y trae X cantidad de paises (seleccionable) -> Se llama desde fsc_ordenamiento
                ordenar_por_nombre(paises)
            case "7":
                #Ordena los paises de forma ascendente/descendente y trae X cantidad de paises con su población (seleccioanble) -> Se llama desde fsc_ordenamiento
                ordenar_por_poblacion(paises)
            case "8":
                #Ordena la superficie de los paises de forma ascendente/descendente, trae TODOS los paises -> Se llama desde fsc_ordenamiento
                ordenar_por_superficie(paises)
            case "9":
                #Muestra las estadisticas de TODOS los paises -> Se llama desde fsc_estadisticas
                mostrar_estadisticas(paises)
            case "10":
                #Agrega un nuevo pais o lo borra -> Se llama desde fsc_agregar_borrar_pais
                agregar_editar_eliminar_pais(paises, "paises.csv")
            case "11":
                mostrar_idiomas(paises)
            case "12":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
################################################################################################################################################################################

if __name__ == "__main__":
    ejecutar_programa()


