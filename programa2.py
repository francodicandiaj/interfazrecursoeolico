from tkinter import *

ventana=Tk()
ventana.geometry("700x500")

texto_zona=Entry(ventana, font=("Courier", 20, "normal"), justify="center")
texto_zona.pack(padx=30, pady=30)

obtener_prediccion=Button(ventana, text="Zona 1",font=("Courier", 20, "normal"))
obtener_prediccion.pack()
obtener_prediccion=Button(ventana, text="Zona 2",font=("Courier", 20, "normal"))
obtener_prediccion.pack()
obtener_prediccion=Button(ventana, text="Zona 3",font=("Courier", 20, "normal"))
obtener_prediccion.pack()

mostrar_prediccion=Label(text="Recurso Eólico", font=("Courier",20,"normal"))
mostrar_prediccion.pack(padx=10, pady=10)


ventana.mainloop()