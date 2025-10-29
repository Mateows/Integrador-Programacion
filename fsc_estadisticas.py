import csv
import Cargar_API_y_CSV

 # Opción 7: Ordenar países por superficie.
#     #Pide al usuario si quiere ascendente o descendente, valida la entrada
#     #y muestra los resultados en pantalla.

# def ordenar_por_superficie(paises):
#     if not paises:
#         print("No hay datos de países cargados.")
#         return
    
#     #Elegimos el orden

#     while True:
#         orden = input("¿Desea orden ascendente (A) o descendente (D)? ").strip().upper()
#         if orden in ("A", "D"):
#             break
#         print("Opción inválida. Ingrese 'A' o 'D'.")

#     #Ordena segun la eleccion.       

#     reverse = (orden == "D")
#     try:
#         ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=reverse)
#     except KeyError:
#         print("Error: los datos de superficie no están correctamente definidos.")
#         return
    
#     print("\n--- Países ordenados por superficie ---")

#     for p in ordenados:
#         print(f"{p['nombre']:<15}  {p['superficie']:>12,.2f} km²  ({p['continente']})")

#     #:<15 significa: - : → empieza el formato - < → alinear a la izquierda15 → ocupar 15 espacios de ancho. 
#     # Esto hace que todos los nombres queden en columnas iguales.

#     #:>12, .2f Esto formatea el número de superficie: - > → alinear a la derecha (útil para números)
#     #12 → ocupa 12 espacios de ancho - , → muestra separadores de miles
#     #.2f → muestra 2 decimales, en formato de número flotante (float)

# def mostrar_estadisticas(paises):
#     # Opción 8: Muestra estadísticas generales de los países.
#     # Incluye totales, promedios y países con máximos/mínimos valores.

# ##Hacer un cambio en lo que se muestra por pantalla y hacerlo parecido o similar a las opciones 1/2 
#     if not paises:
#         print("No hay datos disponibles para mostrar estadísticas.")
#         return
#     try:
#         total = len(paises)
#         poblacion_total = sum(p["poblacion"] for p in paises)
#         superficie_total = sum(p["superficie"] for p in paises)
#         promedio_poblacion = poblacion_total / total
#         promedio_superficie = superficie_total / total

#         pais_mayor_pob = max(paises, key=lambda p: p["poblacion"])
#         pais_menor_pob = min(paises, key=lambda p: p["poblacion"])
#         pais_mayor_sup = max(paises, key=lambda p: p["superficie"])
#         pais_menor_sup = min(paises, key=lambda p: p["superficie"])

#     except(KeyError, ZeroDivisionError, ValueError) as e:
#         print(f"Ocurrió un error al calcular las estadísticas: {e}")
#         return
    
#     print("\n--- Estadísticas Generales de Países ---")
#     print(f"Cantidad total de países: {total}")
#     print(f"Población total: {poblacion_total:,}")
#     print(f"Población promedio: {promedio_poblacion:,.2f}")
#     print(f"Superficie total: {superficie_total:,.2f} km²")
#     print(f"Superficie promedio: {promedio_superficie:,.2f} km²")

#     print("\nPaís con mayor población:", pais_mayor_pob["nombre"], f"({pais_mayor_pob['poblacion']:,} habitantes)")
#     print("País con menor población:", pais_menor_pob["nombre"], f"({pais_menor_pob['poblacion']:,} habitantes)")
#     print("País con mayor superficie:", pais_mayor_sup["nombre"], f"({pais_mayor_sup['superficie']:,.2f} km²)")
#     print("País con menor superficie:", pais_menor_sup["nombre"], f"({pais_menor_sup['superficie']:,.2f} km²)")




