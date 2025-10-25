import csv
import requests
####################################################################CARGAMOS EL CSV############################################################################################################
#TRATAR DE MODULARIZAR ANTES QUE COMENZAR A CAMBIAR LOS NOMBRES DE LAS VARIABLES ASI SE HACE MAS COMODO CAMBIARLAS DESPUES
#MODIFICAR LAS FUNCIONES Y VARIABLES PARA QUE FUNCIONEN CORRECTAMENTE (FIJENSE BIEN COMO ESTÁN ESCRITAS EN LA OPCION FINAL (MOSTRAR PAISES Y COMO ESTA EN LA OPCION 2 FILTRAR POR NOMBRE))
#MODULARIZAR TODAS LAS FUNCIONES Y HACERLAS POR EJEMPLO (UNA FUNCION LLAMADA DATOS_PAISES, TIENE QUE TENER LA FUNCION "BUSCAR PAISES" Y "BUSCAR PAIS POR NOMBRE")
#CREAR UNA OPCION DE OS POR SI EL ARCHIVO NO EXISTE, YA QUE ESTAMOS CARGANDO UNA API, O SEA EL ARCHIVO SIEMPRE VA A EXISTIR, PERO EN CASO DE QUE NO EXISTA, QUE LO CREE
#SOLUCIONAR EL PROBLEMA (con ayuda de los profes si es posible y IA) COMO CARGAR LA SUPERFICIE DENTRO DEL CSV, YA QUE LA API NO LA TRAE, POR LO TANTO HAY QUE BUSCAR OTRA FORMA DE CONSEGUIRLA
#AGREGAR UNA NUEVA VARIABLE QUE SE LLAME "CAPITAL"
#MODIFICAR LAS FUNCIONES PARA QUE TRAIGAN LA CAPITAL Y LA MUESTREN EN PANTALLA (VA A QUEDAR VER LO DE LA SUPERFICIE, PARA LO QUE ACABO DE DECIR MIREN LA OPCION 1 (AL FINAL DEL TODO)





# Nueva URL actualizada de la API
# URL de la API
URL_API = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"
ARCHIVO_CSV = "paises.csv"

# Función para descargar y guardar los datos en un CSV
def guardar_paises_csv():
    response = requests.get(URL_API)
    if response.status_code == 200:
        countries = response.json()
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Capital", "Región", "Población"])
            for country in countries:
                nombre = country.get("name", {}).get("common", "Sin nombre")
                capitales = country.get("capital", [])
                capital = capitales[0] if capitales else "Sin capital"
                region = country.get("region", "Sin región")
                poblacion = country.get("population", "Desconocida")
                writer.writerow([nombre, capital, region, poblacion])
        print("✅ Datos guardados en 'paises.csv'")
    else:
        print("❌ Error al obtener los datos:", response.status_code)

# Función para cargar los datos desde el CSV
def cargar_paises(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "Nombre": fila["Nombre"],
                        "Capital": fila["Capital"],
                        "Región": fila["Región"],
                        "Población": int(fila["Población"])
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"⚠️ Error: Datos inválidos en la fila: {fila}. Saltando fila.")
                except KeyError:
                    print(f"⚠️ Error: Faltan columnas en el CSV. Fila: {fila}. Saltando fila.")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en la ruta: {ruta_archivo}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al cargar el archivo: {e}")
    return paises

guardar_paises_csv()





# def cargar_paises(ruta_archivo):
#     guardar_paises_csv()
#     paises = []
#     try:
#         with open(ruta_archivo, newline="", encoding = "utf-8") as archivo:
#             lector = csv.DictReader(archivo)
#             for fila in lector:
#                 try:
#                     #Convertimos los datos a los tipos adecuados y los almacenamos en un diccionario
#                     pais = {
#                         "Nombre": fila["nombre"],
#                         "Capital": fila["capital"],
#                         "Región": fila["region"],
#                         "Población": int(fila["poblacion"])
#                     }
#                     paises.append(pais) #<---- Aquí se almacenan todos los datos y con esto se puede trabajar en el codigo
#                 except ValueError:
#                     print(f"Error: Datos inválidos en la fila: {fila}. Saltando fila.")
#                 except KeyError:
#                     print(f"Error: Faltan columnas en el CSV. Fila: {fila}. Saltando fila.")
#     except FileNotFoundError:
#         print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")
#         return [] # Devuelve lista vacía para que el programa no falle
#     except Exception as e:
#         print(f"Ocurrió un error inesperado al cargar el archivo: {e}")
#         return []

