import flet as ft

from componentes import buttons, inputs, texts
from services import connectdb, searchservices


def screen_list_services():
    list_services = ft.ListView(
        expand=True, spacing=0, padding=0, auto_scroll=False
    )

    return list_services


def add_services(list_services):
    dados_services = searchservices.search_services()

    def atualizar_lista(services, cabecalho):
        list_services.controls.clear()
        list_services.update()

        colunas = ft.Row(
            controls=[
                ft.Container(
                    ft.Text('ID', size=14, weight=ft.FontWeight.BOLD),
                    width=50,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('NOME', size=14, weight=ft.FontWeight.BOLD),
                    width=200,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center_left,
                ),
                ft.Container(
                    ft.Text('TEMPO', size=14, weight=ft.FontWeight.BOLD),
                    width=70,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('DESCRICAO', size=14, weight=ft.FontWeight.BOLD),
                    expand=True,
                    border=ft.border.all(1, 'black'),
                    bgcolor='#0e3249',
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text('PREÇO', size=14, weight=ft.FontWeight.BOLD),
                    width=100,
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
        list_services.controls.append(cabecalho)
        list_services.controls.append(colunas)

        for id_service, nome, tempo, descricao, preco in services:
            line = ft.Container(
                padding=0,
                border_radius=5,
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(id_service),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            bgcolor='#1c4861',
                            width=50,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(
                                nome, weight=ft.FontWeight.BOLD, size=12
                            ),
                            padding=1,
                            width=200,
                            border=ft.border.all(1, 'black'),
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center_left,
                        ),
                        ft.Container(
                            content=ft.Text(tempo, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=70,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(descricao, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            expand=True,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(preco, size=12),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=100,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.EDIT,
                                height=20,
                                icon_size=15,
                                tooltip='Histórico',
                                data=id_service,
                                bgcolor='#1c4861',
                                on_click=lambda e: print(
                                    f'Editar serviço {e.control.data}'
                                ),
                            ),
                            padding=1,
                            border=ft.border.all(1, 'black'),
                            width=50,
                            bgcolor='#1c4861',
                            alignment=ft.alignment.center,
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
            )
            list_services.controls.append(line)
        list_services.update()

    def new_service():
        pass

    def filter_services():
        pass

    text_pesquisar = texts.criar_texto('Pesquisar:')
    input_pesquisar = inputs.criar_input(
        '',
        height=30,
        hint_text='código ou nome',
        bgcolor='#2b5e78',
        border_color='black',
        cursor_height=20,
        on_change=filter_services,
        content_padding=ft.padding.symmetric(5, 5),
    )
    btn_new_service = buttons.iconbutton(
        icone=ft.Icons.ADD,
        bgcolor='#397490',
        icon_size=15,
        tooltip='Cadastrar serviço',
        on_click=new_service,
    )

    cont_cabecalho = ft.Container(
        content=ft.Row(
            controls=[text_pesquisar, input_pesquisar, btn_new_service]
        ),
        expand=True,
        margin=10,
    )

    atualizar_lista(dados_services, cont_cabecalho)
