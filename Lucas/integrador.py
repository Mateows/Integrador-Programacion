import csv

from Lucas.lucas_funciones import filtrar_por_superficie, ordenar_por_nombre, ordenar_por_poblacion

# Carga los datos de países desde un archivo CSV y los devuelve como una lista de diccionarios.

#LEER ATENTAMENTE; El archivo tiene que tener MÁS datos, ahora bien. ¿Que hace falta por hacer?
#1-Fijense que no pude hacer y intenten hacerlo ustedes!
#2-Falta modularizar el código, es decir, separar las funciones en otros archivos .py para importar directamente al archivo principal y que quede solo una linea
#3-Corregir los errores que puedan generarse, y hacer uso del try/except, fijense que como tenemos el archivo ya creado desde un principio no hace falta validar tanto el archivo dsp
#4.Comentar el codigo para que se entienda que estamos haciendo
#5- 

#Cargamos el archivo CSV "paises.csv" para importar los datos de los países y asi trabajar en el codigo
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



# Muestra el menú principal al usuario.
def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Buscar pais por nombre")#Mateo
    print("2. Filtrar países por continente")#Mateo
    print("3. Filtrar países por población")#Mateo
    print("4. Filtar países por superficie")#Lucas
    print("5. Ordenar países por nombre")#Lucas
    print("6. Ordenar países por población")#Lucas
    print("7. Ordenar países por superficie")#Amanda
    print("8. Mostrar estadísticas")#Amanda
    print("9. Agregar/Eliminar país")#Amanda
    print("10. Salir")


#Main loop del programa
def ejecutar_programa():
    paises = cargar_paises("paises.csv")
    
    # Si no se cargaron países (p.ej. archivo no encontrado), no continuamos.
    if not paises:
        print("No se pudieron cargar los datos de países. Saliendo del programa.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                # buscar_pais(paises) # <--- Función de Mateo
                print("Opción 1 (Mateo) no implementada en este script.")
            case "2":
                # filtrar_por_continente(paises) # <--- Función de Mateo
                print("Opción 2 (Mateo) no implementada en este script.")
            case "3":
                # filtrar_por_poblacion(paises) # <--- Función de Mateo
                print("Opción 3 (Mateo) no implementada en este script.")
            
            ### LÍNEAS CORREGIDAS ###
            # Aquí llamamos a TUS funciones importadas
            case "4":
                filtrar_por_superficie(paises)
            case "5":
                ordenar_por_nombre(paises)
            case "6":
                ordenar_por_poblacion(paises)
            
            case "7":
                # pass # <--- Función de Amanda
                print("Opción 7 (Amanda) no implementada en este script.")
            case "8":
                # pass # <--- Función de Amanda
                print("Opción 8 (Amanda) no implementada en este script.")
            case "9":
                # pass # <--- Función de Amanda
                print("Opción 9 (Amanda) no implementada en este script.")
            case "10":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

#Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_programa()