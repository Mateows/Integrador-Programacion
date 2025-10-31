import csv

def agregar_editar_eliminar_pais(paises, ruta_csv="paises.csv"):
    if not isinstance(paises, list):
        print("Error: la lista de países no es válida.")
        return

    while True:
        opcion = input("\n¿Desea (AG)gregar, (EL)liminar, (ED)editar o (V)olver al menú? ").strip().upper()
        if opcion in ("AG", "EL", "ED", "V"):
            break
        print("Opción inválida. Ingrese 'AG', 'EL', 'ED' o 'V'.")

    if opcion == "V":
        return

    # --- AGREGAR PAÍSES ---
    if opcion == "AG":
        while True:
            try:
                cantidad = int(input("¿Cuántos países desea agregar? (Ingrese un numero entero positivo): "))
                if cantidad <0:
                    raise ValueError
                break
            except ValueError:
         
                print("Ingrese un número válido.")

        paises_agregados = []  # Lista para acumular los nombres de países agregados
       
        for _ in range(cantidad):
            # Validación de cada campo con buclles while
            while True:
                nombre = input("Ingrese el nombre del país: ").strip().title()
                if nombre and all(p["nombre"].lower() != nombre.lower() for p in paises):
                    break
                print("Nombre vacío o país ya existente.")

            capital = input("Ingrese la capital: ").strip().title() or "Desconocida"
            region = input("Ingrese la región o continente: ").strip().title() or "Desconocida"
            lenguaje = input("Ingrese el lenguaje principal: ").strip().title() or "Desconocido"
            moneda = input("Ingrese la moneda oficial: ").strip().title() or "Desconocida"

            while True:
                try:
                    poblacion = int(input("Ingrese la población (entero positivo): ").replace(",", ""))
                    if poblacion < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: debe ingresar un número entero positivo para población.")

            while True:
                try:
                    superficie = float(input("Ingrese la superficie (en km²): ").replace(",", "."))
                    if superficie < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido para superficie.")

            paises.append({
                "nombre": nombre,
                "capital": capital,
                "region": region,
                "poblacion": poblacion,
                "lenguaje": lenguaje,
                "moneda": moneda,
                "superficie": superficie
            })
            paises_agregados.append(nombre)
            print(f"\nSe agregaron correctamente los países: {', '.join(paises_agregados)}.")

        _guardar_csv(paises, ruta_csv)

    # --- ELIMINAR PAÍS ---
    elif opcion == "EL":
        if not paises:
            print("No hay países cargados aún.")
            return
        while True:
            nombre = input("Ingrese el nombre del país a eliminar: ").strip()
            if nombre:
                break
            print("Debe ingresar un nombre.")
        
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
        _guardar_csv(paises, ruta_csv)

    # --- EDITAR PAÍS ---
    elif opcion == "ED":
        if not paises:
            print("No hay países cargados aún.")
            return

        while True:
            nombre = input("Ingrese el nombre del país a editar: ").strip()
            if nombre:
                break
            print("Debe ingresar un nombre.")

        encontrados = [p for p in paises if p["nombre"].lower() == nombre.lower()]
        if not encontrados:
            print("No se encontró el país.")
            return

        pais = encontrados[0]
        print("Deje vacío para mantener el valor actual.")

        nuevo_nombre = input(f"Nombre ({pais['nombre']}): ").strip().title() or pais['nombre']
        capital = input(f"Capital ({pais['capital']}): ").strip().title() or pais['capital']
        region = input(f"Región ({pais['region']}): ").strip().title() or pais['region']
        lenguaje = input(f"Lenguaje ({pais['lenguaje']}): ").strip().title() or pais['lenguaje']
        moneda = input(f"Moneda ({pais['moneda']}): ").strip().title() or pais['moneda']

        while True:
            try:
                poblacion_input = input(f"Población ({pais['poblacion']}): ").replace(",", "")
                poblacion = int(poblacion_input) if poblacion_input else pais['poblacion']
                if poblacion < 0:
                    raise ValueError
                break
            except ValueError:
                print("Error: debe ingresar un número entero positivo para población.")

        while True:
            try:
                superficie_input = input(f"Superficie ({pais['superficie']} km²): ").replace(",", ".")
                superficie = float(superficie_input) if superficie_input else pais['superficie']
                if superficie < 0:
                    raise ValueError
                break
            except ValueError:
                print("Error: debe ingresar un número válido para superficie.")

        # Actualizar los datos
        pais.update({
            "nombre": nuevo_nombre,
            "capital": capital,
            "region": region,
            "lenguaje": lenguaje,
            "moneda": moneda,
            "poblacion": poblacion,
            "superficie": superficie
        })
        print(f"\nPaís '{nuevo_nombre}' editado correctamente.")
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
