import Cargar_API_y_CSV
import csv



#Opción 9: Permite agregar o eliminar países de la lista, con validaciones y guardado automático al CSV.
def agregar_o_eliminar_pais(paises, ruta_csv="paises.csv"):
    if not isinstance(paises, list):
        print("Error: la lista de países no es válida.")
        return

    while True:
        opcion = input("\n¿Desea (A)gregar, (E)liminar o (V)olver al menú? ").strip().upper()
        if opcion in ("A", "E", "V"):
            break
        print("Opción inválida. Ingrese 'A', 'E' o 'V'.")

    # --- VOLVER AL MENÚ ---
    if opcion == "V":
        return

    # --- AGREGAR PAÍS ---
    if opcion == "A":
        nombre = input("Ingrese el nombre del país: ").strip().title()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        
        # Evitar duplicados
        for p in paises:
            if p["nombre"].lower() == nombre.lower():
                print("Ya existe un país con ese nombre.")
                return

        capital = input("Ingrese la capital: ").strip().title()
        if not capital:
            capital = "Desconocida"

        region = input("Ingrese la región o continente: ").strip().title()
        if not region:
            region = "Desconocida"

        lenguaje = input("Ingrese el lenguaje principal: ").strip().title()
        if not lenguaje:
            lenguaje = "Desconocido"

        moneda = input("Ingrese la moneda oficial: ").strip().title()
        if not moneda:
            moneda = "Desconocida"

        try:
            poblacion = int(input("Ingrese la población (entero positivo): ").replace(",", ""))
            if poblacion < 0:
                raise ValueError
        except ValueError:
            print("Error: población inválida.")
            return

        try:
            superficie = float(input("Ingrese la superficie (en km²): ").replace(",", "."))
            if superficie < 0:
                raise ValueError
        except ValueError:
            print("Error: superficie inválida.")
            return

        # Crear el nuevo registro
        nuevo = {
            "nombre": nombre,
            "capital": capital,
            "region": region,
            "poblacion": poblacion,
            "lenguaje": lenguaje,
            "moneda": moneda,
            "superficie": superficie
        }

        paises.append(nuevo)
        print(f"País '{nombre}' agregado correctamente.")

        # Guardar cambios
        _guardar_csv(paises, ruta_csv)

    # --- ELIMINAR PAÍS ---
    elif opcion == "E":
        if not paises:
            print("No hay paises cargados aun")
            return
        

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


# --- FUNCIÓN AUXILIAR ---
def _guardar_csv(paises, ruta_csv):
    """Guarda la lista actualizada de países en el archivo CSV."""
    if not paises:
        print("No hay datos para guardar.")
        return

    try:
        fieldnames = ["nombre", "capital", "region", "poblacion", "lenguaje", "moneda", "superficie"]
        with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print(f"Cambios guardados correctamente en '{ruta_csv}'.")
    except Exception as e:
        print(f"No se pudo guardar el archivo CSV: {e}")
