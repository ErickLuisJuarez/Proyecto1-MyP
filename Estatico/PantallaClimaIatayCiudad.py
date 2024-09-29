from tkinter import *
import buscador
import dataset
from buscador import obtener_nombre_ciudad

def ajustar_tamano_ventana(window, ancho_porcentaje=0.8, alto_porcentaje=0.8):

    ancho_pantalla = window.winfo_screenwidth()
    alto_pantalla = window.winfo_screenheight()

    
    nuevo_ancho = int(ancho_pantalla * ancho_porcentaje)
    nuevo_alto = int(alto_pantalla * alto_porcentaje)

    
    window.geometry(f"{nuevo_ancho}x{nuevo_alto}")

def pantalla_clima_iata_ciudad(window, pantalla_principal, entrada_usuario):
    """
    Muestra la pantalla de clima con los datos climáticos según la entrada del usuario.
    
    Args:
        window (Tk): La ventana principal de la aplicación Tkinter.
        pantalla_principal (function): Función para mostrar la pantalla principal.
        entrada_usuario (str): Entrada del usuario (puede ser un código IATA, nombre de ciudad o ticket).
    """
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Clima")
    ajustar_tamano_ventana(window)  

    datos = dataset.cargar_datos_de_archivo()
    resultado, datos_climaticos = buscador.obtener_datos_climaticos(entrada_usuario, datos)

    canvas = Canvas(window)
    deslizador = Scrollbar(window, orient="vertical", command=canvas.yview)
    frame_desliz = Frame(canvas)

    frame_desliz.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
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
    lienzo.grid(column=1, row=0, padx=(0, 10))

    ClimaTitulo = Label(frame_logo_titulo, text="Clima", font=("Montserrat", 60, "bold"), fg="#011640") 
    ClimaTitulo.grid(column=2, row=0, padx=(150, 10), pady=20, sticky="w")

    Subtitulo = Label(frame_desliz, text=f"Mostrando resultados para {obtener_nombre_ciudad(entrada_usuario).capitalize()}", font=("Montserrat", 22, "italic"), fg="#011640")
    Subtitulo.grid(column=2, row=1, padx=(150, 10), pady=20, sticky="w")

    if datos_climaticos:
        Temperatura = Label(frame_desliz, text=f"Temperatura: \n {datos_climaticos.get('temperatura', 'No disponible')} °C", font=("Montserrat", 24, "bold"), fg="#011640")  
        Temperatura.grid(column=2, row=2, padx=(250, 10), pady=(10, 0), sticky="w")

        Humedad = Label(frame_desliz, text=f"Humedad: \n {datos_climaticos.get('humedad', 'No disponible')}", font=("Montserrat", 24, "bold"), fg="#011640")  
        Humedad.grid(column=2, row=3, padx=(250, 10), pady=10, sticky="w")

        ProbabilidadLluvia = Label(frame_desliz, text=f"Probabilidad \n de lluvia: \n {datos_climaticos.get('probabilidad_lluvia', 'No disponible')}%", font=("Montserrat", 24, "bold"), fg="#011640") 
        ProbabilidadLluvia.grid(column=2, row=4, padx=(250, 10), pady=10, sticky="w")

        Presion = Label(frame_desliz, text=f"Presión: \n {datos_climaticos.get('presion', 'No disponible')}", font=("Montserrat", 24, "bold"), fg="#011640")  
        Presion.grid(column=2, row=5, padx=(250, 10), pady=10, sticky="w")

        VelocidadViento = Label(frame_desliz, text=f"Velocidad \n del viento: \n {datos_climaticos.get('velocidad_viento', 'No disponible')} km/h", font=("Montserrat", 24, "bold"), fg="#011640")  
        VelocidadViento.grid(column=2, row=6, padx=(250, 10), pady=10, sticky="w")
    else:
        error_label = Label(frame_desliz, text=resultado, font=("Montserrat", 24, "bold"), fg="red")  
        error_label.grid(column=2, row=1, padx=(250, 10), pady=(10, 0), sticky="w")

    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)  
    regreso = Button(frame_desliz, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=1, row=10, columnspan=2, pady=20, padx=(250, 10), sticky="ew")

if __name__ == "__main__":
    root = Tk()
    pantalla_clima_iata_ciudad(root, lambda w: print("Pantalla principal"), "Ciudad de México")
    root.mainloop()