#     return paises






# RUTA_ARCHIVO = "paises.csv"

# def cargar_paises(RUTA_ARCHIVO):
#     paises = []
#     try:
#         with open(RUTA_ARCHIVO, newline="", encoding = "utf-8") as archivo:
#             lector = csv.DictReader(archivo)
#             for fila in lector:
#                 try:
#                     #Convertimos los datos a los tipos adecuados y los almacenamos en un diccionario
#                     pais = {
#                         "nombre": fila["nombre"],
#                         "poblacion": int(fila["poblacion"]),
#                         "superficie": float(fila["superficie"]),
#                         "continente": fila["continente"]
#                     }
#                     paises.append(pais) #<---- Aquí se almacenan todos los datos y con esto se puede trabajar en el codigo
#                 except ValueError:
#                     print(f"Error: Datos inválidos en la fila: {fila}. Saltando fila.")
#                 except KeyError:
#                     print(f"Error: Faltan columnas en el CSV. Fila: {fila}. Saltando fila.")
#     except FileNotFoundError:
#         print(f"Error: No se encontró el archivo en la ruta: {RUTA_ARCHIVO}")
#         return [] # Devuelve lista vacía para que el programa no falle
#     except Exception as e:
#         print(f"Ocurrió un error inesperado al cargar el archivo: {e}")
#         return []

#     return paises
################################################################################################################################################################################

def normalizar_manual(texto):
    """
    Reemplaza caracteres acentuados por su versión sin tilde
    y convierte a minúsculas.
    """
    texto = texto.lower()
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("à", "a"), ("è", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u"),
        ("ä", "a"), ("ë", "e"), ("ï", "i"), ("ö", "o"), ("ü", "u"),
        ("ñ", "n")
    )
    for original, reemplazo in reemplazos:
        texto = texto.replace(original, reemplazo)
        return texto





#################################################################OPCIONES 1, 2 Y 3###############################################################################################################
#Se define la función para buscar un país por nombre.
def buscar_pais(paises):
    #Buscamos el pais que el usuario ingrese
    pais_a_buscar = input("Ingrese el nombre del país a buscar: ").strip().lower()
    normalizar_manual(pais_a_buscar)
    #recorremos el archivo buscando coincidencias con el nombre ingresado y lo almacenamos en resultados
    resultados = []
    for pais in paises:
        #Buscamos si las primeras letras que se ingresen coinciden con algun pais
        if pais_a_buscar in pais["Nombre"].lower():
            resultados.append(pais)

#pais in resultados
    if resultados:
    # Imprime la cabecera (mantenemos f-string para alineación)
        print(f"\n{'Nombre':<45} | {'Población':<15} | {'Superficie (km²)':<20}| {"Continente":<15}")
        print("-" * 90)
    # Imprime cada país
        for pais in resultados:
            nombre = pais.get('Nombre', 'N/A')
            poblacion = pais.get('Población', 0)
            superficie = pais.get('superficie', 0)
            continente = pais.get('Región', 'N/A')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<45} | {poblacion:<15,d} | {superficie:<20,.2f} | {continente:<15}")
    else:
        print("No hay coincidencias con el país ingresado")


#Funcion para filtrar paises por continente
def filtrar_por_continente(paises):
    #Buscamos el continente que el usuario ingrese
    continente = input("Ingrese el continente para filtar: ").strip().title()
    resultados = []
    #Recorremos el archivo, si lo que se ingreso es igual a algún continente, lo almacenamos en resultados
    for pais in paises:
        if pais["continente"] == continente:
            resultados.append(pais)

