"""
Código que sirve como buscador para consultar
y buscar información almacenada en el cache.

Creado por Erick Luis Juárez
"""
import cache
import dataset

def buscar_ciudad_y_datos_climaticos(datos, iata_usuario):
    """
    Busca la ciudad más cercana al IATA dado y devuelve el IATA corregido junto con los datos climáticos.

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.
        iata_usuario (str): Código IATA ingresado por el usuario.

    Returns:
        tuple: (iata_corregido, datos_climaticos) donde iata_corregido es el IATA corregido y 
               datos_climaticos es un diccionario con la información climática, o (None, None) si no se encuentra.
    """
    diccionario_ciudades = dataset.crear_diccionario_ciudades()
    iata_corregido = None

    for iata, ciudad in diccionario_ciudades.items():
        if iata_usuario.lower() in ciudad.lower():
            iata_corregido = iata
            break

    if not iata_corregido:
        return None, None
    
    coordenadas = dataset.obtener_coordenadas(datos, iata_corregido)
    if coordenadas:
        lat, lon = coordenadas
        url = cache.construir_url(lat, lon)
        json_data = cache.obtener_datos_desde_url(url)
        datos_climaticos = cache.extraer_informacion_relevante(json_data)
        return iata_corregido, datos_climaticos
    
    return None, None

