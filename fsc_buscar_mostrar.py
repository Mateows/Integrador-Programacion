import Cargar_API_y_CSV
import unicodedata




def normalizar_palabra(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto




##Muestra los resultados encontradoss
def mostrar_resultados(resultados):
    if resultados:
        print(f"\n{'Nombre':<45} | {'Población':<15} | {'Capital':<25} |  | {'Superficie':<25} |   {'Continente':<25} |   {'Moneda':<25} |")
        print("-" * 110)
        for pais in resultados:
            nombre = pais.get('nombre', 'N/A')
            poblacion = pais.get('poblacion', 0)
            capital = pais.get('capital', 0)
            superficie = pais.get("area")
            continente = pais.get('region', 'N/A')
            lenguaje = pais.get("lenguages")
            moneda = pais.get("currencies")

            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<45} | {poblacion:<15,d} | {capital:<25} | {superficie:<25}| {continente:<25} |   {moneda:<25}")
    else:
        print("No se encontraron coincidencias.")

def buscar_pais(paises):
    #Buscamos el pais que el usuario ingrese
    pais_a_buscar = input("Ingrese el nombre del país a buscar: ").strip().lower()
    pais_a_buscar = normalizar_palabra(pais_a_buscar)
    #recorremos el archivo buscando coincidencias con el nombre ingresado y lo almacenamos en resultados
    resultados = []
    for pais in paises:
        #Buscamos si las primeras letras que se ingresen coinciden con algun pais
        nombre_normalizado = normalizar_palabra(pais["nombre"])
        if pais_a_buscar in nombre_normalizado:
            resultados.append(pais)
    return resultados




##---------------------------FUNCIONAMIENTO DE LA OPCION PARA BUSCAR PAISES-----------------
def mostrar_paises(paises):
    # Imprime la cabecera (mantenemos f-string para alineación)
        print(f"\n{'Nombre':<45} | {'Población':<15} | {'Capital':<25} |   {'Superficie':<15} |   {'Continente':<15} |  {'Moneda':<35}")
        print("-" * 180)
    # Imprime cada país
        for pais in paises:
            nombre = pais.get('nombre', 'N/A')
            poblacion = pais.get('poblacion', '0')
            capital = pais.get('capital', 'N/A')
            superficie = pais.get('superficie', '0')
            continente = pais.get('region', 'N/A')
            moneda = pais.get('moneda', '0')
            # Mantenemos f-string para formato de números y alineación
            print(f"{nombre:<45} | {poblacion:<15} | {capital:<25} |   {superficie:<15} |   {continente:<15} |  {moneda:<35}")




##MENÚ DE OPCIONES
def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Mostrar paises")
    print("2. Buscar pais por nombre")#Mateo
    print("3. Filtrar países por continente")#Mateo
    print("4. Filtrar países por población")#Mateo
    print("5. Filtar países por superficie")#Lucas
    print("6. Ordenar países por nombre")#Lucas
    print("7. Ordenar países por población")#Lucass
    print("8 Ordenar países por superficie")#Amanda
    print("9. Mostrar estadísticas")#Amanda
    print("10. Agregar/Eliminar país")#Amanda
    print("11. Salir")
