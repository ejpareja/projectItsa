import mysql.connector 
def connection() :

    dbQ = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="itpe"
    ) 
    return dbQ

def login(user, passw) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT u.id AS iduser, u.nombre AS nomuser, \
        r.nombre AS rol from usuarios u \
        INNER JOIN roles r ON u.rol = r.id  WHERE usuario = %s AND contrasena = %s AND u.estado = %s "
    argument = (user, passw, 'A')
    cursor.execute(sql, argument)
    response = cursor.fetchone()
    dbQ.close()
    return response

def create_user(id, name, user, passw, role) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "INSERT INTO usuarios (id,nombre,usuario,contrasena,rol,estado) VALUES (%s,%s,%s,%s,%s,%s)"
    argument = (id, name, user, passw,role, 'A')
    cursor.execute(sql,argument)
    dbQ.commit()
    response = cursor.rowcount
    dbQ.close()
    return response
    
def get_users() :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT u.id AS iduser, u.nombre AS nomuser, r.nombre AS role from usuarios u INNER JOIN roles r ON u.rol = r.id  WHERE u.estado = 'A'"
    cursor.execute(sql,)
    results =  cursor.fetchall()
    dbQ.close()
    return results

def delete_user(id) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "UPDATE usuarios SET estado = 'I' WHERE id = %s"
    args = (id)
    cursor.execute(sql, args)
    response = cursor.rowcount
    dbQ.close()
    return response


def create_role(id,name) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "INSERT INTO roles (id, nombre, estado) VALUES (%s,%s,%s) "  
    args = (int(id), name, 'A')
    cursor.execute(sql, args)
    print(cursor.rowcount)
    dbQ.commit() 

def get_roles() :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT id, nombre, estado FROM roles WHERE u.estado = 'A'"
    cursor.execute(sql)
    results =  cursor.fetchall()
    dbQ.close()
    return results

def get_roles_ids() :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT id, nombre WHERE u.estado = 'A' AND "
    cursor.execute(sql)
    results =  cursor.fetchall()
    dbQ.close()
    return results


def delete_role(id) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "UPDATE roles SET estado = 'I' WHERE id = %s"
    args = (id)
    cursor.execute(sql, args)
    response = cursor.rowcount
    dbQ.close()
    return response

def crete_product(id, reference, name, description, unit, price_buy, price_sale) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "INSERT INTO productos (id, referencia, nombre, descripcion, unidad, precio_compra, precio_venta, fechadecompra) VALUES (%s,%s,%s,%s,%s,%s,%s,'LOCALTIMESTAMP')"
    argument = (id, reference, name, description, unit, price_buy, price_sale)
    cursor.execute(sql,argument)
    dbQ.commit()
    response = cursor.rowcount
    dbQ.close()
    return response
    
def get_product() :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT id, referencia, nombre, descripcion, unidad, precio_compra, precio_venta FROM productos"
    cursor.execute(sql)
    results =  cursor.fetchall()
    dbQ.close()
    return results

def get_product_ids(type_filter, filter) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT id, referencia, nombre FROM productos"
    if filter == "nombre" :
        sql += "WHERE nombre LIKE %s"
    elif filter == "id" :
            sql += "WHERE id LIKE %s"
    else :
         sql += "WHERE nombre LIKE %s"
    args = ("%"+ filter + "%")
    cursor.execute(sql, args)
    results =  cursor.fetchall()
    return results

def get_price(reference) :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT precio_venta FROM productos WHEREE reference = %s"
    args = (reference)
    cursor.execute(sql)
    results =  cursor.fetchone()
    return results

def get_invoices() :
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT COUNT(*) as cantidad, p.referencia FROM ventas v INNER JOIN productos p on (v.id_producto = p.id)"
    cursor.execute(sql)
    results =  cursor.fetchall()
    return results

def secuencia():
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'itpe' AND   TABLE_NAME   = 'ventas';"
    cursor.execute(sql)
    response = cursor.fetchone()
    dbQ.close()
    return response[0]

def create_invoice(id, quantity, unit_value, total_value, name_client, id_client, unit_previous):
    result = False
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "INSERT INTO ventas (id_producto, cantidad, valor_unidad, valor_total, nombre_cliente, id_cliente, fechaventa)  VALUES (%s,%s,%s,%s,%s,%s,'LOCALTIMESTAMP') "
    argument = (id, quantity, unit_value, total_value, name_client, id_client)
    cursor.execute(sql,argument)
    dbQ.commit()
    response = cursor.rowcount
    print(response)
    dbQ.close()
    if response == 1:
        unit = unit_previous - unit_value
        res = udpate_producto(id,unit)
        if res == 1:
            return True
        else:
            return False
    else:
        return False

def udpate_producto(id,unit):
    dbQ = connection()
    cursor = dbQ.cursor()
    sql = "UPDATE productos SET unidad = %s WHERE id = %s"
    argument = (int(unit), id)
    cursor.execute(sql,argument)
    dbQ.commit()
    response = cursor.rowcount
    dbQ.close()
    return response