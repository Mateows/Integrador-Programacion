import csv
import requests



URL_API = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,languages,currencies,area"
ARCHIVO_CSV = "paises.csv"

# Función para descargar y guardar los datos en un CSV
def guardar_paises_csv():
    response = requests.get(URL_API)
    if response.status_code == 200:
        countries = response.json()
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["nombre", "capital", "region", "poblacion", "lenguaje", "moneda", "superficie"])
            for country in countries:
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
                        "nombre": fila["nombre"],
                        "capital": fila["capital"],
                        "region": fila["region"],
                        "poblacion": fila["poblacion"],
                        "lenguaje": fila["lenguaje"],
                        "tipo_de_moneda": fila["tipo_de_moneda"],
                        "superficie": fila["superficie"]
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