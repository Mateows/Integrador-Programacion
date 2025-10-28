import Cargar_API_y_CSV
from fsc_buscar_mostrar import _obtener_orden, _mostrar_paises_lista
from fsc_filtrado import _mostrar_paises_lista

# --- TAREA 6: ORDENAR PAÍSES POR NOMBRE (CON MEJORA 2: Flexible) ---(Lucas)

def ordenar_por_nombre(lista_paises):
    """
    Muestra la lista de países ordenada alfabéticamente por nombre,
    permitiendo al usuario elegir el orden (ASC/DESC).
    """
    print("\n--- 5. Ordenar Países por Nombre ---")
    
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                            key=lambda pais: pais.get('nombre', ''), 
                            reverse=orden_inverso)
    
    _mostrar_paises_lista(paises_ordenados)

#-----------------------------------------------------------------------------------------------

# # --- TAREA 7: ORDENAR PAÍSES POR POBLACIÓN (CON MEJORA 2: Flexible) ---(Lucas)

def ordenar_por_poblacion(lista_paises):
    """
    Muestra la lista de países ordenada por población,
    permitiendo al usuario elegir el orden (ASC/DESC).
    """
    print("\n--- 6. Ordenar Países por Población ---")
    
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                            key=lambda pais: pais.get('poblacion', 0), 
                            reverse=orden_inverso)
    
    _mostrar_paises_lista(paises_ordenados)

#------------------------------------------------------------------------------------------

#Opción 8: Ordenar países por superficie.
    #Pide al usuario si quiere ascendente o descendente, valida la entrada
    #y muestra los resultados en pantalla.

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
    
    print("\n--- Países ordenados por superficie ---")

    for p in ordenados:
        print(f"{p['nombre']:<15}  {p['superficie']:>12,.2f} km²  ({p['continente']})")

    #:<15 significa: - : → empieza el formato - < → alinear a la izquierda15 → ocupar 15 espacios de ancho. 
    # Esto hace que todos los nombres queden en columnas iguales.

    #:>12, .2f Esto formatea el número de superficie: - > → alinear a la derecha (útil para números)
    #12 → ocupa 12 espacios de ancho - , → muestra separadores de miles
    #.2f → muestra 2 decimales, en formato de número flotante (float)