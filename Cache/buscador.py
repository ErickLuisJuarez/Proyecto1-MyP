"""
Codigo que sirve como buscador para consultar
y buscar información almacenada en el cache

Creado por Erick Luis Juárez
"""
import csv

from Cache import cache

from dataset import cargar_datos_de_archivo, validar_datos, generar_diccionario_iatas

def cargar_datos_y_generar_busqueda():
    """
    Carga los datos desde el archivo CSV, valida los datos y genera el diccionario para la búsqueda.

    Returns:
        dict: Diccionario donde cada clave es un código IATA y el valor es una lista de registros asociados.
    """
    datos = cargar_datos_de_archivo()
    validar_datos(datos)
    return generar_diccionario_iatas(datos)

# Carga los datos y genera el diccionario de búsqueda
diccionario_iatas = cargar_datos_y_generar_busqueda()

def buscar_por_iata(iata, diccionario_iatas):
    """
    Realiza una búsqueda por IATA y devuelve una lista de registros que coinciden con el IATA.

    Args:
        iata (str): Código IATA a buscar.
        diccionario_iatas (dict): Diccionario con los datos organizados por IATA.

    Returns:
        list: Lista de registros que coinciden con el IATA, o una lista vacía si no se encuentran coincidencias.
    """
    return diccionario_iatas.get(iata, [])