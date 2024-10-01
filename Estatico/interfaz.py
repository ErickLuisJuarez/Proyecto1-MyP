from tkinter import *
from PantallaClimaTicket import pantalla_clima_ticket
from PantallaClimaIatayCiudad import pantalla_clima_iata_ciudad
import dataset

def ajustar_tamano_ventana(window, ancho_porcentaje=0.8, alto_porcentaje=0.8):
    ancho_pantalla = window.winfo_screenwidth()
    alto_pantalla = window.winfo_screenheight()
    nuevo_ancho = int(ancho_pantalla * ancho_porcentaje)
    nuevo_alto = int(alto_pantalla * alto_porcentaje)
    window.geometry(f"{nuevo_ancho}x{nuevo_alto}")

def pantalla_principal(window):
    """
    Esta es la pantalla principal de inicio al ejecutar el programa de consulta de clima.
    """
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Consulta de clima")
    window.minsize(width=100, height=700)
    window.config(padx=20, pady=20)

    ajustar_tamano_ventana(window)

    lienzo = Canvas(window, width=200, height=200) 
    window.logoaeropuerto = PhotoImage(file="Img/LogoAeropuerto.png")
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0)

    titulo1 = Label(text="Consulta de clima", font=("Montserrat", 40, "bold"), fg="#011640") 
    titulo1.grid(column=1, row=0)

    titulo2 = Label(window, text="Introduzca IATA, Ciudad o Ticket \n para realizar la búsqueda", font=("Montserrat", 20, "bold"), fg="#3CA6A6")
    titulo2.grid(column=1, row=1, padx=50, pady=30, sticky="n")

    Pedir_datos = Label(window, text="Datos:", font=("Montserrat", 15, "bold"), fg="#026773")
    Pedir_datos.grid(column=0, row=2, pady=15)
    
    Datos_entrada = Entry(window, width=20, font=("Montserrat", 12))
    Datos_entrada.grid(column=1, row=2)

    mensaje_invalido = Label(window, text="", font=("Montserrat", 15), fg="red")
    mensaje_invalido.grid(column=0, row=3, columnspan=2)

    Anuncio1 = Label(text="Compra aquí \n tu boleto!", font=("Montserrat", 30, "bold"), fg="#011640") 
    Anuncio1.grid(column=2, row=0, padx=50)

    def abrir_aeropuerto():
        url = "https://acortar.link/sDOAlu"
        webbrowser.open(url)
    window.BotonBoleto = PhotoImage(file="Img/Boleto.png").subsample(15,15)
    boleto = Button(window, image=window.BotonBoleto, borderwidth=0, command=abrir_aeropuerto)
    boleto.grid(column=2, row=1, padx=50)

    Anuncio2 = Label(text="Realiza reserva \n de hotel aquí!", font=("Montserrat", 30, "bold"), fg="#011640") 
    Anuncio2.grid(column=2, row=2, padx=50)

    def abrir_trivago():
        url = "https://acortar.link/PvQw9P"
        webbrowser.open(url)     
    window.BotonHotel = PhotoImage(file="Img/Hotel.png").subsample(3, 3)
    hotel = Button(window, image=window.BotonHotel, borderwidth=0, command=abrir_trivago)
    hotel.grid(column=2, row=3, padx=50)

    BotonSiguiente = PhotoImage(file="Img/BotonSiguiente.png")
    window.boton_siguiente_imagen = BotonSiguiente
    siguiente = Button(window, image=BotonSiguiente, borderwidth=0, command=lambda: validar_datos(window, Datos_entrada, mensaje_invalido))
    siguiente.grid(column=1, row=4, pady=30)

    def validar_datos(window, entrada, mensaje_invalido):
        """
        Valida la longitud de la entrada de datos y determina el tipo de entrada (IATA, ciudad o ticket).
        """
        datos = entrada.get().strip()  
        print(f"Datos ingresados: {datos}")

        tipo_entrada = identificar_tipo_entrada(datos)

        if tipo_entrada == 'ticket':
            print("Ticket identificado. Avanzando a la pantalla de ticket.") 
            mensaje_invalido.config(text="")
            pantalla_clima_ticket(window, pantalla_principal, datos)  
        elif tipo_entrada in ['iata', 'ciudad']:
            print(f"{tipo_entrada.capitalize()} identificado. Avanzando a la pantalla de IATA/Ciudad.")
            mensaje_invalido.config(text="")
            pantalla_clima_iata_ciudad(window, pantalla_principal, datos) 
        else:
            mensaje_invalido.config(text="Entrada inválida. Debe ser IATA, Ciudad o Ticket.")
            print("Datos inválidos. Por favor, ingrese datos válidos.")

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

window = Tk()
pantalla_principal(window)
window.mainloop()