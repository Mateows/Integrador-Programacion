
import Cargar_API_y_CSV
from fsc_buscar_mostrar import mostrar_resultados, buscar_pais, _mostrar_paises_lista





# #Funcion para filtrar paises por continente
def filtrar_por_continente(paises):
    #Buscamos el continente que el usuario ingrese
    continente = input("Ingrese el continente para filtar: ").strip().title()
    resultados = []
    #Recorremos el archivo, si lo que se ingreso es igual a algún continente, lo almacenamos en resultados
    for pais in paises:
        if pais["region"] == continente:
            resultados.append(pais)

# #En caso de que se guarde algun continente en resultados o no, mostramos el mensaje correspondiente
    if resultados:
        print(f"\n{'Nombre':<45} | {'Población':<15} | {'Superficie (km²)':<20} | {'Continente':<20}")
        print("-" * 80)
        for pais in resultados:
            nombre = pais.get('nombre', 'N/A')
            poblacion = pais.get('poblacion', 0)
            superficie = pais.get('superficie', 0)
            continente = pais.get('region', 'N/A')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<45} | {poblacion:<15,d} | {superficie:<20,.2f} | {continente:<20}")
    else:
        print("No hay coincidencias con el continente ingresado")

#-----------------------------------------------------------------------------------------




def filtrar_por_superficie(paises):
    """
    Filtra la lista de países por superficie, con validaciones robustas
    Permite una sub-búsqueda por nombre dentro de los resultados.
    """
    print("\n--- 5. Filtrar Países por Superficie ---")
    try:
        # (Validación de superficie...)
        superficie_limite = -1
        while superficie_limite <= 0:
            try:
                entrada = input("Ingrese el valor de superficie (en km², debe ser > 0): ").strip().replace(",", "")
                if entrada == "":
                    print("Error: No ingresó ningún valor. Intente de nuevo.")
                    continue
                
                superficie_limite = float(entrada)
                
                if superficie_limite <= 0:
                    print("Error: La superficie debe ser un número positivo.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número.")
                superficie_limite = -1
        
        # (Validación de criterio...)
        criterio = ""
        while criterio not in ('>', '<'):
            criterio = input("¿Mostrar países 'mayor que' (>) o 'menor que' (<) este valor? ").strip().lower()
            if criterio in ("mayor", "mayor que"):
                criterio = ">"
            elif criterio in ("menor", "menor que"):
                criterio = "<"
            
            if criterio not in ('>', '<'):
                print("Error: Criterio no válido. Ingrese 'mayor', 'menor', '>' o '<'.")

        # Lógica de filtrado
        paises_filtrados = []
        if criterio == '>':
            paises_filtrados = [pais for pais in paises if pais.get("superficie", 0) > superficie_limite]
        elif criterio == '<':
            paises_filtrados = [pais for pais in paises if pais.get("superficie", 0) < superficie_limite]

        print(f"\nPaíses con superficie {criterio} {superficie_limite:,.2f} km²:")
        
        mostrar_resultados(paises_filtrados)
        
        # --- INICIO DE MEJORA (IDEA 3): BÚSQUEDA ANIDADA ---
        if paises_filtrados: # Solo preguntar si hay resultados
            while True:
                respuesta_buscar = input(f"\n¿Desea buscar por nombre DENTRO de estos {len(paises_filtrados)} resultados? (S/N): ").strip().upper()
                
                if respuesta_buscar == 'S':
                    print("\n--- Búsqueda dentro de resultados ---")
                    sub_resultados = buscar_pais(paises_filtrados) # Reutilizamos buscar_pais
                    mostrar_resultados(sub_resultados) # Reutilizamos mostrar_resultados
                    print("--- Fin de la sub-búsqueda ---")
                
                elif respuesta_buscar == 'N':
                    break # Salir del bucle de "buscar dentro"
                
                else:
                    print("Opción inválida. Ingrese 'S' o 'N'.")
        # --- FIN DE MEJORA ---
        
        # (Manejamos el caso de que la lista original estuviera vacía)
        elif not paises_filtrados and criterio: 
            pass # El 'mostrar_resultados' ya habrá dicho "No se encontraron coincidencias"
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

#--------------------------------------------------------------------------------------------------------------------------


# #Función para filtrar países por población
def filtrar_por_poblacion(paises):
    """
    Filtra países por un rango de población (mínimo y máximo).
    Permite una sub-búsqueda por nombre dentro de los resultados.
    """
    print("\n--- 4. Filtrar Países por Población ---")
    resultados = []
    poblacion_minima = -1
    poblacion_maxima = -1

    # (Validación de población mínima...)
    while poblacion_minima < 0:
        try:
            entrada = input("Ingrese la población mínima: ").strip().replace(",", "").replace(".", "")
            if not entrada.isdigit():
                print("Error: Ingrese solo números positivos.")
                continue
            poblacion_minima = int(entrada)
            if poblacion_minima < 0:
                print("El número debe ser positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero positivo.")

    # (Validación de población máxima...)
    while poblacion_maxima < poblacion_minima:
        try:
            entrada = input("Ingrese la población máxima: ").strip().replace(",", "").replace(".", "")
            if not entrada.isdigit():
                print("Error: Ingrese solo números positivos.")
                continue
            poblacion_maxima = int(entrada)
            if poblacion_maxima < poblacion_minima:
                print(f"ERROR. La población máxima debe ser mayor o igual a la mínima ({poblacion_minima:,d}).")
        except ValueError:
            print("ERROR. Por favor ingrese un número entero positivo.")

    # Lógica de filtrado
    resultados = [pais for pais in paises if poblacion_minima <= pais.get("poblacion", 0) <= poblacion_maxima]

    # Lógica de impresión
    if resultados:
        print(f"\nPaíses con población entre {poblacion_minima:,d} y {poblacion_maxima:,d} habitantes:")
        mostrar_resultados(resultados)
        
        # --- INICIO DE MEJORA (IDEA 3): BÚSQUEDA ANIDADA ---
        while True:
            respuesta_buscar = input(f"\n¿Desea buscar por nombre DENTRO de estos {len(resultados)} resultados? (S/N): ").strip().upper()
            
            if respuesta_buscar == 'S':
                print("\n--- Búsqueda dentro de resultados ---")
                sub_resultados = buscar_pais(resultados) # Reutilizamos buscar_pais con la lista filtrada
                mostrar_resultados(sub_resultados) # Reutilizamos mostrar_resultados
                print("--- Fin de la sub-búsqueda ---")
                break
            
            elif respuesta_buscar == 'N':
                break # Salir del bucle de "buscar dentro"
            
            else:
                print("Opción inválida. Ingrese 'S' o 'N'.")
        # --- FIN DE MEJORA ---
            
    else:
        print("\nNo se encontraron países en ese rango de población.")
################################################################################################################################################################################


