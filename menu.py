from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from datetime import date


def intRegister(root):
	root.destroy()
	import register.py
def intFacturation():
	root.destroy()
	import facturation.py

def load_interface(name, ide, role):
	date_now = date.today()
	font1 = ('Bahnschrift Light', 14) 
	font = ('Bahnschrift Light', 12)
	root = Tk()
	root.geometry("330x320+450+100")
	root.resizable(False,False)
	root.title("Menú")
	root.iconbitmap('presupuesto.ico')
	root.config(bg="#222f3e")

	
	
	Label(root, text="Menú", font=font1, bg="#c8d6e5", fg="black").place(x=0, y=0, width="330", height="50")
	#RegisterWindow
	Label(root, text=name, font=font, bg="#222f3e", fg="white").place(x=30, y=80)
	Label(root, text="1. Registrar Usuario:", font=font, bg="#222f3e", fg="white").place(x=30, y=100)
	Button(root, text="Click Aquí", font=font, command=intRegister(root),bg="#c8d6e5", fg="black").place(x=210, y=75)
	#FacturationWindow
	Label(root, text="2. Facturar:", font=font,bg="#222f3e", fg="white").place(x=30, y=130)
	Button(root, text="Click Aquí", font=font, command=intFacturation(root),bg="#c8d6e5", fg="black").place(x=210, y=125)
	print(name, ide, role)
	root.mainloop()
