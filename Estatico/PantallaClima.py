from tkinter import *
import buscador 
import dataset  

def pantalla_clima(window, pantalla_principal, ticket_usuario):
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
    window.geometry("1500x1200")

    datos = dataset.cargar_datos_de_archivo()

    iata_origen, datos_climaticos_origen, iata_destino, datos_climaticos_destino = buscador.obtener_datos_climaticos_por_ticket(ticket_usuario, datos)

    # Si no hay datos climáticos disponibles
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

    window.logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    # Clima de Origen
    ClimaOrigen = Label(frame_logo_titulo, text="Clima del lugar \n de origen", font=("Montserrat", 40, "bold"), fg="#011640")
    ClimaOrigen.grid(column=1, row=0, padx=(20, 10), pady=20, sticky="w")

    TemperaturaOrigen = Label(frame_desliz, text=f"Temperatura: \n {datos_climaticos_origen['temperatura']} °c", font=("Montserrat", 30, "bold"), fg="#011640")
    TemperaturaOrigen.grid(column=1, row=1, padx=(20, 10), pady=(10, 0), sticky="w")

    HumedadOrigen = Label(frame_desliz, text=f"Humedad: \n {datos_climaticos_origen['humedad']}", font=("Montserrat", 30, "bold"), fg="#011640")
    HumedadOrigen.grid(column=1, row=2, padx=(40, 10), pady=10, sticky="w")

    ProbabilidaLluviaOrigen = Label(frame_desliz, text=f"Probabilidad \n de lluvia: \n {datos_climaticos_origen['probabilidad_lluvia']}%", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidaLluviaOrigen.grid(column=1, row=3, padx=(30, 10), pady=10, sticky="w")

    PresionOrigen = Label(frame_desliz, text=f"Presión: \n {datos_climaticos_origen['presion']}", font=("Montserrat", 30, "bold"), fg="#011640")
    PresionOrigen.grid(column=1, row=4, padx=(80, 10), pady=10, sticky="w")

    VelocidadVientoOrigen = Label(frame_desliz, text=f"Velocidad \n del viento: \n {datos_climaticos_origen['velocidad_viento']}", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadVientoOrigen.grid(column=1, row=5, padx=(40, 10), pady=10, sticky="w")

    window.flecaDer = PhotoImage(file="Recursos/FlechaDer.png").subsample(3, 3)
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.flecaDer)
    lienzo.grid(column=2, row=0, padx=(0, 10))

    # Clima de Destino
    ClimaLlegada = Label(frame_logo_titulo, text="Clima del lugar \n de destino", font=("Montserrat", 40, "bold"), fg="#011640")
    ClimaLlegada.grid(column=3, row=0, padx=(20, 10), pady=20, sticky="w")

    TemperaturaLlegada = Label(frame_desliz, text=f"Temperatura: \n {datos_climaticos_destino['temperatura']} °c", font=("Montserrat", 30, "bold"), fg="#011640")
    TemperaturaLlegada.grid(column=3, row=1, padx=(20, 10), pady=(10, 0), sticky="w")

    HumedadLlegada = Label(frame_desliz, text=f"Humedad: \n {datos_climaticos_destino['humedad']}", font=("Montserrat", 30, "bold"), fg="#011640")
    HumedadLlegada.grid(column=3, row=2, padx=(40, 10), pady=10, sticky="w")

    ProbabilidaLluviaLlegada = Label(frame_desliz, text=f"Probabilidad \n de lluvia: \n {datos_climaticos_destino['probabilidad_lluvia']}% ", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidaLluviaLlegada.grid(column=3, row=3, padx=(30, 10), pady=10, sticky="w")

    PresionLlegada = Label(frame_desliz, text=f"Presión: \n{datos_climaticos_destino['presion']}", font=("Montserrat", 30, "bold"), fg="#011640")
    PresionLlegada.grid(column=3, row=4, padx=(80, 10), pady=10, sticky="w")

    VelocidadVientoLlegada = Label(frame_desliz, text=f"Velocidad \n del viento: \n {datos_climaticos_destino['velocidad_viento']}", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadVientoLlegada.grid(column=3, row=5, padx=(40, 10), pady=10, sticky="w")

    # Botón de regreso
    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(1, 1)
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=1, row=9, columnspan=2, pady=20, padx=(400, 10), sticky="ew")

if __name__ == "__main__":
    root = Tk()
    pantalla_clima(root, lambda w: print("Pantalla principal"), "12345")
    root.mainloop()
