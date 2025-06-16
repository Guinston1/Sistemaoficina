from mysql.connector import Error

from services import connectdb


def user_salve(name, user, password, group, store):
    connection = None
    cursor = None

    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        query = """INSERT INTO usuarios (nome, login, password, tipo_usuario, loja)
            VALUES (%s, %s, %s, %s, %s);"""

        values = (name, user, password, group, store)

        cursor.execute(query, values)
        connection.commit()

        print('user registered successfully')
        return True

    except Error as err:
        print(f'[ERRO] failed to register user: {err}')
        return False

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
