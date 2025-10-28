import Cargar_API_y_CSV
import unicodedata
import csv




def normalizar_palabra(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto




##Muestra los resultados encontradoss
def mostrar_resultados(resultados):
    """
    Función principal para mostrar una lista de países.
    Usa las claves correctas y formato de números.
    """
    # Chequeo si la lista de resultados está vacía
    if not resultados:
        print("\nNo se encontraron coincidencias.")
        return

    # --- CABECERA CORREGIDA ---
    # Usamos los anchos que ya probamos que funcionan
    print(f"\n{'Nombre':<45} | {'Población':<15} | {'Capital':<25} |   {'Superficie (km²)':<20} |   {'Continente':<15} |  {'Moneda':<80}")
    print("-" * 218)

    for pais in resultados:
        # --- CORRECCIÓN DE CLAVES Y VALORES POR DEFECTO ---
        nombre = pais.get('nombre', 'N/A')
        poblacion = pais.get('poblacion', 0)
        capital = pais.get('capital', 'N/A')     # CORREGIDO: Usar 'N/A', no 0
        superficie = pais.get('superficie', 0.0) # CORREGIDO: Usar 'superficie', no 'area'
        continente = pais.get('region', 'N/A')
        moneda = pais.get('moneda', 'N/A')       # CORREGIDO: Usar 'moneda', no 'currencies'

        # --- FILA DE DATOS CON FORMATO ---
        # Aplicamos formato de números
        print(f"{nombre:<45} | {poblacion:<15,d} | {capital:<25} |   {superficie:<20,.2f} |   {continente:<15} |  {moneda:<80}")






def buscar_pais(paises):
    #Buscamos el pais que el usuario ingrese
    pais_a_buscar = input("Ingrese el nombre del país a buscar: ").strip().lower()
    pais_a_buscar = normalizar_palabra(pais_a_buscar)
    #recorremos el archivo buscando coincidencias con el nombre ingresado y lo almacenamos en resultados
    resultados = []
    for pais in paises:
        #Buscamos si las primeras letras que se ingresen coinciden con algun pais
        nombre_normalizado = normalizar_palabra(pais["nombre"])
        if pais_a_buscar in nombre_normalizado:
            resultados.append(pais)
    return resultados





##---------------------------FUNCIONAMIENTO DE LA OPCION PARA BUSCAR PAISES-----------------
def mostrar_paises(paises):
    """
    Función para la Opción 1.
    Ahora solo llama a mostrar_resultados para reutilizar código.
    """
    print("\n--- Lista Completa de Países ---")
    mostrar_resultados(paises) # Reutilizamos la función corregida
#Opción 9: Permite agregar o eliminar países de la lista, con validaciones y guardado automático al CSV.
#Amanda



def agregar_o_eliminar_pais(paises, ruta_csv="paises.csv"):
    
    if not isinstance(paises, list):
        print("Error: la lista de países no es válida.")
        return

    while True:
        opcion = input("\n¿Desea (A)gregar, (E)liminar o (V)olver al menú? ").strip().upper()
        if opcion in ("A", "E", "V"):
            break
        print("Opción inválida. Ingrese 'A', 'E' o 'V'.")

    if opcion == "V":
        return  # vuelve al menú principal

    # --- AGREGAR PAÍS ---
    if opcion == "A":
        nombre = input("Ingrese el nombre del país: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        
    # Evitar duplicados
        for p in paises:
            if p["nombre"].lower() == nombre.lower():
                print("Ya existe un país con ese nombre.")
                return

    # Validar población
        try:
            poblacion = int(input("Ingrese la población (entero positivo): ").replace(",", ""))
            if poblacion < 0:
                raise ValueError #se usa para simular un error de valor cuando el dato ingresado es un número,
                                # pero es lógicamente incorrecto
        except ValueError:
            print("Error: población inválida.")
            return    
    # Validar superficie
        try:
            superficie = float(input("Ingrese la superficie (en km²): ").replace(",", "."))
            if superficie < 0:
                raise ValueError
        except ValueError:
            print("Error: superficie inválida.")
            return

        continente = input("Ingrese el continente: ").strip()
        if not continente:
            continente = "Desconocido"

        nuevo = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(nuevo)
        print(f"País '{nombre}' agregado correctamente.")

    # Guardar cambios
        _guardar_csv(paises, ruta_csv)

    # --- ELIMINAR PAÍS ---
    elif opcion == "E":
        nombre = input("Ingrese el nombre del país a eliminar: ").strip()
        if not nombre:
            print("Debe ingresar un nombre.")
            return

        encontrados = [p for p in paises if p["nombre"].lower() == nombre.lower()]
        if not encontrados:
            print("No se encontró el país.")
            return

        confirm = input(f"¿Confirma eliminar '{nombre}'? (S/N): ").strip().upper()
        if confirm != "S":
            print("Operación cancelada.")
            return
        
        paises[:] = [p for p in paises if p["nombre"].lower() != nombre.lower()]
        print(f"País '{nombre}' eliminado correctamente.")

    # Guardar cambios
        _guardar_csv(paises, ruta_csv)   




def _guardar_csv(paises, ruta_csv):

    #Guardamos la lista actualizada de países en el CSV.
    
    try:
        with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=paises)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print(f"Cambios guardados correctamente en '{ruta_csv}'.")
    except Exception as e:
        print(f"No se pudo guardar el archivo CSV: {e}")

#-----------------------------------------------------------------------------------------------

###########################################################OPCIONES 4,5 Y 6####################################################################################################################
def _mostrar_paises_lista(lista_paises):  #(Lucas)
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
        nombre = pais.get('Nombre', 'N/A')
        poblacion = pais.get('Población', 0)
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

#-----------------------------------------------------------------------------------------------

def mostrar_estadisticas(paises):
    # Opción 8: Muestra estadísticas generales de los países.
    # Incluye totales, promedios y países con máximos/mínimos valores.

##Hacer un cambio en lo que se muestra por pantalla y hacerlo parecido o similar a las opciones 1/2 
    if not paises:
        print("No hay datos disponibles para mostrar estadísticas.")
        return
    try:
        total = len(paises)
        poblacion_total = sum(p["poblacion"] for p in paises)
        superficie_total = sum(p["superficie"] for p in paises)
        promedio_poblacion = poblacion_total / total
        promedio_superficie = superficie_total / total

        pais_mayor_pob = max(paises, key=lambda p: p["poblacion"])
        pais_menor_pob = min(paises, key=lambda p: p["poblacion"])
        pais_mayor_sup = max(paises, key=lambda p: p["superficie"])
        pais_menor_sup = min(paises, key=lambda p: p["superficie"])

    except(KeyError, ZeroDivisionError, ValueError) as e:
        print(f"Ocurrió un error al calcular las estadísticas: {e}")
        return
    
    print("\n--- Estadísticas Generales de Países ---")
    print(f"Cantidad total de países: {total}")
    print(f"Población total: {poblacion_total:,}")
    print(f"Población promedio: {promedio_poblacion:,.2f}")
    print(f"Superficie total: {superficie_total:,.2f} km²")
    print(f"Superficie promedio: {promedio_superficie:,.2f} km²")

    print("\nPaís con mayor población:", pais_mayor_pob["nombre"], f"({pais_mayor_pob['poblacion']:,} habitantes)")
    print("País con menor población:", pais_menor_pob["nombre"], f"({pais_menor_pob['poblacion']:,} habitantes)")
    print("País con mayor superficie:", pais_mayor_sup["nombre"], f"({pais_mayor_sup['superficie']:,.2f} km²)")
    print("País con menor superficie:", pais_menor_sup["nombre"], f"({pais_menor_sup['superficie']:,.2f} km²)")













##MENÚ DE OPCIONES
def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Mostrar paises")
    print("2. Buscar pais por nombre")#Mateo
    print("3. Filtrar países por continente")#Mateo
    print("4. Filtrar países por población")#Mateo
    print("5. Filtar países por superficie")#Lucas
    print("6. Ordenar países por nombre")#Lucas
    print("7. Ordenar países por población")#Lucass
    print("8 Ordenar países por superficie")#Amanda
    print("9. Mostrar estadísticas")#Amanda
    print("10. Agregar/Eliminar país")#Amanda
    print("11. Salir")
