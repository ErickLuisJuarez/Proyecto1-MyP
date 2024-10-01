from tkinter import *
from Cache import buscador
from Cache import dataset
import webbrowser

def ajustar_tamano_ventana(window, ancho_porcentaje=0.8, alto_porcentaje=0.8):
    """
     Ajusta el tamaño de la ventana en función de un porcentaje de la resolución de la pantalla.

    Args:
        window (Tk): La ventana de la aplicación.
        ancho_porcentaje (float): El porcentaje del ancho de la pantalla que ocupará la ventana.
        alto_porcentaje (float): El porcentaje del alto de la pantalla que ocupará la ventana.
    """
    ancho_pantalla = window.winfo_screenwidth()
    alto_pantalla = window.winfo_screenheight()

    nuevo_ancho = int(ancho_pantalla * ancho_porcentaje)
    nuevo_alto = int(alto_pantalla * alto_porcentaje)

    window.geometry(f"{nuevo_ancho}x{nuevo_alto}")

def pantalla_clima_ticket(window, pantalla_principal, ticket_usuario):
    """
    Muestra la pantalla de clima con los datos climáticos de la ciudad especificada por el usuario.

    Args:
        window (Tk): La ventana principal de la aplicación Tkinter.
        pantalla_principal (function): Función para mostrar la pantalla principal.
        ticket_usuario (str): Número del ticket ingresado por el usuario.
    """
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Clima")
    ajustar_tamano_ventana(window)

    datos = dataset.cargar_datos_de_archivo()

    iata_origen, datos_climaticos_origen, iata_destino, datos_climaticos_destino = buscador.obtener_datos_climaticos_por_ticket(ticket_usuario, datos)

    if datos_climaticos_origen is None:
        datos_climaticos_origen = {
            "temperatura": "No disponible",
            "humedad": "No disponible",
            "probabilidad_lluvia": "No disponible",
            "presion": "No disponible",
            "velocidad_viento": "No disponible"
        }

    if datos_climaticos_destino is None:
        datos_climaticos_destino = {
            "temperatura": "No disponible",
            "humedad": "No disponible",
            "probabilidad_lluvia": "No disponible",
            "presion": "No disponible",
            "velocidad_viento": "No disponible"
        }

    canvas = Canvas(window)
    deslizador = Scrollbar(window, orient="vertical", command=canvas.yview)
    frame_desliz = Frame(canvas)

    frame_desliz.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=frame_desliz, anchor="nw")
    canvas.configure(yscrollcommand=deslizador.set)

    canvas.grid(row=0, column=0, sticky="nsew")
    deslizador.grid(row=0, column=1, sticky="ns")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    frame_logo_titulo = Frame(frame_desliz)
    frame_logo_titulo.grid(column=0, row=0, padx=(20, 10), pady=20, sticky="ew", columnspan=4)

    window.logoaeropuerto = PhotoImage(file="Img/LogoAeropuerto.png")
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    ClimaOrigen = Label(frame_logo_titulo, text=f"Clima del lugar \n de origen: \n {buscador.obtener_nombres_ciudades(ticket_usuario)[0]}", font=("Montserrat", 20, "bold"), fg="#011640")
    ClimaOrigen.grid(column=1, row=0, padx=(20, 10), pady=20, sticky="w")

    TemperaturaOrigen = Label(frame_desliz, text=f"Temperatura: \n {datos_climaticos_origen['temperatura']} °c", font=("Montserrat", 18, "bold"), fg="#011640")
    TemperaturaOrigen.grid(column=1, row=1, padx=(20, 10), pady=(10, 0), sticky="w")

    HumedadOrigen = Label(frame_desliz, text=f"Humedad: \n {datos_climaticos_origen['humedad']}", font=("Montserrat", 18, "bold"), fg="#011640")
    HumedadOrigen.grid(column=1, row=2, padx=(40, 10), pady=10, sticky="w")

    ProbabilidaLluviaOrigen = Label(frame_desliz, text=f"Probabilidad \n de lluvia: \n {datos_climaticos_origen['probabilidad_lluvia']}%", font=("Montserrat", 18, "bold"), fg="#011640")
    ProbabilidaLluviaOrigen.grid(column=1, row=3, padx=(30, 10), pady=10, sticky="w")

    PresionOrigen = Label(frame_desliz, text=f"Presión: \n {datos_climaticos_origen['presion']}", font=("Montserrat", 18, "bold"), fg="#011640")
    PresionOrigen.grid(column=1, row=4, padx=(80, 10), pady=10, sticky="w")

    VelocidadVientoOrigen = Label(frame_desliz, text=f"Velocidad \n del viento: \n {datos_climaticos_origen['velocidad_viento']}", font=("Montserrat", 18, "bold"), fg="#011640")
    VelocidadVientoOrigen.grid(column=1, row=5, padx=(40, 10), pady=10, sticky="w")

    window.flecaDer = PhotoImage(file="Img/FlechaDer.png").subsample(4, 4) 
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.flecaDer)
    lienzo.grid(column=2, row=0, padx=(0, 10))

    
    ClimaLlegada = Label(frame_logo_titulo, text=f"Clima del lugar \n de destino: \n {buscador.obtener_nombres_ciudades(ticket_usuario)[1]}", font=("Montserrat", 20, "bold"), fg="#011640")
    ClimaLlegada.grid(column=3, row=0, padx=(20, 10), pady=20, sticky="w")

    TemperaturaLlegada = Label(frame_desliz, text=f"Temperatura: \n {datos_climaticos_destino['temperatura']} °c", font=("Montserrat", 18, "bold"), fg="#011640")
    TemperaturaLlegada.grid(column=3, row=1, padx=(20, 10), pady=(10, 0), sticky="w")

    HumedadLlegada = Label(frame_desliz, text=f"Humedad: \n {datos_climaticos_destino['humedad']}", font=("Montserrat", 18, "bold"), fg="#011640")
    HumedadLlegada.grid(column=3, row=2, padx=(40, 10), pady=10, sticky="w")

    ProbabilidaLluviaLlegada = Label(frame_desliz, text=f"Probabilidad \n de lluvia: \n {datos_climaticos_destino['probabilidad_lluvia']}% ", font=("Montserrat", 18, "bold"), fg="#011640")
    ProbabilidaLluviaLlegada.grid(column=3, row=3, padx=(30, 10), pady=10, sticky="w")

    PresionLlegada = Label(frame_desliz, text=f"Presión: \n{datos_climaticos_destino['presion']}", font=("Montserrat", 18, "bold"), fg="#011640")
    PresionLlegada.grid(column=3, row=4, padx=(80, 10), pady=10, sticky="w")

    VelocidadVientoLlegada = Label(frame_desliz, text=f"Velocidad \n del viento: \n {datos_climaticos_destino['velocidad_viento']}", font=("Montserrat", 18, "bold"), fg="#011640")
    VelocidadVientoLlegada.grid(column=3, row=5, padx=(40, 10), pady=10, sticky="w")

    window.BotonRegreso = PhotoImage(file="Img/BotonRegreso.png").subsample(2, 2)
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=1, row=9, columnspan=2, pady=20, padx=(200, 10), sticky="ew")

if __name__ == "__main__":
    root = Tk()
    pantalla_clima_ticket(root, lambda w: print("Pantalla principal"), "12345")
    root.mainloop()
