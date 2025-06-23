from datetime import datetime
from time import strftime

from mysql.connector import Error

from services import connectdb


# funcao para salver o cliente no banco de dados
def save_client_db(
    nome,
    last,
    cpf,
    telefone,
    bairro,
    cidade,
    estado,
    endereco,
    marca,
    modelo,
    ano,
    placa,
):
    connection = None
    cursor = None
    try:
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        data_atual = datetime.now().strftime('%d/%m/%Y')

        query = """INSERT INTO clientes (first_name, last_name, cpf, telefone, bairro, cidade,
        estado, endereço, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        values = (
            nome,
            last,
            cpf,
            telefone,
            bairro,
            cidade,
            estado,
            endereco,
            data_atual,
        )

        cursor.execute(query, values)

        id_cliente = cursor.lastrowid
        print(id_cliente)
        if id_cliente:
            try:
                query = """INSERT INTO motocicletas (marca, modelo, ano, placa, cliente_Id, data_cadastro)
                VALUES (%s, %s, %s, %s, %s, %s)"""

                values = (marca, modelo, ano, placa, id_cliente, data_atual)

                cursor.execute(query, values)

                cursor.close()
                connection.commit()
                connection.close()
                return True
            except Error as err:
                print(f'[ERRO] Falha ao cadastrar motocicleta: {err}')
    except Error as err:
        print(f'[ERRO] Falha ao cadastrar o cliente: {err}')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


def motosave(id_client, marca, modelo, ano, placa):
    """Função para salvar o cadastro da motocicleta no banco de dados."""

    connection = None
    cursor = None

    try:

        print(f'{id_client}')
        connection = connectdb.connectdb()
        cursor = connection.cursor()

        data_atual = datetime.now().strftime('%d/%m/%Y')

        query = """INSERT INTO motocicletas (marca, modelo, ano, placa, cliente_Id, data_cadastro)
                    VALUES (%s, %s, %s, %s, %s, %s);"""

        values = (marca, modelo, ano, placa, id_client, data_atual)

        cursor.execute(query, values)
        connection.commit()

        return True

    except Error as err:
        print(f'[ERRO] Falha ao salvar a motocicleta no banco de dados: {err}')

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()
