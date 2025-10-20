import csv
# Carga los datos de países desde un archivo CSV y los devuelve como una lista de diccionarios.

#LEER ATENTAMENTE; El archivo tiene que tener MÁS datos, ahora bien. ¿Que hace falta por hacer?
#1-Fijense que no pude hacer y intenten hacerlo ustedes!
#2-Falta modularizar el código, es decir, separar las funciones en otros archivos .py para importar directamente al archivo principal y que quede solo una linea
#3-Corregir los errores que puedan generarse, y hacer uso del try/except, fijense que como tenemos el archivo ya creado desde un principio no hace falta validar tanto el archivo dsp
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
#Manejo de errores que podrian surgir al abrir el archivo
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
        print("Resultados encontrados:")
        for pais in resultados:
            print(f"{pais["nombre"]}| Población: {pais["poblacion"]} habitantes | Superficie: {pais["superficie"]} km2| Continente: {pais["continente"]}")
    else:
        print("No hay coincidencias con el país ingresado")


#Funcion para filtrar paises por continente
def filtrar_por_continente(paises):
    #Buscamos el continente que el usuario ingrese
    continente = input("Ingrese el contienen para filtar: ").strip().title()
    resultados = []
    #Recorremos el archivo, si lo que se ingreso es igual a algún continente, lo almacenamos en resultados
    for pais in paises:
        if pais["continente"] == continente:
            resultados.append(pais)

#En caso de que se guarde algun continente en resultados o no, mostramos el mensaje correspondiente
    if resultados:
        print(f"Paises en el continente {continente}")
        for pais in resultados:
            print(f"{pais["nombre"]}| Población: {pais["poblacion"]} habitantes | Superficie: {pais["superficie"]} km2| Continente: {pais["continente"]}")
    else:
        print("No hay coincidencias con el continente ingresado")



#Función para filtrar países por población
def filtrar_por_poblacion(paises):
    resultados = []
    #Insistimos en que el usuario ingrese valores válidos para la población mínima
    while True:
        try:
            poblacion_minima = int(input("Ingrese la población mínima: ")).strip()
            if poblacion_minima < 0:
                print("El número debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor. Ingrese un número entero positivo. ")

    #Insistimos en que el usuario ingrese valores válidos para la población máxima
    while True:
        try:
            poblacion_maxima = int(input("Ingrese la población máxima:")).strip()
            if poblacion_maxima < poblacion_minima:
                print("ERROR. La población debe de ser mayor a la minima.")
                continue
            break
        except ValueError:
            print("ERROR. Por favor ingrese un número entero positivo.")
    ###Guardamos los valores en resultados y reccoremos un bucle
    resultados = [pais for pais in paises if poblacion_minima <= pais["poblacion"] <= poblacion_maxima]
    #Mostramos los resultados o el mensaje de error correspondiente
    if resultados:
        print(f"Paises con la poblacion entre {poblacion_minima} y {poblacion_maxima}")
        for pais in resultados:
            print(f"{pais["nombre"]}| Población: {pais["poblacion"]} habitantes | Superficie: {pais["superficie"]} km2| Continente: {pais["continente"]}")
    else:
        print("No hay coincidencias con las poblaciones ingresadas")








# Muestra el menú principal al usuario.
def mostrar_menu():
    print("------MENÚ PRINCIPAL-------")
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
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                buscar_pais(paises)
            case "2":
                filtrar_por_continente(paises)
            case "3":
                filtrar_por_poblacion(paises)
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
                pass
            case "10":
                print("Saliendo del programa. . .")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


ejecutar_programa()

