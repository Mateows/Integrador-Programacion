import csv
from fsc_buscar_mostrar import mostrar_resultados

#Funcion para ordenar lo que se le solicite
def _obtener_orden():
    """
    Función auxiliar para preguntar al usuario el orden (Asc/Desc).
    Devuelve el parámetro 'reverse' para la función sorted().
    """
    while True:
        orden = input("¿En qué orden? (ASC = Ascendente / DESC = Descendente): ").strip().upper()
        if orden == "ASC":
            return False  # reverse=False
        elif orden == "DESC":
            return True   # reverse=True
        else:
            print("Opción inválida. Escriba 'ASC' o 'DESC'.")

# --- Función para limitar los resultados a un número que eliga el usuario o ninguno (muestra todo) ---
def _limitar_resultados(lista_ordenada):
    """
    Función auxiliar para preguntar al usuario si desea limitar los resultados.
    Devuelve la lista completa o una versión "rebanada" (sliced).
    """
    if not lista_ordenada: # Si la lista está vacía, no preguntar nada
        return lista_ordenada
        
    while True:
        print(f"\nSe encontraron {len(lista_ordenada)} países.")
        respuesta = input("¿Mostrar todos (T) o solo los N primeros? (Ingrese 'T' o un número N): ").strip().upper()
        
        if respuesta == 'T':
            return lista_ordenada
        
        if respuesta.isdigit():
            n = int(respuesta)
            if n > 0:
                print(f"Mostrando los {n} primeros resultados...")
                return lista_ordenada[:n] # Slicing [:n] obtiene los primeros 'n' elementos
            else:
                print("Error: El número debe ser positivo. Intente de nuevo.")
        else:
            print("Error: Opción inválida. Ingrese 'T' o un número.")


# --- TAREA 6: ORDENAR PAÍSES POR NOMBRE ---
def ordenar_por_nombre(lista_paises):
    if not lista_paises:
        print("No hay paises cargados aún")
        return
    """
    Muestra la lista de países ordenada alfabéticamente por nombre,
    permitiendo al usuario elegir el orden (ASC/DESC) y el N° de resultados.
    """
    print("\n--- 6. Ordenar Países por Nombre ---")
    
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                            key=lambda pais: pais.get('nombre', '').lower(), 
                            reverse=orden_inverso)
    
    paises_a_mostrar = _limitar_resultados(paises_ordenados)
    
    mostrar_resultados(paises_a_mostrar)


# --- TAREA 7: ORDENAR PAÍSES POR POBLACIÓN (CON MEJORA) ---
def ordenar_por_poblacion(lista_paises):
    if not lista_paises:
        print("No hay paises cargados aún")
        return
    """
    Muestra la lista de países ordenada por población,
    permitiendo al usuario elegir el orden (ASC/DESC) y el N° de resultados.
    """
    print("\n--- 7. Ordenar Países por Población ---")
    
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                            key=lambda pais: pais.get('poblacion', 0), 
                            reverse=orden_inverso)
    
    paises_a_mostrar = _limitar_resultados(paises_ordenados)

    mostrar_resultados(paises_a_mostrar)


# --- TAREA 8: ORDENAR PAÍSES POR SUPERFICIE (CÓDIGO DE AMANDA ) ---

#Opción 8: Ordenar países por superficie.(Amanda)
    #Pide al usuario si quiere ascendente o descendente, valida la entrada
    #y muestra los resultados en pantalla.
#se dejo funcionando esta opcion, con el mismo formato de las opciones 1 y 2

def ordenar_por_superficie(paises):
    if not paises:
        print("No hay datos de países cargados.")
        return
    
    #Elegimos el orden

    while True:
        orden = input("¿Desea orden ascendente (A) o descendente (D)? ").strip().upper()
        if orden in ("A", "D"):
            break
        print("Opción inválida. Ingrese 'A' o 'D'.")

    #Ordena segun la eleccion.       

    reverse = (orden == "D")
    try:
        ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=reverse)
    except KeyError:
        print("Error: los datos de superficie no están correctamente definidos.")
        return
    
    # Encabezado
    print("\n°°°°°°°°°°°°°°°°° Países ordenados por superficie °°°°°°°°°°°°°°°°°  ")
    print(f"{'País':<45} | {'Superficie (Km²)':>18} | {'Continente/Región':<20}")
    print("-" * 80)
    
        # Filas
    for p in ordenados:
        nombre = p.get("nombre", "Desconocido")
        superficie = p.get("superficie", 0)
        region = p.get("region", "Desconocido")
        print(f"{nombre:<45} | {superficie:>18,.2f} | {region:<20}")
        

    #:<15 significa: - : → empieza el formato - < → alinear a la izquierda15 → ocupar 15 espacios de ancho. 
    # Esto hace que todos los nombres queden en columnas iguales.

    #:>12, .2f Esto formatea el número de superficie: - > → alinear a la derecha (útil para números)
    #12 → ocupa 12 espacios de ancho - , → muestra separadores de miles
    #.2f → muestra 2 decimales, en formato de número flotante (float)