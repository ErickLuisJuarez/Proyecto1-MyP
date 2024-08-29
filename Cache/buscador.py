"""
Codigo que sirve como buscador para consultar
y buscar información almacenada en el cache

Creado por Erick Luis Juárez
"""
import csv

from Cache import cache

from dataset import cargar_datos_de_archivo, validar_datos

def cargar_datos_y_generar_busqueda():
    """
    Carga los datos desde el archivo CSV, valida los datos y genera el diccionario para la búsqueda.

    Retorna
    -------
        dict
            Diccionario donde cada clave es un código IATA y el valor es una lista de registros asociados.
    """
    datos = cargar_datos_de_archivo()
    validar_datos(datos)
    return generar_diccionario_iatas(datos)

# Carga los datos y genera el diccionario de búsqueda
diccionario_iatas = cargar_datos_y_generar_busqueda()

def generar_diccionario_iatas(datos):
    """Genera un diccionario con las IATA como claves y sus registros como valores."""
    diccionario_iatas = {}
    for fila in datos:
        iata_origen = fila['origin']
        iata_destino = fila['destination']
        if iata_origen not in diccionario_iatas:
            diccionario_iatas[iata_origen] = []
        if iata_destino not in diccionario_iatas:
            diccionario_iatas[iata_destino] = []
        diccionario_iatas[iata_origen].append(fila)
        diccionario_iatas[iata_destino].append(fila)
    return diccionario_iatas

def buscar_por_iata(iata, diccionario_iatas):
    """Realiza una búsqueda por IATA y devuelve una lista de listas con coincidencias."""
    return diccionario_iatas.get(iata, [])