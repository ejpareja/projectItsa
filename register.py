from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar
from tkinter import messagebox

def register():
	fields = emptyFields()
	if fields == 0:
		messagebox.showerror(title="Error",message="No deben haber campos vacios.")
	else:
		verifyPassword()
		clear()
	# root.destroy()
	# import login.py
def verifyPassword():
	emptyFields()
	pass1 = password.get()
	pass2 = verify_password.get()
	if pass1 != pass2:
		messagebox.showerror(title="Error", message="Las contraseñas no coinciden.")
	else:
		if len(pass1) <8:
			messagebox.showerror(title="Error", message="La contraseña debe tener minimo 8 caracteres.")
		else:
			messagebox.showinfo(title="Registro exitoso", message="Registro exitoso.")
def emptyFields():
	if identification.get()=="" or fullname.get()=="" or username.get() == "" or password.get() == "" or verify_password.get() == "":
		if admin.get() == 0 and billing.get() == 0:
			return 0
def clear():
	identification.set("")
	fullname.set("")
	username.set("")
	password.set("")
	verify_password.set("")
	admin.set(0)
	billing.set(0)
font = ('Bahnschrift Light', 11) 
root = Tk()
root.geometry("440x310+460+100")
root.resizable(False,False)
root.title("Registrar Usuario")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")
#id
identification = StringVar()
Label(root, text="Identificación:", font=font,bg="#222f3e", fg="white").place(x=30, y=30)
Entry(root, font=font, textvariable=identification, bg="#c8d6e5").place(x=30, y=60)
#fullname
fullname = StringVar()
Label(root, text="Nombre Completo:", font=font, bg="#222f3e", fg="white").place(x=220, y=30)
Entry(root, font=font, textvariable=fullname, bg="#c8d6e5").place(x=220, y=60)
#user
username = StringVar()
Label(root, text="Nombre Usuario:", font=font, bg="#222f3e", fg="white").place(x=30, y=100)
Entry(root, font=font, textvariable=username, bg="#c8d6e5").place(x=30, y=130)
#password
password = StringVar()
Label(root, text="Contraseña", font=font, bg="#222f3e", fg="white").place(x=220, y=100)
Entry(root, font=font, textvariable=password, bg="#c8d6e5", show="●").place(x=220, y=130)
#verifypass
verify_password = StringVar()
Label(root, text="Confirmar Contraseña:", font=font, bg="#222f3e", fg="white").place(x=30, y=170)
Entry(root, font=font, textvariable=verify_password, bg="#c8d6e5", show="●").place(x=30, y=200)
#Rol
admin = IntVar()
billing = IntVar()
Label(root, text="Rol:", font=font, bg="#222f3e", fg="white").place(x=220, y=170)
Checkbutton(root, text="Administrador", variable=admin, font=font, bg="#222f3e", fg="black").place(x=260, y=170)
Checkbutton(root, text="Facturador", variable=billing, font=font, bg="#222f3e", fg="black").place(x=260, y=200)
#button
Button(root, text="Registrar", font=font, bg="#c8d6e5", fg="black", command=register).place(x=160, y=250)
root.mainloop()