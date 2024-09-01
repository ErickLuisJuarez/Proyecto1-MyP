from tkinter import *

window = Tk()
window.title("Personal")
window.minsize(width=800, height=800)
window.config(padx=20, pady=20)

imagen = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Recursos/LogoAeropuerto.png")
imagen.create_image(100,100, image=logo_img)
imagen.grid(column=0, row=0)

tituloPrincipal=Label(text="Personal", font=("Montserrat", 60, "bold"), fg="#011640")
tituloPrincipal.grid(column=1, row=0, pady=20, sticky="w")

tituloSecundario=Label(text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
tituloSecundario.grid(column=0, row=1, columnspan=3, padx=150, sticky="n", pady=15)

Origen=Label(text="Origen", font=("Montserrat", 20, "bold"), fg="#026773")
Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
entradaOrigen = Entry(width= 20, font=("Montserrat", 15))
entradaOrigen.grid(column=1, row=3)

Destino=Label(text="Destino", font=("Montserrat", 20, "bold"), fg="#026773")
Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
entradaDestino = Entry(width= 20, font=("Montserrat", 15))
entradaDestino.grid(column=1, row=4)

HoraDeSalida=Label(text="Hora de salida", font=("Montserrat", 20, "bold"), fg="#026773")
HoraDeSalida.grid(column=0, row=5, padx=(0, 10), pady=15)
entradaHoraSalida = Entry(width= 20, font=("Montserrat", 15))
entradaHoraSalida.grid(column=1, row=5)

HoraDellegada=Label(text="Hora de llegada", font=("Montserrat", 20, "bold"), fg="#026773")
HoraDellegada.grid(column=0, row=6, padx=(0, 10), pady=15)
entradaHoraLlegada = Entry(width= 20, font=("Montserrat", 15))
entradaHoraLlegada.grid(column=1, row=6)

LatitudOrigen=Label(text="Latitud del origen", font=("Montserrat", 20, "bold"), fg="#026773")
LatitudOrigen.grid(column=0, row=7, padx=(0, 10), pady=15)
entradaLatitudOrigen = Entry(width= 20, font=("Montserrat", 15))
entradaLatitudOrigen.grid(column=1, row=7)

LatitudDestino=Label(text="Latitud del destino", font=("Montserrat", 20, "bold"), fg="#026773")
LatitudDestino.grid(column=0, row=8, padx=(0, 10), pady=15)
entradaLatitudDestino = Entry(width= 20, font=("Montserrat", 15))
entradaLatitudDestino.grid(column=1, row=8)

LongitudDestino=Label(text="Longitud del destino", font=("Montserrat", 20, "bold"), fg="#026773")
LongitudDestino.grid(column=0, row=9, padx=(0, 10), pady=15)
entradaLongitudDestino = Entry(width= 20, font=("Montserrat", 15))
entradaLongitudDestino.grid(column=1, row=9)

BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
siguiente = Button(image=BotonSiguiente, borderwidth=0)
siguiente.grid(column=1, row=10)

BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
siguiente = Button(image=BotonRegreso, borderwidth=0)
siguiente.grid(column=0, row=10)

window.mainloop()