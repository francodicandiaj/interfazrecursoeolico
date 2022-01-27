from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana=Tk()
ventana.geometry("900x700")
ventana.wm_title("ZONA 1: CEIBA")

frame=Frame(ventana, bg='green')
frame.grid(column=0,row=0,sticky="nsew")

x=[1,2,3,4,5,6,7,8,9,10]
yr=[1.471049,1.484255,1.751918,1.241942,1.44689,1.782367,1.24733,1.323103,1.509383,1.150576]
yp=[1.384595,1.23438,1.6665,1.158126,1.362038,1.70554,1.166464,1.236547,1.430105,1.06651] 

fig,