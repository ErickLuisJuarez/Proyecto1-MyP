from tkinter import *

def pantalla_clima(window, pantalla_personal_datos, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Clima")

    window.geometry("1200x600")

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
    frame_logo_titulo.grid(column=0, row=0, padx=(20, 10), pady=20, sticky="ew")

    window.logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    ClimaOrigen=Label(frame_desliz, text="Clima", font=("Montserrat",45, "bold"), fg="#011640")
    ClimaOrigen.grid(column=1, row=0, padx=(20, 10), pady=20, sticky="ew")

    TemperaturaOrigen=Label(frame_desliz, text="Temperatura:", font=("Montserrat", 30, "bold"), fg="#011640")
    TemperaturaOrigen.grid(column=0, row=2, padx=(20, 10), pady=20, sticky="ew")

    HumedadOrigen=Label(frame_desliz, text="Humedad:", font=("Montserrat", 30, "bold"), fg="#011640")
    HumedadOrigen.grid(column=0, row=4, padx=(20, 10), pady=20, sticky="ew")

    ProbabilidaLluviaOrigen=Label(frame_desliz, text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidaLluviaOrigen.grid(column=0, row=6, padx=(20, 10), pady=20, sticky="ew")

    PresionOrigen=Label(frame_desliz, text="Presion:", font=("Montserrat", 30, "bold"), fg="#011640")
    PresionOrigen.grid(column=0, row=7, padx=(20, 10), pady=20, sticky="ew")

    VelocidadVientoOrigen=Label(frame_desliz, text="Velocidad \n del viento:", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadVientoOrigen.grid(column=0, row=8, padx=(20, 10), pady=20, sticky="ew")

    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_personal_datos(window, pantalla_principal))
    regreso.grid(column=1, row=9, columnspan=3, pady=20, sticky="ew")