#En caso de que se guarde algun continente en resultados o no, mostramos el mensaje correspondiente
    if resultados:
        print(f"\n{'Nombre':<30} | {'Población':<15} | {'Superficie (km²)':<20}")
        print("-" * 80)
        for pais in resultados:
            nombre = pais.get('Nombre', 'N/A')
            poblacion = pais.get('Población', 0)
            superficie = pais.get('superficie', 0)
            continente = pais.get('Región', 'N/A')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<30} | {poblacion:<15,d} | {superficie:<20,.2f}")
    else:
        print("No hay coincidencias con el continente ingresado")



#Función para filtrar países por población
def filtrar_por_poblacion(paises):
    resultados = []
    #Insistimos en que el usuario ingrese valores válidos para la población mínima
    while True:
        try:
            poblacion_minima = int(input("Ingrese la población mínima: "))
            if poblacion_minima < 0:
                print("El número debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor. Ingrese un número entero positivo. ")

    #Insistimos en que el usuario ingrese valores válidos para la población máxima
    while True:
        try:
            poblacion_maxima = int(input("Ingrese la población máxima:"))
            if poblacion_maxima < poblacion_minima:
                print("ERROR. La población debe de ser mayor a la minima.")
                continue
            break
        except ValueError:
            print("ERROR. Por favor ingrese un número entero positivo.")
    ###Guardamos los valores en resultados, recorriendo una lista por comprensión para buscar las coincidencias
    resultados = [pais for pais in paises if poblacion_minima <= pais["Población"] <= poblacion_maxima]
    #Mostramos los resultados o el mensaje de error correspondiente
    if resultados:
        print(f"Paises con la poblacion entre {poblacion_minima} y {poblacion_maxima} de habitantes")
        #Esto es para mantener la alineación de las columnas, para que sea vea de forma prolija
        print(f"\n{'Nombre':<30} | {'Población':<15} | {'Superficie (km²)':<20}| {"Continente":<15}")
        print("-" * 90)
        for pais in resultados:
            nombre = pais.get('Nombre', 'N/A')
            poblacion = pais.get('Población', 0)
            superficie = pais.get('superficie', 0)
            continente = pais.get('Región', 'N/A')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<30} | {poblacion:<15,d} | {superficie:<20,.2f} | {continente:<15}")
    else:
        print("No hay coincidencias con las poblaciones ingresadas")
################################################################################################################################################################################



############################################################OPCIONES 4,5 Y 6####################################################################################################################
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
################################################################################################################################################################################







################################################################OPCIONES 7. 8 Y 9################################################################################################################
    # Opción 7: Ordenar países por superficie.
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

def agregar_o_eliminar_pais(paises, ruta_csv="paises.csv"):

    #Opción 9: Permite agregar o eliminar países de la lista, 
    # con validaciones y guardado automático al CSV.
    
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



def mostrar_paises(paises):
    # Imprime la cabecera (mantenemos f-string para alineación)
        print(f"\n{'Nombre':<45} | {'Población':<15} | {'Capital':<25} | {"Continente":<25}")
        print("-" * 110)
    # Imprime cada país
        for pais in paises:
            nombre = pais.get('Nombre', 'N/A')
            poblacion = pais.get('Población', 0)
            capital = pais.get('Capital', 0)
            continente = pais.get('Región', 'N/A')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<45} | {poblacion:<15,d} | {capital:<25} | {continente:<25}")






#########################################################MENU PRINCIPAL#######################################################################################################################
def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Mostrar paises")
    print("2. Buscar pais por nombre")#Mateo
    print("3. Filtrar países por continente")#Mateo
    print("4. Filtrar países por población")#Mateo
    print("5. Filtar países por superficie")#Lucas
    print("6. Ordenar países por nombre")#Lucas
    print("7. denar países por población")#Lucas
    print("8 Ordenar países por superficie")#Amanda
    print("9. Mostrar estadísticas")#Amanda
    print("10. Agregar/Eliminar país")#Amanda
    print("11. Salir")
################################################################################################################################################################################





########################################################MENÚ DE OPCIONES############################################################################################################
def ejecutar_programa():
    paises = cargar_paises(ARCHIVO_CSV)

    
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
                buscar_pais(paises)
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


