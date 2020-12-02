import openpyxl
import Queries
from datetime import date

def get_users():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "reporte"
    data = Queries.get_users()
    sheet.append(('id', 'nombre', 'rol'))
    for i in data:
        ide = i[0]
        name = i[1]
        role = i[2]
        sheet.append((ide,name, role))
    now = date.today()
    wb.save("reporteusuario"+str(now)+".xlsx")

def get_invoices()
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "reporte"
    data = Queries.get_invoices()
    sheet.append(('id', 'nombre', 'rol'))
    for i in data:
        ide = i[0]
        name = i[1]
        role = i[2]
        sheet.append((ide,name, role))
    now = date.today()
    wb.save("reporteproductos"+str(now)+".xlsx")

def get_invoices()
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "reporte"
    data = Queries.get_invoices()
    sheet.append(('id', 'nombre', 'rol'))
    for i in data:
        ide = i[0]
        name = i[1]
        role = i[2]
        sheet.append((ide,name, role))
    now = date.today()
    wb.save("reporteproductos"+str(now)+".xlsx")
