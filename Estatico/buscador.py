"""
Código que sirve como buscador para consultar
y buscar información almacenada en el cache.

Creado por Erick Luis Juárez
"""
import dataset
import cache
from unicodedata import normalize
import difflib

def corregir_nombre_ciudad(nombre_ciudad_usuario):
    """
    Corrige el nombre de la ciudad proporcionado por el usuario.
    Utiliza el diccionario de ciudades para encontrar una coincidencia.

    Args:
        nombre_ciudad_usuario (str): Nombre de la ciudad ingresado por el usuario.

    Returns:
        tuple: Código IATA corregido si se encuentra una coincidencia, 
               sugerencia de ciudad corregida si el nombre es similar pero incorrecto.
    """
    diccionario_ciudades = dataset.crear_diccionario_ciudades()
    nombre_ciudad_usuario = nombre_ciudad_usuario.lower()
    nombre_ciudad_usuario = normalize('NFKD', nombre_ciudad_usuario).encode('ASCII', 'ignore').decode('ASCII')
    nombres_ciudades = [normalize('NFKD', ciudad.lower()).encode('ASCII', 'ignore').decode('ASCII') for ciudad in diccionario_ciudades.values()]
    coincidencias = difflib.get_close_matches(nombre_ciudad_usuario, nombres_ciudades, n=1, cutoff=0.6)

    if coincidencias:
        ciudad_corregida = coincidencias[0]

        for iata, ciudad in diccionario_ciudades.items():
            if normalize('NFKD', ciudad.lower()).encode('ASCII', 'ignore').decode('ASCII') == ciudad_corregida:
                if nombre_ciudad_usuario != ciudad_corregida:
                    return iata, f"Tal vez quisiste buscar: {ciudad}"
                return iata, None

    return None, "No se encontró ninguna coincidencia cercana."


def corregir_codigo_iata(iata_usuario):
    """
    Corrige el código IATA proporcionado por el usuario si es incorrecto o no existe.
    Verifica que el código tenga exactamente 3 caracteres.

    Args:
        iata_usuario (str): Código IATA ingresado por el usuario.

    Returns:
        tuple: Código IATA corregido si se encuentra una coincidencia,
               sugerencia del código corregido si es similar pero incorrecto.
    """
    if len(iata_usuario) != 3:
        return None, "El código IATA debe tener exactamente 3 caracteres."

    diccionario_ciudades = dataset.crear_diccionario_ciudades()
    iata_usuario = iata_usuario.upper()

    if iata_usuario in diccionario_ciudades:
        return iata_usuario, None

    codigos_iata = diccionario_ciudades.keys()
    coincidencias = difflib.get_close_matches(iata_usuario, codigos_iata, n=1, cutoff=0.6)

    if coincidencias:
        codigo_corregido = coincidencias[0]
        return codigo_corregido, f"Tal vez quisiste ingresar el código IATA: {codigo_corregido}"

    return None, "No se encontró ninguna coincidencia cercana para el código IATA."


def obtener_datos_climaticos_por_ciudad(nombre_ciudad_usuario, datos):
    """
    Obtiene los datos climáticos para una ciudad proporcionada por el usuario.

    Args:
        nombre_ciudad_usuario (str): Nombre de la ciudad ingresado por el usuario.
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        tuple: (Código IATA corregido, datos climáticos) si se encuentran coordenadas,
               (None, None) en caso contrario.
    """
    iata_corregido, sugerencia = corregir_nombre_ciudad(nombre_ciudad_usuario)
    if not iata_corregido:
        print(sugerencia)
        return None, None
    coordenadas = dataset.obtener_coordenadas(datos, iata_corregido)
    if coordenadas:
        lat, lon = coordenadas
        ciudad = dataset.obtener_nombre_ciudad_por_iata(iata_corregido)
        if ciudad:
            url = cache.construir_url(ciudad)
            json_data = cache.obtener_datos_desde_url(url)
            datos_climaticos = cache.extraer_informacion_relevante(json_data)
            return iata_corregido, datos_climaticos
    return None, None


def obtener_datos_climaticos_por_iata(iata_usuario, datos):
    """
    Obtiene los datos climáticos para una ciudad proporcionada por el código IATA.

    Args:
        iata_usuario (str): Código IATA ingresado por el usuario.
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        tuple: (Código IATA corregido, datos climáticos) si se encuentran coordenadas,
               (None, None) en caso contrario.
    """
    iata_corregido, sugerencia = corregir_codigo_iata(iata_usuario)
    if not iata_corregido:
        print(sugerencia)
        return None, None
    coordenadas = dataset.obtener_coordenadas(datos, iata_corregido)
    if coordenadas:
        lat, lon = coordenadas
        ciudad = dataset.obtener_nombre_ciudad_por_iata(iata_corregido)
        if ciudad:
            url = cache.construir_url(ciudad)
            json_data = cache.obtener_datos_desde_url(url)
            datos_climaticos = cache.extraer_informacion_relevante(json_data)
            return iata_corregido, datos_climaticos
    return None, None

if __name__ == "__main__":
    datos = dataset.cargar_datos_de_archivo()

    opcion = input("¿Deseas buscar por nombre de ciudad o por código IATA? (ciudad/iata): ").strip().lower()

    if opcion == 'ciudad':
        nombre_ciudad_usuario = input("Introduce el nombre de la ciudad: ")
        iata_corregido, datos_climaticos = obtener_datos_climaticos_por_ciudad(nombre_ciudad_usuario, datos)

        if iata_corregido:
            print(f"Código IATA: {iata_corregido}")
            print(f"Datos climáticos: {datos_climaticos}")
        else:
            print("No se pudieron obtener los datos climáticos.")
    
    elif opcion == 'iata':
        iata_usuario = input("Introduce el código IATA: ").strip().upper()
        iata_corregido, datos_climaticos = obtener_datos_climaticos_por_iata(iata_usuario, datos)

        if iata_corregido:
            print(f"Código IATA corregido: {iata_corregido}")
            print(f"Datos climáticos: {datos_climaticos}")
        else:
            print("No se pudieron obtener los datos climáticos.")
    else:
        print("Opción no válida.")
