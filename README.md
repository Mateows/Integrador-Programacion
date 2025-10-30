# Trabajo Práctico Integrador - Programación 1

·Proyecto de consola para la gestión y consulta de datos mundiales de países, consumiendo una API pública (REST Countries) y aplicando lógicas de filtrado, ordenamiento y visualización de datos.

👨‍💻 Integrantes:
(Lucas Avila)

(Mateo Liendo)

(Amanda Pagano)

🚀 Características Principales:

Este proyecto no solo cumple con los requisitos básicos de consulta, sino que implementa mejoras significativas para la experiencia del usuario y la calidad del código:

Conexión a API Externa: El sistema consume datos en vivo desde la API https://restcountries.com/v3.1/all para obtener la información más actualizada.

Persistencia de Datos (Caché): Para optimizar el rendimiento y evitar llamadas innecesarias a la API, los datos se guardan localmente en un archivo paises.csv. El programa solo descarga los datos de la API si el archivo .csv no existe.

Diseño Modular: El código está separado en módulos (fsc_...py) según su responsabilidad (Carga de Datos, Búsqueda, Filtrado, Ordenamiento, Estadísticas), facilitando su mantenimiento.

Código Limpio (Principio DRY): Se implementó una función "experta" única (mostrar_resultados) que es reutilizada por todas las demás funciones para imprimir tablas, garantizando un formato consistente y evitando la duplicidad de código.

🌟 Funcionalidades Innovadoras:
Ranking "Top N" (Opciones 6 y 7): Al ordenar países por nombre o población, el sistema permite al usuario elegir si desea ver la lista completa o solo un "Top N" (por ejemplo, los 10 primeros), haciendo el análisis de datos más ágil.

Búsqueda Anidada (Opciones 4 y 5): Después de realizar un filtro (por población o superficie), el usuario puede realizar una segunda búsqueda por nombre dentro de esos resultados, permitiendo refinar las consultas de forma interactiva.

🛠️ Instalación, Actualización y Ejecución:
Para correr este proyecto en tu máquina local, seguí estos pasos.

1. Prerrequisitos
Tener Python 2 ó 3 instalado.

2. Dependencias
Este proyecto depende de la biblioteca (requests) para realizar las consultas a la API. Para instalarla, abrí tu terminal y ejecutá:

##  Instalación

**Para Python 2:**
```bash
pip install requests
```


**Para Python 3:**
```bash
pip3 install requests
```



---

##  En caso de que el comando `pip` no se reconozca

Ejecuta los siguientes comandos:

```bash
python -m ensurepip --upgrade
```

Luego instala `requests` con:

```bash
python -m pip install requests
```

---

##  Actualización de la biblioteca `requests`

**Para Python 2:**
```bash
pip install --upgrade requests
```


**Para Python 3:**
```bash
pip3 install --upgrade requests
```


---

##  Cómo saber qué versión de Python estás utilizando

Desde la terminal de Windows, ejecuta alguno de los siguientes comandos:

```bash
python --version
```

O, si no funciona el anterior:

```bash
python3 --version
```
---

  **Consejo:** asegurate de tener siempre actualizada tu versión de `pip` antes de instalar o actualizar bibliotecas.


3. Ejecución
Una vez instalada la dependencia, simplemente ejecutá el script principal desde tu terminal:

python integradorLimpio.py
Nota: La primera vez que lo ejecutes, el programa puede tardar unos segundos mientras descarga los datos de la API y crea el archivo paises.csv. Las ejecuciones siguientes serán instantáneas.

📖 Uso (Menú de Opciones)
El programa presenta un menú interactivo con las siguientes opciones:

1·Mostrar todos los países: Imprime la tabla completa con todos los datos.

2·Buscar país por nombre: Permite una búsqueda flexible (sin importar mayúsculas o acentos).

3·Filtrar por continente: Muestra solo países de un continente elegido.

4·Filtrar por población: Permite filtrar por un rango (mínimo y máximo) y luego buscar por nombre dentro de esos resultados.

5·Filtrar por superficie: Permite filtrar por un límite (mayor o menor que) y luego buscar por nombre dentro de esos resultados.

6·Ordenar por nombre: Ordena la lista (ASC/DESC) y permite mostrar solo el "Top N".

7·Ordenar por población: Ordena la lista (ASC/DESC) y permite mostrar solo el "Top N".

8·Ordenar por superficie: Ordena la lista (ASC/DESC).

9·Mostrar estadísticas: Calcula y muestra datos como promedios, máximos y mínimos.

10·Agregar/Eliminar país: Permite la gestión manual de la lista local.

11·Salir: Cierra el programa.

📁 Estructura del Proyecto
El código está organizado en los siguientes módulos para una clara separación de responsabilidades:

integradorLimpio.py:

Rol: Archivo principal (Entrypoint).

Contiene: El menú principal (match case) y el bucle de ejecución del programa.

Cargar_API_y_CSV.py:

Rol: Módulo de Datos.

Contiene: La lógica para conectarse a la API de restcountries.com (usando requests), descargar los datos, y guardarlos/cargarlos desde paises.csv. Estandariza las claves a minúsculas al cargar.

fsc_buscar_mostrar.py:

Rol: Módulo de Visualización y Búsqueda.

Contiene: La función experta mostrar_resultados() (Principio DRY), la función buscar_pais() y la normalizar_palabra() para búsquedas flexibles.

fsc_filtrado.py:

Rol: Módulo de Filtrado.

Contiene: Las funciones para las opciones 3, 4 y 5 (filtrar por continente, población y superficie), incluyendo la lógica de "búsqueda anidada".

fsc_ordenamiento.py:

Rol: Módulo de Ordenamiento.

Contiene: Las funciones para las opciones 6, 7 y 8 (ordenar por nombre, población y superficie), incluyendo la lógica de "Top N" (_limitar_resultados).

fsc_estadisticas.py:

Rol: Módulo de Cálculos.

Contiene: Las funciones para las opciones 9 y 10 (mostrar estadísticas y agregar/eliminar países).

paises.csv:

Rol: Base de datos / Caché.

Contiene: Los datos de los países descargados de la API, listos para ser leídos por el programa.
