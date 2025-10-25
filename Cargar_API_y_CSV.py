import csv
import requests



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
def cargar_paises():

    paises = []
    try:
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
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
        print(f"❌ Error: No se encontró el archivo en la ruta: {"archivo.csv"}")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al cargar el archivo: {e}")
    return paises