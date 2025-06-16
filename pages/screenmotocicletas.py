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
                ft.Container(
                    ft.Text('ID', size=14, weight=ft.FontWeight.BOLD),
                    width=50,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('MARCA', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center_left,
                ),
                ft.Container(
                    ft.Text('MODELO', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    width=120,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('ANO', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    width=100,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('PLACA', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    width=100,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('ID PROPRIETÁRIO', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    width=70,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('CADASTRO', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    width=70,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('', weight=ft.FontWeight.BOLD),
                    width=50,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
            ],
            spacing=0,
        )
        list_motos.controls.append(colunas_tabela)

        for id_moto, marca, modelo, ano, placa,cliente_Id, data_cadastro in dados_motos:
            line = ft.Container(
                padding=0,
                border_radius=5,
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(id_moto),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            bgcolor='#1c4861',
                            width=50,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(
                                marca, weight=ft.FontWeight.BOLD, size=12
                            ),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center_left,
                        ),
                        ft.Container(
                            content=ft.Text(modelo, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=120,
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(ano, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=100,
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(placa, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=100,
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(
                                cliente_Id, weight=ft.FontWeight.BOLD, size=12
                            ),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center_left,
                        ),
                        ft.Container(
                            content=ft.Text(data_cadastro, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=70,
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.HISTORY,
                                height=20,
                                icon_size=15,

                                tooltip='Histórico',
                                data=id_moto,
                                bgcolor='#1c4861',
                                on_click=lambda e: print(
                                    f'Histórico {e.control.data}'
                                ),
                            ),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=50,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
            )
            list_motos.controls.append(line)
        list_motos.update()







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