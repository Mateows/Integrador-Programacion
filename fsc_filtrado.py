# #Funcion para filtrar paises por continente
def filtrar_por_continente(paises):
    #Buscamos el continente que el usuario ingrese
    continente = input("Ingrese el continente para filtar: ").strip().title()
    resultados = []
    #Recorremos el archivo, si lo que se ingreso es igual a algún continente, lo almacenamos en resultados
    for pais in paises:
        if pais["continente"] == continente:
            resultados.append(pais)

# #En caso de que se guarde algun continente en resultados o no, mostramos el mensaje correspondiente
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

#-----------------------------------------------------------------------------------------

# #Función para filtrar países por población
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


# # --- TAREA 4: FILTRAR POR SUPERFICIE (CON MEJORA 1: Robusta) --- (Lucas)
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

#--------------------------------------------------------------------------------------------------------------------------