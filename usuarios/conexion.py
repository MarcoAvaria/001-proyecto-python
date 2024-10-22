import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="127.0.0.1",
        user="soporte",
        passwd='soporte',
        database="master_python",
        port=3306
    )
    cursor = database.cursor(buffered=True)
    
    return [database, cursor]