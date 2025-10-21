# --- Archivo: lucas_funciones.py (Versión "para un 10") ---

# --- MEJORA 3: CÓDIGOS DE COLOR ---
class Color:
    HEADER = '\033[95m'   # Violeta
    BLUE = '\033[94m'     # Azul
    GREEN = '\033[92m'    # Verde
    YELLOW = '\033[93m'   # Amarillo
    RED = '\033[91m'      # Rojo
    ENDC = '\033[0m'      # Resetear color
    BOLD = '\033[1m'      # Negrita

# --- Función auxiliar de impresión (AHORA CON COLOR) ---
def _mostrar_paises_lista(lista_paises):
    """
    Una función interna de ayuda para mostrar una lista de países de forma prolija.
    """
    if not lista_paises:
        print(f"{Color.YELLOW}No se encontraron países que coincidan con el criterio.{Color.ENDC}")
        return

    # Imprime la cabecera con color
    print(f"{Color.BOLD}{Color.BLUE}{'Nombre':<30} | {'Población':<15} | {'Superficie (km²)':<20}{Color.ENDC}")
    print("-" * 70)
    
    # Imprime cada país
    for pais in lista_paises:
        nombre = pais.get('nombre', 'N/A')
        poblacion = pais.get('poblacion', 0)
        superficie = pais.get('superficie', 0)
        print(f"{nombre:<30} | {poblacion:<15,d} | {superficie:<20,.2f}")

# --- MEJORA 2: FUNCIÓN HELPER REUTILIZABLE ---
def _obtener_orden():
    """
    Función auxiliar para preguntar al usuario el orden (Asc/Desc).
    Devuelve el parámetro 'reverse' para la función sorted().
    """
    while True:
        orden = input(f"¿En qué orden? ({Color.GREEN}ASC{Color.ENDC} = Ascendente / {Color.YELLOW}DESC{Color.ENDC} = Descendente): ").strip().upper()
        if orden == "ASC":
            return False  # reverse=False
        elif orden == "DESC":
            return True   # reverse=True
        else:
            print(f"{Color.RED}Opción inválida. Escriba 'ASC' o 'DESC'.{Color.ENDC}")


# --- TAREA 4: FILTRAR POR SUPERFICIE (CON MEJORA 1: ROBUSTEZ) ---
def filtrar_por_superficie(lista_paises):
    """
    Filtra la lista de países por superficie, con validaciones robustas
    de entrada de usuario.
    """
    print(f"\n{Color.HEADER}{Color.BOLD}--- 4. Filtrar Países por Superficie ---{Color.ENDC}")
    try:
        # MEJORA 1: Validación de número positivo (AHORA DENTRO DE UN BUCLE)
        superficie_limite = -1
        while superficie_limite <= 0: # Bucle para seguir preguntando
            try:
                # Pedimos el número
                entrada = input("Ingrese el valor de superficie (en km², debe ser > 0): ")
                # Si está vacío, volvemos a preguntar
                if entrada == "":
                    print(f"{Color.RED}Error: No ingresó ningún valor. Intente de nuevo.{Color.ENDC}")
                    continue # Salta al inicio del while
                
                superficie_limite = float(entrada)
                
                # Si es negativo, mostramos error y el bucle repetirá
                if superficie_limite <= 0:
                    print(f"{Color.RED}Error: La superficie debe ser un número positivo.{Color.ENDC}")
            except ValueError:
                # Si pone "hola", mostramos error y el bucle repetirá
                print(f"{Color.RED}Error: Entrada inválida. Por favor, ingrese un número.{Color.ENDC}")
                superficie_limite = -1 # Reseteamos por si acaso
        
        # MEJORA 1: Validación de criterio flexible
        criterio = ""
        while criterio not in ('>', '<'):
            criterio = input(f"¿Mostrar países 'mayor que' ({Color.GREEN}>{Color.ENDC}) o 'menor que' ({Color.YELLOW}<{Color.ENDC}) este valor? ").strip().lower()
            if criterio in ("mayor", "mayor que"):
                criterio = ">"
            elif criterio in ("menor", "menor que"):
                criterio = "<"
            
            if criterio not in ('>', '<'):
                print(f"{Color.RED}Error: Criterio no válido. Ingrese 'mayor', 'menor', '>' o '<'.{Color.ENDC}")

        # --- El resto del código de filtrado (sin cambios) ---
        paises_filtrados = []
        if criterio == '>':
            for pais in lista_paises:
                if pais.get("superficie", 0) > superficie_limite:
                    paises_filtrados.append(pais)
        elif criterio == '<':
            for pais in lista_paises:
                if pais.get("superficie", 0) < superficie_limite:
                    paises_filtrados.append(pais)

        print(f"\n{Color.BOLD}Países con superficie {criterio} {superficie_limite:,.2f} km²:{Color.ENDC}")
        _mostrar_paises_lista(paises_filtrados)

    except Exception as e:
        print(f"{Color.RED}Ocurrió un error inesperado: {e}{Color.ENDC}")


# --- TAREA 5: ORDENAR PAÍSES POR NOMBRE (CON MEJORA 2: FLEXIBILIDAD) ---
def ordenar_por_nombre(lista_paises):
    """
    Muestra la lista de países ordenada alfabéticamente por nombre,
    permitiendo al usuario elegir el orden (ASC/DESC).
    """
    print(f"\n{Color.HEADER}{Color.BOLD}--- 5. Ordenar Países por Nombre ---{Color.ENDC}")
    
    # Usamos la función helper para preguntar el orden
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                              key=lambda pais: pais.get('nombre', ''), 
                              reverse=orden_inverso)
    
    _mostrar_paises_lista(paises_ordenados)


# --- TAREA 6: ORDENAR PAÍSES POR POBLACIÓN (CON MEJORA 2: FLEXIBILIDAD) ---
def ordenar_por_poblacion(lista_paises):
    """
    Muestra la lista de países ordenada por población,
    permitiendo al usuario elegir el orden (ASC/DESC).
    """
    print(f"\n{Color.HEADER}{Color.BOLD}--- 6. Ordenar Países por Población ---{Color.ENDC}")
    
    # Reutilizamos la función helper
    orden_inverso = _obtener_orden()
    
    paises_ordenados = sorted(lista_paises, 
                              key=lambda pais: pais.get('poblacion', 0), 
                              reverse=orden_inverso)
    
    _mostrar_paises_lista(paises_ordenados)