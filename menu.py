from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from datetime import date

def intRegister():
	root.destroy()
	import register

def intFacturation():
	root.destroy()
	import facturation

def intGraficos():
	root.destroy()
	import graficos

font1 = ('Bahnschrift Light', 14) 
font = ('Bahnschrift Light', 12)
root = Tk()
root.geometry("330x320+450+100")
root.geometry("500x400+350+100")
root.resizable(False,False)
root.title("Menú")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")

Label(root, text="Menú", font=font1, bg="#c8d6e5", fg="black").place(x=0, y=0, width="500", height="50")
#Buttons
Button(root, text="Registrar", font=font1, command=intRegister, bg="#c8d6e5", fg="black").place(x=30, y=150, width="120", height="50")
Button(root, text="Facturar", font=font1, command=intFacturation, bg="#c8d6e5", fg="black").place(x=190, y=150, width="120", height="50")
Button(root, text="Reportes", font=font1, bg="#c8d6e5", fg="black").place(x=350, y=150, width="120", height="50")
Button(root, text="Salir", font=font, bg="#c8d6e5", fg="black").place(x=420, y=80)
Button(root, text="Gráficos", font=font1, bg="#c8d6e5", fg="black").place(x=30, y=230, width="120", height="50")
root.mainloop()