from tkinter import *
import matplotlib
from PIL import Image, ImageTk
from tkinter import messagebox

ventana = Tk()
ventana.geometry("850x200")
ventana.title("Predicción del Recurso Eólico disponible")
labelA=Label(ventana, text="UNIVERSIDAD FRANCISCO DE PAULA SANTANDER")
labelB=Label(ventana, text="PROGRAMA DE INGENIERÍA ELECTRÓNICA")
labelC=Label(ventana, text="INTERFAZ DE USUARIO")
label=Label(ventana, text="SELECCIONE LA ZONA")
label.place(x="380",y="120")
labelA.place(x="300",y="10")
labelB.place(x="330",y="40")
labelC.place(x="380",y="70")

img=Image.open('logoufps.png')
new_img=img.resize((180,130))
render=ImageTk.PhotoImage(new_img)
img1=Label(ventana, image=render)
img1.image=render
img1.place(x="10", y="10")

img2=Image.open('selloa.png')
new_img=img2.resize((100,100))
render=ImageTk.PhotoImage(new_img)
imgB=Label(ventana, image=render)
imgB.image=render
imgB.place(x="700", y="35")


def aeropuerto():
    ventana2=Toplevel()
    ventana2.geometry("850x700")
    ventana2.title("A E R O P U E R T O")
    label=Label(ventana2, text="A E R O P U E R T O")
    label.place(x="350",y="30")
    label1=Label(ventana2, text="PERFIL VERTICAL DEL VIENTO")
    label2=Label(ventana2, text="PREDICCIÓN PARA 1 AÑO")
    label3=Label(ventana2, text="ÉPOCAS VS MAE")
    label4=Label(ventana2, text="RESULTADOS")
    label1.place(x="130", y="70")
    label2.place(x="540", y="70")
    label3.place(x="160", y="370")
    label4.place(x="590", y="370")


    img=Image.open('1AERO.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana2, image=render)
    img1.image=render
    img1.place(x="10", y="100")

    img=Image.open('2AERO.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana2, image=render)
    img1.image=render
    img1.place(x="450", y="100")

    img=Image.open('3AERO.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana2, image=render)
    img1.image=render
    img1.place(x="10", y="400")

    img=Image.open('4AERO.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana2, image=render)
    img1.image=render
    img1.place(x="450", y="400")

def ceiba():
    ventana3=Toplevel()
    ventana3.geometry("850x700")
    ventana3.title("C E I B A")
    label=Label(ventana3, text="C E I B A ")
    label.place(x="350",y="30")
    label1=Label(ventana3, text="PERFIL VERTICAL DEL VIENTO")
    label2=Label(ventana3, text="PREDICCIÓN PARA 10 MINUTOS")
    label3=Label(ventana3, text="ÉPOCAS VS MAE")
    label4=Label(ventana3, text="RESULTADOS")
    label1.place(x="130", y="70")
    label2.place(x="540", y="70")
    label3.place(x="160", y="370")
    label4.place(x="590", y="370")


    img=Image.open('perfil viento CEIBA.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana3, image=render)
    img1.image=render
    img1.place(x="10", y="100")

    img=Image.open('predCEIBA.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana3, image=render)
    img1.image=render
    img1.place(x="450", y="100")

    img=Image.open('errorCEIBA.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana3, image=render)
    img1.image=render
    img1.place(x="10", y="400")

    img=Image.open('resultados.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana3, image=render)
    img1.image=render
    img1.place(x="450", y="400")

def torcoroma():
    ventana4=Toplevel()
    ventana4.geometry("850x700")
    ventana4.title("T O R C O R O M A")
    label=Label(ventana4, text="T O R C O R O M A")
    label.place(x="350",y="30")
    label1=Label(ventana4, text="PERFIL VERTICAL DEL VIENTO")
    label2=Label(ventana4, text="PREDICCIÓN PARA 10 MINUTOS")
    label3=Label(ventana4, text="ÉPOCAS VS MAE")
    label4=Label(ventana4, text="RESULTADOS")
    label1.place(x="130", y="70")
    label2.place(x="540", y="70")
    label3.place(x="160", y="370")
    label4.place(x="590", y="370")


    img=Image.open('1TORC.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana4, image=render)
    img1.image=render
    img1.place(x="10", y="100")

    img=Image.open('2TORC.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana4, image=render)
    img1.image=render
    img1.place(x="450", y="100")

    img=Image.open('3TORC.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana4, image=render)
    img1.image=render
    img1.place(x="10", y="400")

    img=Image.open('4TORC.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana4, image=render)
    img1.image=render
    img1.place(x="450", y="400")

def belen():
    ventana5=Toplevel()
    ventana5.geometry("850x700")
    ventana5.title("B E L E N")
    label=Label(ventana5, text="B E L E N")
    label.place(x="350",y="30")
    label1=Label(ventana5, text="PERFIL VERTICAL DEL VIENTO")
    label2=Label(ventana5, text="PREDICCIÓN PARA 10 MINUTOS")
    label3=Label(ventana5, text="ÉPOCAS VS MAE")
    label4=Label(ventana5, text="RESULTADOS")
    label1.place(x="130", y="70")
    label2.place(x="540", y="70")
    label3.place(x="160", y="370")
    label4.place(x="590", y="370")


    img=Image.open('1BELEN.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana5, image=render)
    img1.image=render
    img1.place(x="10", y="100")

    img=Image.open('2BELEN.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana5, image=render)
    img1.image=render
    img1.place(x="450", y="100")

    img=Image.open('3BELEN.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana5, image=render)
    img1.image=render
    img1.place(x="10", y="400")

    img=Image.open('4BELEN.jpg')
    new_img=img.resize((340,230))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana5, image=render)
    img1.image=render
    img1.place(x="450", y="400")

boton1=Button(ventana, text="ZONA 1: AEROPUERTO", command=aeropuerto)
boton1.pack()
boton2=Button(ventana, text="ZONA 2: CEIBA", command=ceiba)
boton2.pack()
boton3=Button(ventana, text="ZONA 3: TORCOROMA", command=torcoroma)
boton3.pack()
boton4=Button(ventana, text="ZONA 4: BELEN", command=belen)
boton4.pack()

boton1.place(x="150",y="160")
boton2.place(x="320",y="160")
boton3.place(x="440",y="160")
boton4.place(x="600",y="160")

ventana.mainloop()

