from mysql.connector import Error

from services import connectdb


def search_services():
    connection = None
    cursor = None
    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM servicos;')

        results = cursor.fetchall()
        print(results)

        return results
    except Error as Err:
        print(f'[ERRO] Falha ao buscar os serviços no banco de dados: {Err}')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()
