from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def db_Register():
	empty = emptyFields()
	if empty == 1:
		messagebox.showerror(title="Error", message="Error, no deben haber campos vacíos.")
	else:
		date_time = datetime.now()
		mydb = mysql.connector.connect(
			host = "localhost",
			user="root",
			password="",
			database="itpe")
		cursor = mydb.cursor()
		sql = "INSERT INTO productos (id, referencia, nombre, descripcion, unidad, precio_compra, precio_venta, fechadecompra) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)"
		values = (id_product.get(), reference.get(), name.get(), description.get(), unity.get(), buyprice.get(), saleprice.get(), date_time)
		
		cursor.execute(sql, values)
		mydb.commit()

		messagebox.showinfo(title="Registro exitoso", message="Registro Exitoso.")

def emptyFields():
	if id_product.get() == "" or reference.get() =="" or name.get() == "" or description.get() == "" or unity.get() =="" or buyprice.get() == "" or saleprice.get() == "":
		return 1

font = ('Bahnschrift Light', 14) 
img_ubi = 'usuario.png'
root = Tk()
root.geometry("570x380+360+100")
root.resizable(False,False)
root.title("Login")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")

Label(root, text="Registrar Productos", font=font, bg="#c8d6e5", fg="black").place(x=0, y=0, width="570", height="50")
#id
id_product = StringVar()
Label(root, text="ID Producto:", font=font, bg="#222f3e", fg="white").place(x=40, y=70)
Entry(root, textvariable=id_product, font=font, bg="#c8d6e5").place(x=40, y=100)
#reference
reference = StringVar()
Label(root, text="Referencia Producto:", font=font, bg="#222f3e", fg="white").place(x=300, y=70)
Entry(root, textvariable=reference, font=font, bg="#c8d6e5").place(x=300, y=100)
#name
name = StringVar()
Label(root, text="Nombre Producto:", font=font, bg="#222f3e", fg="white").place(x=40, y=140)
Entry(root, textvariable=name, font=font, bg="#c8d6e5").place(x=40, y=170)
#description
description = StringVar()
Label(root, text="Descripción Producto:", font=font, bg="#222f3e", fg="white").place(x=300, y=140)
Entry(root, textvariable=description, font=font, bg="#c8d6e5").place(x=300, y=170)
#unity
unity = StringVar()
Label(root, text="Unidades Producto:", font=font, bg="#222f3e", fg="white").place(x=40, y=210)
Entry(root, textvariable=unity, font=font, bg="#c8d6e5").place(x=40, y=240, width="60")
#buyprice
buyprice = StringVar()
Label(root, text="Precio Compra:", font=font, bg="#222f3e", fg="white").place(x=230, y=210)
Entry(root, textvariable=buyprice, font=font, bg="#c8d6e5").place(x=230, y=240, width="60")
#saleprice
saleprice = StringVar()
Label(root, text="Precio Venta:", font=font, bg="#222f3e", fg="white").place(x=390, y=210)
Entry(root, textvariable=saleprice, font=font, bg="#c8d6e5").place(x=390, y=240, width="60")
#button
Button(root, text="Registrar Producto", font=font, bg="#c8d6e5", fg="black", command=db_Register).place(x=280, y=300)
Button(root, text="Volver", font=font, bg="#c8d6e5", fg="black").place(x=170, y=300)
root.mainloop()