import csv
import Cargar_API_y_CSV

def mostrar_estadisticas(paises):

    if not paises:
        print("No hay datos disponibles para mostrar estadísticas.")
        return

    try:
        total = len(paises)
        poblacion_total = sum(p["poblacion"] for p in paises)
        superficie_total = sum(p["superficie"] for p in paises)
        promedio_poblacion = poblacion_total / total
        promedio_superficie = superficie_total / total

        pais_mayor_pob = max(paises, key=lambda p: p["poblacion"])
        pais_menor_pob = min(paises, key=lambda p: p["poblacion"])
        pais_mayor_sup = max(paises, key=lambda p: p["superficie"])
        pais_menor_sup = min(paises, key=lambda p: p["superficie"])

    except (KeyError, ZeroDivisionError, ValueError) as e:
        print(f"Ocurrió un error al calcular las estadísticas: {e}")
        return

    # Encabezado
    print("\n°°°°°°°°°°°°°°°°°°°°Estadísticas Generales de Países°°°°°°°°°°°°°°°°°°°°")
    print("-" * 75)
    print(f"{'Indicador':<35} | {'Valor':>25}")
    print("-" * 75)

    # Totales y promedios
    print(f"{'Cantidad total de países':<35} | {total:>25}")
    print("-" * 75)
    print(f"{'Población total':<35} | {poblacion_total:>25,}")
    print("-" * 75)
    print(f"{'Población promedio':<35} | {promedio_poblacion:>25,.2f}")
    print("-" * 75)
    print(f"{'Superficie total (km²)':<35} | {superficie_total:>25,.2f}")
    print("-" * 75)
    print(f"{'Superficie promedio (km²)':<35} | {promedio_superficie:>25,.2f}")
    print("-" * 75)

    # Países destacados
    print(f"{'País con mayor población':<35} | {pais_mayor_pob['nombre']:<25}")
    print("-" * 75)
    print(f"{'→ Habitantes':<35} | {pais_mayor_pob['poblacion']:>25,}")
    print("-" * 75)
    print(f"{'País con menor población':<35} | {pais_menor_pob['nombre']:<25}")
    print("-" * 75)
    print(f"{'→ Habitantes':<35} | {pais_menor_pob['poblacion']:>25,}")
    print("-" * 75)
    print(f"{'País con mayor superficie':<35} | {pais_mayor_sup['nombre']:<25}")
    print("-" * 75)
    print(f"{'→ Superficie (km²)':<35} | {pais_mayor_sup['superficie']:>25,.2f}")
    print("-" * 75)
    print(f"{'País con menor superficie':<35} | {pais_menor_sup['nombre']:<25}")
    print("-" * 75)
    print(f"{'→ Superficie (km²)':<35} | {pais_menor_sup['superficie']:>25,.2f}")
    print("-" * 75)

