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
                cantidad = int(input("¿Cuántos países desea agregar? (Ingrese un número entero positivo): "))
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número válido.")

        paises_agregados = []

        for _ in range(cantidad):

            # ===== VALIDACIÓN DE NOMBRE =====
            while True:
                nombre = input("Ingrese el nombre del país: ").strip().title()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                if any(char.isdigit() for char in nombre):
                    print("El nombre del país no debe contener números. Intente nuevamente.")
                    continue
                if any(p["nombre"].lower() == nombre.lower() for p in paises):
                    print("Ese país ya existe. Ingrese otro nombre.")
                    continue
                break

            # ===== VALIDACIÓN DE CAPITAL =====
            while True:
                capital = input("Ingrese la capital: ").strip().title() or "Desconocida"
                if any(char.isdigit() for char in capital):
                    print("La capital no puede contener números. Intente nuevamente.")
                else:
                    break

            # ===== VALIDACIÓN DE REGIÓN =====
            while True:
                region = input("Ingrese la región o continente: ").strip().title() or "Desconocida"
                if any(char.isdigit() for char in region):
                    print("La región no puede contener números. Intente nuevamente.")
                else:
                    break

            # ===== VALIDACIÓN DE LENGUAJE =====
            while True:
                lenguaje = input("Ingrese el lenguaje principal: ").strip().title() or "Desconocido"
                if any(char.isdigit() for char in lenguaje):
                    print("El lenguaje no puede contener números. Intente nuevamente.")
                else:
                    break

            # ===== VALIDACIÓN DE MONEDA =====
            while True:
                moneda = input("Ingrese la moneda oficial: ").strip().title() or "Desconocida"
                if any(char.isdigit() for char in moneda):
                    print("La moneda no puede contener números. Intente nuevamente.")
                else:
                    break

            # ===== VALIDACIÓN DE POBLACIÓN =====
            while True:
                try:
                    poblacion = int(input("Ingrese la población (entero positivo): ").replace(",", ""))
                    if poblacion < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: debe ingresar un número entero positivo para población.")

            # ===== VALIDACIÓN DE SUPERFICIE =====
            while True:
                try:
                    superficie = float(input("Ingrese la superficie (en km²): ").replace(",", "."))
                    if superficie < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido para superficie.")

            # Agregar país a la lista
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

        def validar_texto(campo, valor_actual):
            """Valida que un campo de texto no contenga números"""
            while True:
                valor = input(f"{campo} ({valor_actual}): ").strip().title()
                if not valor:
                    return valor_actual
                if any(char.isdigit() for char in valor):
                    print(f"El {campo.lower()} no puede contener números. Intente nuevamente.")
                else:
                    return valor

        nuevo_nombre = validar_texto("Nombre", pais["nombre"])
        capital = validar_texto("Capital", pais["capital"])
        region = validar_texto("Región", pais["region"])
        lenguaje = validar_texto("Lenguaje", pais["lenguaje"])
        moneda = validar_texto("Moneda", pais["moneda"])

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


