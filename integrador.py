import csv
# Carga los datos de países desde un archivo CSV y los devuelve como una lista de diccionarios.

#LEER ATENTAMENTE; El archivo tiene que tener MÁS datos, ahora bien. ¿Que hace falta por hacer?
#1-Fijense que no pude hacer y intenten hacerlo ustedes!
#2-Falta modularizar el código, es decir, separar las funciones en otro archivo llamado "funciones.py" y luego importarlas aquí.
#3-Corregir los errores que se puedan generar o que ustedes consideren que pueden generarse.
#4-Comentar el codigo para que se entienda que estamos haciendo
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
                    paises.append(pais) #<---- Aquí se almacenan todos los datos para luego ser usados
                except ValueError:
                    print(f"Error en conversión de tipos en fila: {fila}")

    except FileNotFoundError:
        print(f"Archivo no encontrado")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return paises




#Se define la función para buscar un país por nombre.
def buscar_pais(paises):
    #Buscamos el pais que el usuario ingrese
    pais_a_buscar = input("Ingrese el nombre del país a buscar: ").strip().title()
    #recorremos el archivo buscando coincidencias con el nombre ingresado y lo almacenamos en resultados
    resultados = []
    for pais in paises:
        #Buscamos si las primeras letras que se ingresen coinciden con algun pais
        if pais_a_buscar in pais["nombre"]:
            resultados.append(pais)


    if resultados:
        print("Resultados encontrados. . .")
        for pais in resultados:
            print(f"{pais["nombre"]}| Población: {pais["poblacion"]}| Superficie: {pais["superficie"]}| Continente: {pais["continente"]}")
    else:
        print("No hay coincidencias con el país ingresado")

def filtrar_por_continente(paises):









# Muestra el menú principal al usuario.
def mostrar_menu():
    print("------MENÚ PRINCIPAL-------")
    print("1. Buscar pais por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por población")
    print("4. Filtar países por superficie")
    print("5. Ordenar países por nombre")
    print("6. Ordenar países por población")
    print("7. Ordenar países por superficie")
    print("8. Mostrar estadísticas")
    print("9. Salir")





#Main loop del programa
def ejecutar_programa():
    paises = cargar_paises("paises.csv")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                buscar_pais(paises)
            case "2":
                filtar_por_continente(paises)
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                print("Saliendo del programa. . .")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


ejecutar_programa()

