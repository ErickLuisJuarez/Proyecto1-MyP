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
    Corrige el nombre de la ciudad proporcionado por el usuario y devuelve el código IATA asociado.
    Usa coincidencias aproximadas para manejar errores tipográficos y nombres con espacios.

    Args:
        nombre_ciudad_usuario (str): Nombre de la ciudad ingresado por el usuario.

    Returns:
        tuple: Código IATA corregido si se encuentra una coincidencia,
               sugerencia de ciudad corregida si el nombre es similar pero incorrecto.
    """
    diccionario_ciudades = dataset.crear_diccionario_ciudades()
    
    nombre_ciudad_usuario = nombre_ciudad_usuario.lower().strip()
    nombre_ciudad_usuario = ' '.join(nombre_ciudad_usuario.split())
    nombre_ciudad_usuario = normalize('NFKD', nombre_ciudad_usuario).encode('ASCII', 'ignore').decode('ASCII')
    
    nombres_ciudades = {iata: normalize('NFKD', ciudad.lower()).encode('ASCII', 'ignore').decode('ASCII') 
                        for iata, ciudad in diccionario_ciudades.items()}
    
    coincidencias = difflib.get_close_matches(nombre_ciudad_usuario, nombres_ciudades.values(), n=1, cutoff=0.5)

    if coincidencias:
        ciudad_corregida = coincidencias[0]

        for iata, ciudad_normalizada in nombres_ciudades.items():
            if ciudad_normalizada == ciudad_corregida:
                if nombre_ciudad_usuario != ciudad_corregida:
                    return iata, f"Tal vez quisiste buscar: {diccionario_ciudades[iata]}"
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

def obtener_datos_climaticos_por_ticket(ticket_usuario, datos):
    """
    Obtiene los datos climáticos para los códigos IATA de origen y destino de un ticket proporcionado.

    Args:
        ticket_usuario (str): Número del ticket ingresado por el usuario.
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        tuple: (Código IATA de origen, datos climáticos de origen, Código IATA de destino, datos climáticos de destino)
               Si no se encuentra el ticket, devuelve (None, None, None, None).
    """
    diccionario_tickets = dataset.crear_diccionario_tickets()
    
    iata_origen_destino = diccionario_tickets.get(ticket_usuario)
    
    if iata_origen_destino:
        iata_origen, iata_destino = iata_origen_destino
        
        iata_corregido_origen, datos_climaticos_origen = obtener_datos_climaticos_por_iata(iata_origen, datos)
        if not iata_corregido_origen:
            return None, None, None, None
        
        iata_corregido_destino, datos_climaticos_destino = obtener_datos_climaticos_por_iata(iata_destino, datos)
        if not iata_corregido_destino:
            return None, None, None, None

        return iata_corregido_origen, datos_climaticos_origen, iata_corregido_destino, datos_climaticos_destino
    
    else:
        return None, None, None, None

def identificar_tipo_entrada(entrada_usuario):
    """
    Identifica si la entrada del usuario es un código IATA, una ciudad o un ticket.

    Args:
        entrada_usuario (str): Entrada proporcionada por el usuario.

    Returns:
        str: Tipo de entrada ('iata', 'ciudad', 'ticket').
    """
    entrada_usuario = entrada_usuario.strip()
    
    if len(entrada_usuario) == 3 and entrada_usuario.isalpha():
        return 'iata'
    
    if len(entrada_usuario) == 6 and any(char.isdigit() for char in entrada_usuario):
        return 'ticket'
    
    if any(char.isalpha() for char in entrada_usuario):
        return 'ciudad'
    
    return None

def obtener_datos_climaticos(entrada_usuario, datos):
    """
    Determina el tipo de entrada del usuario y obtiene los datos climáticos correspondientes.

    Args:
        entrada_usuario (str): Entrada proporcionada por el usuario.
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        tuple: Datos climáticos según el tipo de entrada del usuario.
    """
    tipo_entrada = identificar_tipo_entrada(entrada_usuario)

    if tipo_entrada == 'iata':
        iata_corregido, datos_climaticos = obtener_datos_climaticos_por_iata(entrada_usuario, datos)
        if iata_corregido:
            return f"Código IATA: {iata_corregido}", datos_climaticos
        else:
            return "No se pudieron obtener los datos climáticos para el código IATA.", None
    
    elif tipo_entrada == 'ciudad':
        iata_corregido, datos_climaticos = obtener_datos_climaticos_por_ciudad(entrada_usuario, datos)
        if iata_corregido:
            return f"Código IATA: {iata_corregido}", datos_climaticos
        else:
            return "No se pudieron obtener los datos climáticos para la ciudad.", None
    
    elif tipo_entrada == 'ticket':
        iata_origen, datos_climaticos_origen, iata_destino, datos_climaticos_destino = obtener_datos_climaticos_por_ticket(entrada_usuario, datos)
        if iata_origen and iata_destino:
            return (f"Código IATA de origen: {iata_origen}", f"Datos climáticos en origen: {datos_climaticos_origen}", 
                    f"Código IATA de destino: {iata_destino}", f"Datos climáticos en destino: {datos_climaticos_destino}")
        else:
            return "No se pudieron obtener los datos climáticos para el ticket.", None

    else:
        return "La entrada no es válida como código IATA, ciudad o número de ticket.", None


if __name__ == "__main__":
    datos = dataset.cargar_datos_de_archivo()

    entrada_usuario = input("Introduce un código IATA, nombre de ciudad o número de ticket: ").strip()
    resultado = obtener_datos_climaticos(entrada_usuario, datos)

    if isinstance(resultado, tuple):
        for item in resultado:
            print(item)
    else:
        print(resultado)