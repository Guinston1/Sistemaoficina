from services.connectdb import connectdb
from mysql.connector import Error

def save_product(
        codigo,
        nome,
        descricao,
        categoria,
        marca,
        modelo,
        unidade,
        peso,
        altura,
        largura,
        profundidade,
        preco_custo,
        preco_venda,
        estoque,
        estoque_minimo,
        localizacao,
        fornecedor,
        codigo_barras,
        status,
        ncm,
        cest,
        cfop,
        cst_icms,
        csosn,
        origem,
        aliq_icms,
        aliq_pis,
        aliq_cofins,
        aliq_ipi,
        cst_pis,
        cst_cofins,
        cst_ipi,
        unidade_tributavel,
        quantidade_tributavel,
):
    connection = None
    cursor = None
    try:
        connection = connectdb()
        cursor = connection.cursor()

        query = """INSERT INTO produtos (codigo,nome, descricao, categoria, marca, modelo,
        unidade, peso, altura, largura, profundidade, preco_custo, preco_venda, stoque, estoque_minimo,
        localizacao, fornecedor, codigo_barras, status, ncm, cest, cfop, cst_icms, csosn, origem, aliq_icms, aliq_pis, aliq_cofins,
        aliq_ipi,cst_pis,cst_cofins,cst_ipi,unidade_tributavel,quantidade_tributavel)
        VALUES (%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

        values = (codigo,
        nome,
        descricao,
        categoria,
        marca,
        modelo,
        unidade,
        peso,
        altura,
        largura,
        profundidade,
        preco_custo,
        preco_venda,
        estoque,
        estoque_minimo,
        localizacao,
        fornecedor,
        codigo_barras,
        status,
        ncm,
        cest,
        cfop,
        cst_icms,
        csosn,
        origem,
        aliq_icms,
        aliq_pis,
        aliq_cofins,
        aliq_ipi,
        cst_pis,
        cst_cofins,
        cst_ipi,
        unidade_tributavel,
        quantidade_tributavel)

        cursor.execute(query, values)
        connection.commit()

        return True
    except Error as err:
        print(f"Falha ao salvar produto no banco de dados: {err}")
        return False

    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()
            