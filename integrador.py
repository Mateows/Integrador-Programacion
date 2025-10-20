import csv
def cargar_paises(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, newline="", encoding = "utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": float(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error en conversión de tipos en fila: {fila}")
                    
    except FileNotFoundError:
        print(f"Archivo no encontrado")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return paises