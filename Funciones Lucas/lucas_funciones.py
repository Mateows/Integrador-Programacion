# --- Archivo: lucas_funciones.py (Versión Limpia, Robusta y Flexible) ---

# --- Función auxiliar de impresión (Limpia) ---
def _mostrar_paises_lista(lista_paises):
    """
    Una función interna de ayuda para mostrar una lista de países de forma prolija.
    """
    if not lista_paises:
        print("No se encontraron países que coincidan con el criterio.")
        return

    # Imprime la cabecera (mantenemos f-string para alineación)
    print(f"\n{'Nombre':<30} | {'Población':<15} | {'Superficie (km²)':<20}")
    print("-" * 70)
    
    # Imprime cada país
    for pais in lista_paises:
        nombre = pais.get('nombre', 'N/A')
        poblacion = pais.get('poblacion', 0)
        superficie = pais.get('superficie', 0)
        # Mantenemos f-string para formato de números y alineación
        print(f"{nombre:<30} | {poblacion:<15,d} | {superficie:<20,.2f}")

# --- MEJORA 2: FUNCIÓN HELPER REUTILIZABLE (Flexible) ---
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


# --- TAREA 4: FILTRAR POR SUPERFICIE (CON MEJORA 1: Robusta) ---
def filtrar_por_superficie(lista_paises):
    """
    Filtra la lista de países por superficie, con validaciones robustas
    de entrada de usuario.
    """
    print("\n--- 4. Filtrar Países por Superficie ---")
    try:
        # MEJORA 1: Validación de número positivo (con bucle)
        superficie_limite = -1
        while superficie_limite <= 0:
            try:
                entrada = input("Ingrese el valor de superficie (en km², debe ser > 0): ")
                if entrada == "":
                    print("Error: No ingresó ningún valor. Intente de nuevo.")
                    continue
                
                superficie_limite = float(entrada)
                
                if superficie_limite <= 0:
                    print("Error: La superficie debe ser un número positivo.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número.")
                superficie_limite = -1
        
        # MEJORA 1: Validación de criterio flexible (con bucle)
        criterio = ""
        while criterio not in ('>', '<'):
            criterio = input("¿Mostrar países 'mayor que' (>) o 'menor que' (<) este valor? ").strip().lower()
            if criterio in ("mayor", "mayor que"):
                criterio = ">"
            elif criterio in ("menor", "menor que"):
                criterio = "<"
            
            if criterio not in ('>', '<'):
                print("Error: Criterio no válido. Ingrese 'mayor', 'menor', '>' o '<'.")

        # --- Lógica de filtrado ---
        paises_filtrados = []
        if criterio == '>':
            for pais in lista_paises:
                if pais.get("superficie", 0) > superficie_limite:
                    paises_filtrados.append(pais)
        elif criterio == '<':
            for pais in lista_paises:
                if pais.get("superficie", 0) < superficie_limite:
                    paises_filtrados.append(pais)

        # Mantenemos f-string para mostrar el límite formateado
        print(f"\nPaíses con superficie {criterio} {superficie_limite:,.2f} km²:")
        _mostrar_paises_lista(paises_filtrados)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# --- TAREA 5: ORDENAR PAÍSES POR NOMBRE (CON MEJORA 2: Flexible) ---
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


# --- TAREA 6: ORDENAR PAÍSES POR POBLACIÓN (CON MEJORA 2: Flexible) ---
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