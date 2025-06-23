from mysql.connector import Error

from services import connectdb


def list_motocycle():

    connection = None
    cursor = None

    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM motocicletas;""")

        results = cursor.fetchall()
        print(results)

        return results
    except Error as err:
        print(f'[ERRO] Falha ao buscar as motos no banco de dados: {err}')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

def savemotodb():
    connection = None,
    cursor = None,

