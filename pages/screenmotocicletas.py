import flet as ft

from componentes import buttons, inputs, texts
from services import searchmotocycle


def screen_list_motos():
    list_motos = ft.ListView(
        expand=True,
        spacing=0,
        padding=0,
        auto_scroll=False
    )

    return list_motos

def add_motos(list_motos):

    dados_motos = searchmotocycle.list_motocycle()

    def update_list(dados_motos, cabecalho):
        list_motos.controls.clear()
        list_motos.controls.append(cabecalho)
        list_motos.update()

        colunas_tabela = ft.Row(
            controls=[

            ]
        )

        for id_moto, marca, modelo, ano, placa, client_Id, data_cadastro in dados_motos:






    text_pesquisar = texts.criar_texto("Pesquisar:",size=14)
    input_pesquisar = inputs.criar_input("",
                height=30,
                border_color='black',
                bgcolor='#2b5e78',
                cursor_height=20,
                hint_text='Placa...',
                content_padding=ft.padding.symmetric(5, 5)
    )

    btn_new_moto = buttons.iconbutton(
                icone=ft.Icons.ADD,
                bgcolor='#397490',
                icon_size=15,
                tooltip='Cadastrar motocicleta'
    )

    cabecalho = ft.Container(
        content=ft.Row(
            controls=[
            text_pesquisar,
            input_pesquisar,
            btn_new_moto
            ],expand=True
        ), expand=True, margin=10
    )

    list_motos.controls.append(cabecalho)
    update_list(dados_motos, cabecalho)