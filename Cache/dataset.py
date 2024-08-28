""""
Codigo que gestiona y procesa los datos del archivo dataset1.cvs

Creado por Erick Luis Juárez 
"""
# Se importa el modulo pandas para 
import pandas as pd
#Se importa el codigo cache de la carpeta Cache
from Cache import cache

def cargar_datos_de_archivo(archivo): 
    try:
        datos = pd.read_csv(archivo, encoding="utf-8")
        # Validar que no haya valores nulos en las columnas clave
        if datos[['origin', 'destination', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude']].isnull().any().any():
            raise ValueError("El archivo contiene valores nulos.")
        print("Datos cargados y validados con éxito.")
        return datos
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError, ValueError) as error:
        print(f"Error al cargar o validar los datos: {error}")
        raise

def obtener_coordenadas(datos, iata):
    fila_origen = datos[datos['origin'] == iata]
    fila_destino = datos[datos['destination'] == iata]
    
    if not fila_origen.empty:
        return (fila_origen.iloc[0]['origin_latitude'], fila_origen.iloc[0]['origin_longitude'])
    elif not fila_destino.empty:
        return (fila_destino.iloc[0]['destination_latitude'], fila_destino.iloc[0]['destination_longitude'])
    else:
        return None

def obtener_iata(datos):
    iatas_origen = datos['origin'].unique()
    iatas_destino = datos['destination'].unique()
    iatas_unicos = pd.unique(pd.concat([pd.Series(iatas_origen), pd.Series(iatas_destino)]))
    return iatas_unicos

def es_iata_valido(datos, iata):
    return not datos[(datos['origin'] == iata) | (datos['destination'] == iata)].empty

def obtener_nombres(datos):
    return pd.concat([datos['origin'], datos['destination']]).unique()

def nombre_valido(datos, nombre):
    return nombre in obtener_nombres(datos)