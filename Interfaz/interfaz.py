from tkinter import *
from PantallaIdPersonal import pantalla_Idpersonal
from PantallaDatos import pantalla_Datos

def pantalla_principal(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Consulta de clima")
    window.minsize(width=1200, height=500)
    window.config(padx=20, pady=20)

    
    lienzo = Canvas(window, width=200, height=200) #.subsample(5.5)
    window.logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0)

    titulo1=Label(text="Consulta de clima", font=("Montserrat", 80, "bold"), fg="#011640")
    titulo1.grid(column=1, row=0)

    titulo1=Label(text="Selecciona tu rol", font=("Montserrat", 65, "bold"), fg="#3CA6A6")
    titulo1.grid(column=0, row=2, columnspan=3, pady=(20, 40))

    botoncliente = Button(window, text="Cliente", font=("Montserrat", 40, "bold"), fg="#026773",
                          command=lambda: pantalla_Datos(window, pantalla_principal))
    botoncliente.grid(column=1, row=3, padx=30, pady=15)

    botonpersonal = Button(window, text="Personal", font=("Montserrat", 40, "bold"), fg="#026773", 
                           command=lambda: pantalla_Idpersonal(window, pantalla_principal))
    botonpersonal.grid(column=1, row=4, padx=30, pady=15)

window = Tk()
pantalla_principal(window)
window.mainloop()