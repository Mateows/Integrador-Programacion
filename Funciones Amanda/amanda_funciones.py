# Comienzo de implementacion opciones 7, 8 y 9 del menu.

import csv  
CSV_HEADERS = ["nombre", "poblacion", "superficie", "continente"]  
CSV_RUTA_DEFAULT = "paises.csv"




def cargar_paises(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, newline="", encoding = "utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    #Convertimos los datos a los tipos adecuados y los almacenamos en un diccionario
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": float(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais) #<---- Aquí se almacenan todos los datos
                except ValueError:
                    print(f"Error: Datos inválidos en la fila: {fila}. Saltando fila.")
                except KeyError:
                    print(f"Error: Faltan columnas en el CSV. Fila: {fila}. Saltando fila.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")
        return [] # Devuelve lista vacía para que el programa no falle
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar el archivo: {e}")
        return []

    return paises





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
    
    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"Cantidad total de países: {total}")
    print(f"Población total: {poblacion_total:,}")
    print(f"Población promedio: {promedio_poblacion:,.2f}")
    print(f"Superficie total: {superficie_total:,.2f} km²")
    print(f"Superficie promedio: {promedio_superficie:,.2f} km²")

    print("\nPaís con mayor población:", pais_mayor_pob["nombre"], f"({pais_mayor_pob['poblacion']:,} habitantes)")
    print("País con menor población:", pais_menor_pob["nombre"], f"({pais_menor_pob['poblacion']:,} habitantes)")
    print("País con mayor superficie:", pais_mayor_sup["nombre"], f"({pais_mayor_sup['superficie']:,.2f} km²)")
    print("País con menor superficie:", pais_menor_sup["nombre"], f"({pais_menor_sup['superficie']:,.2f} km²)")

def agregar_o_eliminar_pais(paises, ruta_csv=CSV_RUTA_DEFAULT):

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
            escritor = csv.DictWriter(archivo, fieldnames=CSV_HEADERS)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print(f"Cambios guardados correctamente en '{ruta_csv}'.")
    except Exception as e:
        print(f"No se pudo guardar el archivo CSV: {e}")
 



