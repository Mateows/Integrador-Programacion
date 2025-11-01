import Cargar_API_y_CSV
import unicodedata
import csv




def normalizar_palabra(texto):
# Convierte texto a minúsculas y elimina acentos para búsquedas flexibles.
    texto = texto.lower()
    # Normaliza a 'NFKD' para separar caracteres base de diacríticos (acentos)
    texto = unicodedata.normalize('NFKD', texto)
    # Reconstruye el string omitiendo los caracteres diacríticos
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
    
    # ',d'   -> entero con separador de miles.
    # ',.2f' -> flotante con separador de miles y 2 decimales.
    print(f"\n{'País':<45} | {'Población':<15} | {'Capital':<25} |   {'Superficie (km²)':<20} |   {'Continente':<15} |  {'Moneda':<80}")
    print("-" * 150)

    for pais in resultados:
        # --- CORRECCIÓN DE CLAVES Y VALORES POR DEFECTO ---
        nombre = pais.get('nombre', 'N/A')
        poblacion = pais.get('poblacion', 0)
        capital = pais.get('capital', 'N/A')     
        superficie = pais.get('superficie', 0.0) 
        continente = pais.get('region', 'N/A')
        moneda = pais.get('moneda', 'N/A')
        lenguaje = pais.get("lenguaje", "N/A")       

        # --- FILA DE DATOS CON FORMATO ---
        # Aplicamos formato de números
        print(f"{nombre:<45} | {poblacion:<15,d} | {capital:<25} |   {superficie:<20,.2f} |   {continente:<15} |  {moneda:<80}")



#-------------------------------------------------------------------------------------------------

def buscar_pais(paises):
    if not paises:
        print("No hay paisea cargados aun")
        return
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
    mostrar_resultados(resultados)





##---------------------------FUNCIONAMIENTO DE LA OPCION PARA BUSCAR PAISES-----------------
def mostrar_paises(paises):
    if not paises:
        print("No hay paises cargados aun")
        return
    """
    Función para la Opción 1.
    Ahora solo llama a mostrar_resultados para reutilizar código.
    """
    print("\n--- Lista Completa de Países ---")
    mostrar_resultados(paises) # Reutilizamos la función corregida




def mostrar_idiomas(paises):
    if not paises:
        print("No hay paises cargados aun")
        return
    print(f"\n{'País':<50} | {"Lengua Natal":<55}")
    print("-" * 135)
    for pais in paises:

        nombre = pais.get('nombre', 'N/A')
        lenguaje = pais.get("lenguaje", "N/A")       

        # --- FILA DE DATOS CON FORMATO ---
        # Aplicamos formato de números
        print(f"{nombre:<50} | {lenguaje:<55}")

###########################################################OPCIONES 4,5 Y 6####################################################################################################################
def _mostrar_paises_lista(lista_paises):
    """
    Una función interna de ayuda para mostrar una lista de países de forma prolija.
    """
    if not lista_paises:
        print("No se encontraron países que coincidan con el criterio.")
        return

    # Imprime la cabecera (mantenemos f-string para alineación)
    print(f"\n{'País':<30} | {'Población':<15} | {'Superficie (km²)':<20}")
    print("-" * 70)
    
    # Imprime cada país
    for pais in lista_paises:
        nombre = pais.get('nombre', 'N/A')
        poblacion = pais.get('poblacion', 0)
        superficie = pais.get('superficie', 0)
        # Mantenemos f-string para formato de números y alineación
        print(f"{nombre:<30} | {poblacion:<15,d} | {superficie:<20,.2f}")


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

##MENÚ DE OPCIONES
def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Mostrar paises")
    print("2. Buscar pais por nombre")
    print("3. Filtrar países por continente")
    print("4. Filtrar países por población")
    print("5. Filtar países por superficie")
    print("6. Ordenar países por nombre")
    print("7. Ordenar países por población")
    print("8 Ordenar países por superficie")
    print("9. Mostrar estadísticas")
    print("10. Agregar/Eliminar/Editar país")
    print("11. Mostrar paises y sus idiomas")
    print("12. Salir")
