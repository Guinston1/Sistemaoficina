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

def save_service(nome, tempo, descricao, preco):
    connection = None
    cursor = None
    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        query = """INSERT INTO servicos (nome, duracao_estimada, descricao, preco)
         VALUES (%s, %s, %s,%s);"""

        values = (nome, tempo, descricao, preco)

        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as err:
        print(f"[ERRO] falha ao salvar serviço no banco de dados: {err}")

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

