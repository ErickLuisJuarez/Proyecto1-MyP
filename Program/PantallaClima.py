from tkinter import *
import buscador  # Asegúrate de importar correctamente tu módulo que contiene la función obtener_datos_climaticos
import dataset  # Este módulo debería contener la función cargar_datos_de_archivo

def pantalla_clima(window, pantalla_personal_datos, pantalla_principal, ciudad_origen):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Clima")
    window.geometry("900x600")

    # Cargar datos del archivo CSV
    datos = dataset.cargar_datos_de_archivo()

    # Obtener los datos climáticos
    iata_corregido, datos_climaticos = buscador.obtener_datos_climaticos(ciudad_origen, datos)

    if datos_climaticos is None:
        datos_climaticos = {
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
    frame_logo_titulo.grid(column=0, row=0, padx=(20, 10), pady=20, sticky="ew")

    window.logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo = Canvas(frame_logo_titulo, width=200, height=200)
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    Clima = Label(frame_desliz, text="Clima", font=("Montserrat", 70, "bold"), fg="#011640")
    Clima.grid(column=1, row=0, padx=(20, 10), sticky="ew")

    Temperatura = Label(frame_desliz, text=f"Temperatura: {datos_climaticos['temperatura']}", font=("Montserrat", 30, "bold"), fg="#011640")
    Temperatura.grid(column=1, row=1, padx=(20, 10), sticky="ew")

    Humedad = Label(frame_desliz, text=f"Humedad: {datos_climaticos['humedad']}", font=("Montserrat", 30, "bold"), fg="#011640")
    Humedad.grid(column=1, row=2, padx=(20, 10), pady=20, sticky="ew")

    ProbabilidadLluvia = Label(frame_desliz, text=f"Probabilidad \n de lluvia: {datos_climaticos['probabilidad_lluvia']}", font=("Montserrat", 30, "bold"), fg="#011640")
    ProbabilidadLluvia.grid(column=1, row=3, padx=(20, 10), pady=20, sticky="ew")

    Presion = Label(frame_desliz, text=f"Presión: {datos_climaticos['presion']}", font=("Montserrat", 30, "bold"), fg="#011640")
    Presion.grid(column=1, row=4, padx=(20, 10), pady=20, sticky="ew")

    VelocidadViento = Label(frame_desliz, text=f"Velocidad \n del viento: {datos_climaticos['velocidad_viento']}", font=("Montserrat", 30, "bold"), fg="#011640")
    VelocidadViento.grid(column=1, row=5, padx=(20, 10), pady=20, sticky="ew")

    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_personal_datos(window, pantalla_principal))
    regreso.grid(column=1, row=9, columnspan=6, pady=20, sticky="ew")

if __name__ == "__main__":
    root = Tk()
    pantalla_clima(root, lambda w, p: print("Regresando..."), lambda: print("Pantalla principal"), "Madrid")
    root.mainloop()
