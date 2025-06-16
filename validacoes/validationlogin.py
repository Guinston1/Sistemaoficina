from services import connectdb


def validation_login(login, password):
    connection = connectdb.connectdb()
    cursor = connection.cursor()

    sql = "SELECT * FROM usuarios WHERE login = %s AND password = %s"
    values = (login, password)

    cursor.execute(sql, values)

    results = cursor.fetchone()

    cursor.close()
    connection.close()

    if results:
        print("Successful Login")
        return results
    else:
        return False