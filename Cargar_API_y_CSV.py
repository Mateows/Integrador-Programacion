import csv
import requests
import os



URL_API = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,languages,currencies,area"
ARCHIVO_CSV = "paises.csv"


# Función para descargar y guardar los datos en un CSV
def guardar_paises_csv():
    try:
        response = requests.get(URL_API) ##PARA PROBAR AL CSV SIN API, COMENTEN ESTE LINEA!!!!!!!
        #raise requests.RequestException("Probando sin API") #COMENTEN ESTA LINEA EN CASO DE QUE NO QUIERAN TRABAJAR CON LA LISTA VACIA
        if response.status_code == 200:
            countries = response.json()
            with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)
                # Escribe la fila de encabezado en el CSV. Se usan nombres en español y capitalizados por convención inicial.
                writer.writerow(["nombre", "capital", "region", "poblacion", "lenguaje", "moneda", "superficie"])
                # Itera sobre cada país recibido de la API
                for country in countries:
                    # Se usa .get(clave, valor_por_defecto) para evitar errores si un país no tiene cierto dato en la API.
                    nombre = country.get("name", {}).get("common", "Sin nombre")

                    capitales = country.get("capital", [])

                    capital = capitales[0] if capitales else "Sin capital"

                    region = country.get("region", "Sin región")

                    poblacion = country.get("population", "Desconocida")

                    lenguajes = list(country.get("languages", {}).values())
                
                    lenguaje = ", ".join(lenguajes) if lenguajes else "Sin dato"

                    monedas = country.get("currencies", {})
                    if monedas:
                        tipo_de_moneda = ", ".join(
                            [f"{moneda['name']} ({codigo})" for codigo, moneda in monedas.items()]
                        )
                    else:
                        tipo_de_moneda = "Sin dato"

                    superficie = country.get("area", "Sin dato")

                    writer.writerow([nombre, capital, region, poblacion, lenguaje, tipo_de_moneda, superficie])
            print(" DATOS CORRECTAMENTES GUARDADOS EN 'paises.csv'")
        else:
            print(" ERROR AL OBTENER LOS DATOS DE:", response.status_code)
    except Exception as e:
        print(f"ERROR AL DESCARGAR LOS DATOS DE LA API {e}")
        cargar_paises()




# Función para cargar los datos desde el CSV
def cargar_paises():
    guardar_paises_csv() ###---->COMENTEN ESTA LINEA PARA TRABAJAR SIN CSV, DESCOMENTENLA EN CASO CONTRARIO
    paises = []
    #####################################################################################
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['nombre', 'capital', 'region', 'poblacion', 'lenguaje', 'moneda', 'superficie'])
        print(f"Archivo '{ARCHIVO_CSV}' creado porque no existía.")
        return paises  # Lista vacía

    ######################################################################################
    try:
        # Intenta convertir población a entero y superficie a flotante.
    # Esto puede fallar si el CSV tiene datos corruptos o no numéricos.
    # Todas las claves se guardan en minúscula para consistencia en todo el programa.
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # usa exactamente los nombres de columnas del CSV
                pais = {
                    "nombre": fila.get("nombre", "N/A"),

                    "capital": fila.get("capital", "N/A"),

                    "region": fila.get("region", "N/A"),

                    "poblacion": int(fila.get("poblacion", 0)) if fila.get("poblacion", "").isdigit() else fila.get("poblacion", 0),

                    "lenguaje": fila.get("lenguaje", "N/A"),

                    "moneda": fila.get("moneda", "N/A"),
                    
                    "superficie": float(fila.get("superficie", 0)) if fila.get("superficie", "").replace('.', '', 1).isdigit() else fila.get("superficie", 0)
                }
                paises.append(pais)
    except FileNotFoundError: 
        print(f" ERROR: NO SE ENCONTRÓ EL ARCHIVO EN LA RUTA: '{ARCHIVO_CSV}'") #----> ERROR VISUAL
    except Exception as e:
        print(f"OCURRIÓ UN ERROR INESPERADO AL CARGAR EL ARCHIVO: {e}")
    return paises