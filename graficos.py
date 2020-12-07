import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import Queries

def diagram_invoices():
    
    result = Queries.get_invoices()
    productos = []
    sizes = []
	
    for i in result:
        productos.append(i[1])
        sizes.append(i[0])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,  labels=productos, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title("Principales Ventas")
    plt.legend()
    plt.savefig('grafica_pastel.png')
    plt.show()
    
def diagram_productos():
    result = Queries.get_product()
    
    productos = []
    unidades = []
    fig, ax = plt.subplots()
	
    for i in result:
        productos.append(i[2])
        unidades.append(i[4])
    
    ax.set_ylabel('Unidades')
    ax.set_title('Cantidad de productos')
    plt.bar(productos, unidades)
    plt.savefig('barras_simple.png')
    plt.show()

diagram_invoices()