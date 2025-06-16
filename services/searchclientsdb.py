from mysql.connector import Error

from services import connectdb


# funcao para buscar os clientes cadastrados
def search_clients():
    connection = None
    cursor = None

    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        query = """SELECT * FROM clientes 
                WHERE id_client > 0;"""

        cursor.execute(query)

        results = cursor.fetchall()
        print(results)

        return results
    except Error as err:
        print('[ERRO] Failed to fetch customers from database: erro {err} ')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()
