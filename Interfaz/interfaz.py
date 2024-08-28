from tkinter import *

window = Tk()
window.title("Consulta de clima")
window.minsize(width=800, height=800)
window.config(padx=20, pady=20)

lienzo = Canvas(width=200, height=200)
logoaeropuerto = PhotoImage(file="/home/tomas/Documentos/Modelado/Proyecto1-MyP/Interfaz/Recursos/LogoAeropuerto.png")
lienzo.create_image(100, 100, image=logoaeropuerto)
lienzo.grid(column=0, row=0)

titulo1=Label(text="Consulta de clima", font=("Montserrat", 80, "bold"), fg="#011640")
titulo1.grid(column=1, row=0)

titulo1=Label(text="Selecciona tu rool", font=("Montserrat", 65, "bold"), fg="#3CA6A6")
titulo1.grid(column=0, row=2, columnspan=3, pady=(20, 40))

botoncliente = Button(text="Cliente", font=("Montserrat", 40, "bold"), fg="#026773")
botoncliente.grid(column=1, row=3, padx=30, pady=15)

botonpersonal = Button(text="Personal", font=("Montserrat", 40, "bold"), fg="#026773")
botonpersonal.grid(column=1, row=4, padx=30, pady=15)

window.mainloop()