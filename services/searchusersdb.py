from mysql.connector import Error

from services import connectdb


# funcao para conectar no banco de dados e buscar usuarios
def users_search_db():
    connection = None
    cursor = None
    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        query = """SELECT id_usuario, nome, login, tipo_usuario, loja, status 
                FROM usuarios;"""

        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        print(results)

        return results
    except Error as err:
        print(f'[ERRO] Falha ao cadastrar usuário: {err}')
        return False

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
