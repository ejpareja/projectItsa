from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk
import Queries
global datos


def save_DB():
	insertInvoices = Queries.create_invoice(productID_.get(), quantity.get(), unityValue.get(), total.get(), clientname.get(), clientID.get(), quantity_.get())

def fun_total():
	if int(quantity.get()) > int(quantity_.get()):
		messagebox.showerror(title="Error", message="La cantidad de unidades no puede ser mayor a las existencias.")
		quantity.set("")
	else:
		total.set(quantity.get() * unityValue.get())

def onChangeValue(object):
    value = str(combox.current())
    n = list_prices[int(value)]
    unityValue.set(n)
    datos = list_unities[int(value)] 
    quantity_.set(datos)
    ides = list_ids[int(value)]
    productID_.set(ides)


invoice = Queries.secuencia()
products = Queries.get_product()

list_ids = []
list_products = []
list_prices = []
list_unities = []
for x in products:
	list_products.append(x[1])
	list_prices.append(x[6])
	list_unities.append(x[4])
	list_ids.append(x[0])


font = ('Bahnschrift Light', 14) 
root = Tk()
root.geometry("760x400+300+100")
root.resizable(False,False)
root.title("Facturar")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")

quantity_ = IntVar()
Label(root, text="Cantidad:", font=font,bg="#222f3e", fg="white")
Entry(root, textvariable=quantity_, font=font,bg="#c8d6e5")

productID_ = StringVar()
Label(root, text="Identificación Cliente:", font=font,bg="#222f3e", fg="white")
Entry(root, textvariable=productID_, font=font,bg="#c8d6e5")

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
consecutive = invoice
Label(root, text="Consecutivo de Factura:", font=font,bg="#222f3e", fg="white").place(x=370, y=120)
Entry(root, textvariable=consecutiveInvoice, font=font,bg="#c8d6e5", state="readonly").place(x=370, y=160, width="360")
consecutiveInvoice.set(consecutive)
#Reference
Label(root, text="Referencia:", font=font,bg="#222f3e", fg="white").place(x=30, y=200)
combox = ttk.Combobox(root, font=font, state="readonly")
combox.place(x=30, y=240)
combox['values'] = list_products
combox.bind("<<ComboboxSelected>>", onChangeValue)
#Quantity
quantity = IntVar()
Label(root, text="Cantidad:", font=font,bg="#222f3e", fg="white").place(x=300, y=200)
Entry(root, textvariable=quantity, font=font,bg="#c8d6e5").place(x=300, y=240, width="100")
#UnityValue
unityValue = IntVar()
Label(root, text="Valor Unidad:", font=font,bg="#222f3e", fg="white").place(x=440, y=200)
Entry(root, textvariable=unityValue, font=font,bg="#c8d6e5", state="readonly").place(x=440, y=240, width="100")
#Total
total = IntVar()
Label(root, text="Total:", font=font,bg="#222f3e", fg="white").place(x=580, y=200)
Entry(root, textvariable=total, font=font,bg="#c8d6e5", state="readonly").place(x=580, y=240, width="150")
#Button
Button(root, text="Calcular Total", font=font, command=fun_total,bg="#c8d6e5", fg="black").place(x=440, y=290)
Button(root, text="Guardar", font=font, command=save_DB,bg="#c8d6e5", fg="black").place(x=300, y=290)

root.mainloop()