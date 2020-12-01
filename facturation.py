from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk

def fun_total():
	total.set(quantity.get() * unityValue.get())

font = ('Bahnschrift Light', 14) 
root = Tk()
root.geometry("760x400+300+100")
root.resizable(False,False)
root.title("Registrar Usuario")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")
#Name
clientname = StringVar()
Label(root, text="Nombre Cliente:", font=font,bg="#222f3e", fg="white").place(x=30, y=40)
Entry(root, textvariable=clientname, font=font,bg="#c8d6e5").place(x=30, y=80, width="700")
#ID
clientID = StringVar()
Label(root, text="Identificación Cliente:", font=font,bg="#222f3e", fg="white").place(x=30, y=120)
Entry(root, textvariable=clientID, font=font,bg="#c8d6e5").place(x=30, y=160, width="300")
#Consecutive invoice
consecutiveInvoice = StringVar()
Label(root, text="Consecutivo de Factura:", font=font,bg="#222f3e", fg="white").place(x=370, y=120)
Entry(root, textvariable=consecutiveInvoice, font=font,bg="#c8d6e5").place(x=370, y=160, width="360")
#Reference
Label(root, text="Referencia:", font=font,bg="#222f3e", fg="white").place(x=30, y=200)
combox = ttk.Combobox(root, font=font, state="readonly")
combox.place(x=30, y=240)
opciones = ['opcion 1', 'opcion 2', 'opcion 3']
combox['values'] = opciones
#Quantity
quantity = IntVar()
Label(root, text="Cantidad:", font=font,bg="#222f3e", fg="white").place(x=300, y=200)
Entry(root, textvariable=quantity, font=font,bg="#c8d6e5").place(x=300, y=240, width="100")
#UnityValue
unityValue = IntVar()
Label(root, text="Valor Unidad:", font=font,bg="#222f3e", fg="white").place(x=440, y=200)
Entry(root, textvariable=unityValue, font=font,bg="#c8d6e5").place(x=440, y=240, width="100")
#Total
total = IntVar()
Label(root, text="Total:", font=font,bg="#222f3e", fg="white").place(x=580, y=200)
Entry(root, textvariable=total, font=font,bg="#c8d6e5", state="readonly").place(x=580, y=240, width="150")
#Button
Button(root, text="Calcular Total", font=font, command=fun_total,bg="#c8d6e5", fg="black").place(x=440, y=280)
root.mainloop()