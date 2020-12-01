from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

font = ('Bahnschrift Light', 14) 
root = Tk()
root.geometry("500x500+450+100")
root.resizable(False,False)
root.title("Usuarios")
root.iconbitmap('presupuesto.ico')
root.config(bg="#222f3e")

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="#c8d6e5", font=font)

my_tree = ttk.Treeview(root, style="BW.TLabel")
my_tree['columns'] = ("ID", "NOMBRE", "ROL" )
my_tree.column("#0", width=0, minwidth=25)
my_tree.column("ID", anchor=W, width=120)
my_tree.column("NOMBRE", anchor=CENTER, width=80)
my_tree.column("ROL", anchor=W, width=120)

my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
my_tree.heading("ROL", text="ROL", anchor=W)

# data = get_user()
# cont = 0
# for i in data :
#     my_tree.insert(parent='', index='end', iid=cont, text="", values=(i[0], i[1], i[2]))
#     cont +=1

my_tree.pack(pady=20)

root.mainloop()