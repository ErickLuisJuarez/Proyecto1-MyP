from tkinter import *

def pantalla_recomendaciones_personal(window, pantalla_personal_datos, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Recomendaciones")

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

    ClimaOrigen=Label(frame_desliz, text="Clima del lugar \n de origen", font=("Montserrat",35, "bold"), fg="#011640")
    ClimaOrigen.grid(column=1, row=0, padx=(20, 10), pady=20, sticky="ew")

    TemperaturaOrigen=Label(frame_desliz, text="Temperatura:", font=("Montserrat", 30, "bold"), fg="#011640")
    TemperaturaOrigen.grid(column=1, row=2, padx=(20, 10), pady=20, sticky="ew")

    HumedadOrigen=Label(frame_desliz, text="Humedad:", font=("Montserrat", 30, "bold"), fg="#011640")
    HumedadOrigen.grid(column=1, row=4, padx=(20, 10), pady=20, sticky="ew")

    ProbabilidaLluviaOrigen=Label(frame_desliz, text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidaLluviaOrigen.grid(column=1, row=6, padx=(20, 10), pady=20, sticky="ew")

    PresionOrigen=Label(frame_desliz, text="Presion:", font=("Montserrat", 30, "bold"), fg="#011640")
    PresionOrigen.grid(column=1, row=7, padx=(20, 10), pady=20, sticky="ew")

    VelocidadVientoOrigen=Label(frame_desliz, text="Velocidad \n del viento:", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadVientoOrigen.grid(column=1, row=8, padx=(20, 10), pady=20, sticky="ew")

    window.FlechaDerecha = PhotoImage(file="Recursos/FlechaDer.png").subsample(5, 5)
    imagen = Canvas(frame_desliz, width=100, height=100)
    imagen.create_image(50, 50, image=window.FlechaDerecha)
    imagen.grid(column=2, row=0)

    ClimaLlegada=Label(frame_desliz, text="Clima del lugar \n de llegada", font=("Montserrat", 35, "bold"), fg="#011640")
    ClimaLlegada.grid(column=3, row=0, padx=(10, 100), pady=20, sticky="ew")

    TemperaturaLLegada=Label(frame_desliz, text="Temperatura:", font=("Montserrat", 30, "bold"), fg="#011640")
    TemperaturaLLegada.grid(column=3, row=2, padx=(20, 10), pady=20, sticky="ew")

    HumedadLlegada=Label(frame_desliz, text="Humedad:", font=("Montserrat", 30, "bold"), fg="#011640")
    HumedadLlegada.grid(column=3, row=4, padx=(20, 10), pady=20, sticky="ew")

    ProbabilidaLluviaLLegada=Label(frame_desliz, text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidaLluviaLLegada.grid(column=3, row=6, padx=(20, 10), pady=20, sticky="ew")

    PresionLlegada=Label(frame_desliz, text="Presion:", font=("Montserrat", 30, "bold"), fg="#011640")
    PresionLlegada.grid(column=3, row=7, padx=(20, 10), pady=20, sticky="ew")

    VelocidadVientoLlegada=Label(frame_desliz, text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadVientoLlegada.grid(column=3, row=8, padx=(20, 10), pady=20, sticky="ew")

    Recomendaciones = Label(frame_desliz, text="Recomendaciones", font=("Montserrat", 35, "bold"), fg="#011640")
    Recomendaciones.grid(column=1, row=9, columnspan=3, pady=(10, 0), sticky="ew")

    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_personal_datos(window, pantalla_principal))
    regreso.grid(column=1, row=10, columnspan=3, pady=20, sticky="ew")