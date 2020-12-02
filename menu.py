from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
global name 
global ide
global role

def meMain(data):
	for i in data:
		ide = i[0]
		name = i[1]
		role = i[2]
	print(ide, name, role)
	loadInt(ide, name, role)

def intRegister():
	root.destroy()
	import register.py
def intFacturation():
	root.destroy()
	import facturation.py

def loadInt(name, ide, role):
	font1 = ('Bahnschrift Light', 14) 
	font = ('Bahnschrift Light', 12)
	root = Tk()
	root.geometry("500x400+350+100")
	root.resizable(False,False)
	root.title("Menú")
	root.iconbitmap('presupuesto.ico')
	root.config(bg="#222f3e")

	Label(root, text="Menú", font=font1, bg="#c8d6e5", fg="black").place(x=0, y=0, width="500", height="50")
	#Data
	Label(root, text=ide, font=font, bg="#222f3e", fg="white").place(x=30, y=80)
	Label(root, text=name, font=font, bg="#222f3e", fg="white").place(x=130, y=80)
	Label(root, text=role, font=font, bg="#222f3e", fg="white").place(x=250, y=80)
	#Buttons
	Button(root, text="Registrar", font=font1, command=intRegister, bg="#c8d6e5", fg="black").place(x=30, y=150, width="120", height="50")
	Button(root, text="Facturar", font=font1, command=intFacturation, bg="#c8d6e5", fg="black").place(x=190, y=150, width="120", height="50")
	Button(root, text="Reportes", font=font1, bg="#c8d6e5", fg="black").place(x=350, y=150, width="120", height="50")
	Button(root, text="Salir", font=font, bg="#c8d6e5", fg="black").place(x=420, y=80)
	root.mainloop()