"""
Código que sirve como buscador para consultar
y buscar información almacenada en el cache.

Creado por Erick Luis Juárez
"""
import dataset
import cache
from unicodedata import normalize

def corregir_nombre_ciudad(nombre_ciudad_usuario):
    """
    Corrige el nombre de la ciudad proporcionado por el usuario.
    Utiliza el diccionario de ciudades para encontrar una coincidencia.
    
    Args:
        nombre_ciudad_usuario (str): Nombre de la ciudad ingresado por el usuario.
    
    Returns:
        str: Código IATA corregido si se encuentra una coincidencia, None en caso contrario.
    """
    diccionario_ciudades = dataset.crear_diccionario_ciudades()
    iata_corregido = None
    
    nombre_ciudad_usuario = nombre_ciudad_usuario.lower()
    nombre_ciudad_usuario = normalize('NFKD', nombre_ciudad_usuario).encode('ASCII', 'ignore').decode('ASCII')
    
    for iata, ciudad in diccionario_ciudades.items():
        if nombre_ciudad_usuario in ciudad.lower():
            iata_corregido = iata
            break
    
    return iata_corregido

def obtener_datos_climaticos(iata_usuario, datos):
    """
    Obtiene los datos climáticos para una ciudad proporcionada por el usuario.

    Args:
        iata_usuario (str): Código IATA de la ciudad para la cual se obtendrán los datos climáticos.
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        tuple: (Código IATA corregido, datos climáticos) si se encuentran coordenadas,
               (None, None) en caso contrario.
    """
    iata_corregido = corregir_nombre_ciudad(iata_usuario)
    if not iata_corregido:
        return "No se encontró la IATA", None
    
    coordenadas = dataset.obtener_coordenadas(datos, iata_corregido)
    if coordenadas:
        lat, lon = coordenadas
        ciudad = dataset.obtener_nombre_ciudad_por_iata(iata_corregido)
        if ciudad:
            url = cache.construir_url(ciudad)
            json_data = cache.obtener_datos_desde_url(url)
            datos_climaticos = cache.extraer_informacion_relevante(json_data)
            return iata_corregido, datos_climaticos
    return "No se encontraron datos climáticos", None


if __name__ == "__main__":
    datos = dataset.cargar_datos_de_archivo()
    nombre_ciudad_usuario = input("Introduce IATA o nombre de la ciudad: ")
    iata_corregido, datos_climaticos = obtener_datos_climaticos(nombre_ciudad_usuario, datos)
    
    print(f"Código IATA: {iata_corregido}")
    print(f"Nombre de la ciudad: {nombre_ciudad_usuario}")
    print(f"Datos climáticos: {datos_climaticos}")