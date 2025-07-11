from tkinter.constants import HORIZONTAL

import flet as ft
from services.connectdb import connectdb
from componentes.inputs import criar_input
from componentes.buttons import elevated,iconbutton

def product_list_screen():
    product_list = ft.ListView(
        expand=True, spacing=0, padding=0, auto_scroll=False
    )

    return product_list

def product_screen(screen):

    def new_product(e):
        screen.controls.clear()
        screen.controls.append(conteudo_tela_cadastro)
        screen.update()

    def filter_product(e):
        pass

    text_titulo = ft.Text(
        'Cadastro de Produto',
        size=20,
        weight=ft.FontWeight.BOLD
    )



    input_codigo = criar_input(
        label='Código',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_nome = criar_input(
        label='Nome',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_descricao = criar_input(
        label='Descrição',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_categoria = criar_input(
        label='Categoria',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_marca = criar_input(
        label='Marca',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_modelo = criar_input(
        label='Modelo',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_unidade = criar_input(
        label='Unidade',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_peso = criar_input(
        label='Peso',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_altura = criar_input(
        label='Altura',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_largura = criar_input(
        label='Largura',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_profundidade = criar_input(
        label='Profundidade',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_preco_custo = criar_input(
        label='Preço de custo',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_preco_venda = criar_input(
        label='Preço de venda',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_estoque = criar_input(
        label='Qtd estoque',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_estoque_minimo = criar_input(
        label='Estoque minimo',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_localizacao = criar_input(
        label='Localização',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_fornecedor = criar_input(
        label='Fornecedor',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_codigo_barras = criar_input(
        label='Código de barras',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_status = criar_input(
        label='Status',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_ncm = criar_input(
        label='NCM',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cest = criar_input(
        label='CEST',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cfop = criar_input(
        label='CFOP',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cst_icms = criar_input(
        label='ICMS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_csosn = criar_input(
        label='CSOSN',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_origem = criar_input(
        label='Origem',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_aliq_icms = criar_input(
        label='Aliq. ICMS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_aliq_pis = criar_input(
        label='Aliq. PIS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_aliq_cofins = criar_input(
        label='Aliq. COFINS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_aliq_ipi = criar_input(
        label='Aliq. IPI',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cst_pis = criar_input(
        label='CST PIS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cst_cofins = criar_input(
        label='CST COFINS',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_cst_ipi = criar_input(
        label='CST IPI',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_unid_tributavel = criar_input(
        label='Unid. tributável',
        bgcolor='#2b5e78',
        height=30,
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )

    container_coluna1 = ft.Container(
        content=ft.Column(
            controls=[
                text_titulo,
                input_codigo,
                input_nome,
                input_descricao,
                input_categoria,
                input_marca,
                input_modelo,
                input_unidade,
                input_peso,
                input_altura,
                input_largura,
                input_profundidade
            ]
        )
    )

    container_coluna2 = ft.Container(
        content=ft.Column(
            controls=[
                input_preco_custo,
                input_preco_venda,
                input_estoque,
                input_estoque_minimo,
                input_localizacao,
                input_fornecedor,
                input_codigo_barras,
                input_status,
            ]
        )
    )

    container_coluna3 = ft.Container(
        content=ft.Column(
            controls=[
                input_ncm,
                input_cest,
                input_cfop,
                input_cst_icms,
                input_csosn,
                input_origem,
                input_aliq_icms,
            ]
        )
    )

    container_coluna4 = ft.Container(
        content=ft.Column(
            controls=[
                input_aliq_pis,
                input_aliq_cofins,
                input_aliq_ipi,
                input_cst_pis,
                input_cst_cofins,
                input_cst_ipi,
                input_unid_tributavel
            ]
        )
    )

    btn_add_produto = iconbutton(
        icone=ft.Icons.ADD,
        bgcolor='#397490',
        icon_size=15,
        tooltip='Cadastrar serviço',
        on_click=new_product,
    )

    input_pesquisar = criar_input(
        '',
        height=30,
        tooltip='Pesquise por id, código, código de barras, nome, descrição, categoria, marca, modelo.',
        bgcolor='#2b5e78',
        border_color='black',
        cursor_height=20,
        content_padding=ft.padding.symmetric(5, 5),
    )

    text_pesquisar = ft.Text(
        'Pesquisar:'
    )

    cabecalho = ft.Container(
        content=ft.Row(
            controls=[text_pesquisar, input_pesquisar, btn_add_produto
            ],
        ),
        expand=True,
        margin=10
    )

    conteudo_tela_cadastro = ft.Container(
        content=ft.Row(
            controls=[
                container_coluna1,
                container_coluna2,
                container_coluna3,
                container_coluna4
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


    screen.controls.append(cabecalho)
    screen.update()