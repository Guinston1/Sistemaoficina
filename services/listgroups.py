from asyncio import current_task

from mysql.connector import Error

from services import connectdb


#funcao para buscar a lista de grupos no banco de dados
def searchlistgroups():
    connection = None
    cursor = None

    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        query = """SELECT nome FROM grupos WHERE id_group > 0;"""
        cursor.execute(query)


        results = cursor.fetchall()
        for linha in results:
            print(linha)
        return results

    except Error as err:
        print(f"[ERRO] Search for groups failed? {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
