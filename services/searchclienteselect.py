from jinja2.lexer import count_newlines
from mysql.connector import Error
from services.connectdb import connectdb


def search_client_select(cpf):
    connection = None
    cursor = None
    try:
        connection = connectdb()
        cursor = connection.cursor()
        query = 'SELECT id_client, first_name, last_name FROM clientes WHERE cpf = %s;'
        values = (cpf,)
        cursor.execute(query, values)

        result = cursor.fetchone()
        print(result)
        return result
    except Error as err:
        print(f'Deu erro {err}')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

