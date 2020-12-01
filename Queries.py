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

# print(login("epareja", "12345"))