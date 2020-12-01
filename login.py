from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar
from tkinter import messagebox
import Queries


def next_int():
	inf = get_Information()
	if inf == None:
		messagebox.showerror(title="Error", message="Error, verifique su usuario o contraseña.")
	elif inf != None :
		root.destroy()
		import menu
		menu.meMain(inf)

def get_Information():
	result = None
	user = username.get()
	passw = password.get()
	if user == "" or passw == "":
		return result
	else:
		result = Queries.login(user, passw)
		if result != None:
			return result
		elif result == None:
			return result

font = ('Bahnschrift Light', 11) 
img_ubi = 'usuario.png'
root = Tk()
root.geometry("350x360+460+100")
root.resizable(False,False)
root.title("Login")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")
#Imagen
img = ImageTk.PhotoImage(Image.open(img_ubi))
Label(root, image = img, bg="#222f3e").place(x=110, y=40)
#User
username = StringVar()
Label(root, text="Usuario:", font=font, bg="#222f3e", fg="white").place(x=40, y=195)
Entry(root, textvariable=username, font=font, bg="#c8d6e5").place(x=140, y=195)
#Pass
password = StringVar()
Label(root, text="Contraseña:", font=font, bg="#222f3e", fg="white").place(x=40, y=235)
Entry(root, textvariable=password, font=font, bg="#c8d6e5", show="●").place(x=140, y=235)
#Button
Button(root, text="Ingresar", font=font, bg="#c8d6e5", fg="black", command=next_int).place(x=140, y=280)
root.mainloop()