from tkinter import *

window = Tk()
window.title("Recomendaciones")
window.minsize(width=800, height=800)
window.config(pady=20)

ClimaOrigen=Label(text="Clima del lugar \n de origen", font=("Montserrat",40, "bold"), fg="#011640")
ClimaOrigen.grid(column=1, row=0, padx=(20, 10), pady=20, sticky="ew")

TemperaturaOrigen=Label(text="Temperatura:", font=("Montserrat", 30, "bold"), fg="#011640")
TemperaturaOrigen.grid(column=1, row=2, padx=(20, 10), pady=20, sticky="ew")

HumedadOrigen=Label(text="Humedad:", font=("Montserrat", 30, "bold"), fg="#011640")
HumedadOrigen.grid(column=1, row=4, padx=(20, 10), pady=20, sticky="ew")

ProbabilidaLluviaOrigen=Label(text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
ProbabilidaLluviaOrigen.grid(column=1, row=6, padx=(20, 10), pady=20, sticky="ew")

PresionOrigen=Label(text="Presion:", font=("Montserrat", 30, "bold"), fg="#011640")
PresionOrigen.grid(column=1, row=7, padx=(20, 10), pady=20, sticky="ew")

VelocidadVientoOrigen=Label(text="Velocidad \n del viento:", font=("Montserrat", 30, "bold"), fg="#011640")
VelocidadVientoOrigen.grid(column=1, row=8, padx=(20, 10), pady=20, sticky="ew")

imagen = Canvas(width=100, height=100)
FlechaDerecha = PhotoImage(file="Recursos/FlechaDer.png").subsample(5, 5)
imagen.create_image(50, 50, image=FlechaDerecha)
imagen.grid(column=2, row=0)

ClimaLlegada=Label(text="Clima del lugar \n de llegada", font=("Montserrat", 40, "bold"), fg="#011640")
ClimaLlegada.grid(column=3, row=0, padx=(10, 100), pady=20, sticky="ew")

TemperaturaLLegada=Label(text="Temperatura:", font=("Montserrat", 30, "bold"), fg="#011640")
TemperaturaLLegada.grid(column=3, row=2, padx=(20, 10), pady=20, sticky="ew")

HumedadLlegada=Label(text="Humedad:", font=("Montserrat", 30, "bold"), fg="#011640")
HumedadLlegada.grid(column=3, row=4, padx=(20, 10), pady=20, sticky="ew")

ProbabilidaLluviaLLegada=Label(text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
ProbabilidaLluviaLLegada.grid(column=3, row=6, padx=(20, 10), pady=20, sticky="ew")

PresionLlegada=Label(text="Presion:", font=("Montserrat", 30, "bold"), fg="#011640")
PresionLlegada.grid(column=3, row=7, padx=(20, 10), pady=20, sticky="ew")

VelocidadVientoLlegada=Label(text="Probabilidad \n de lluvia:", font=("Montserrat", 30, "bold"), fg="#011640")
VelocidadVientoLlegada.grid(column=3, row=8, padx=(20, 10), pady=20, sticky="ew")

Recomendaciones = Label(text="Recomendaciones", font=("Montserrat", 40, "bold"), fg="#011640")
Recomendaciones.grid(column=1, row=9, columnspan=3, pady=(10, 0), sticky="ew")

BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(1, 1)
siguiente = Button(image=BotonRegreso, borderwidth=0)
siguiente.grid(column=1, row=10, columnspan=3, pady=20, sticky="ew")

window.mainloop()