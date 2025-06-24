from datetime import date

import flet as ft
from flet.core.border_radius import horizontal
from flet.core.types import CrossAxisAlignment, MainAxisAlignment

from componentes import buttons, inputs, texts
from pages import (screenclients, screenmotocicletas, screenservices, userlist,
                   userregistration)
from services import connectdb
from validacoes import validationlogin


def main(page: ft.Page):

    # tela home/principal do sistema
    def home(user):

        page.clean()
        page.update()

        # Container que muda o conteudo da tela
        screen_content = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[], expand=True, alignment=MainAxisAlignment.CENTER
            ),
            expand=True,
            bgcolor='#001c32',
        )

        def screen_list_services(e):
            print('Funcao serviços selecionada.')

            screen_content.content.controls.clear()
            page.update()

            list_services = screenservices.screen_list_services()
            screen_content.content.controls.append(list_services)
            page.update()

            screenservices.add_services(list_services)

        def screen_list_motocicletas(e):
            print('Funcao motocicletas selecionada.')

            screen_content.content.controls.clear()
            page.update()

            list_motos = screenmotocicletas.screen_list_motos()
            screen_content.content.controls.append(list_motos)
            page.update()

            screenmotocicletas.add_motos(list_motos)

        # funcao para listar e cadastar clientes
        def screen_list_clients(e):
            print('Funcao clientes selecionada.')

            screen_content.content.controls.clear()
            page.update()

            list_clients = screenclients.screen_clients()
            screen_content.content.controls.append(list_clients)
            page.update()

            screenclients.add_clients(list_clients)
            page.update()

        # função para listar os usuários cadastrados
        def list_users(e):

            print('Funçao listar usuário selecionada.')

            screen_content.content.controls.clear()
            page.update()

            users_list = userlist.list_users()
            print(users_list)

            screen_content.content.controls.append(users_list)
            page.update()

            userlist.add_users(users_list)
            page.update()

        # função para cadastrar um novo usuario no sistema
        def user_registration(e):

            print(
                'Função cadastrar usuario'
            )   # printa o text para saber que selecionou a função
            screen_content.content.controls.clear()
            formulario = (
                userregistration.newuser()
            )   # chama a função que cria os
            # componentes e salve o user no banco

            screen_content.content.controls.append(
                formulario
            )   # inseri o formulario no container da tela

            print(formulario)
            page.update()

        # funcoes do menu na tela principal onde printa os eventos
        def handle_menu_item_click(e):
            print(f'{e.control.content.value}.on_click')

        def handle_submenu_open(e):
            print(f'{e.control.content.value}.on_open')

        def handle_submenu_close(e):
            print(f'{e.control.content.value}.on_close')

        def handle_submenu_hover(e):
            print(f'{e.control.content.value}.on_hover')

        # criação do menu que fica na parte superior da tela
        menu = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                bgcolor='#1c4861',
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
            controls=[
                ft.SubmenuButton(
                    content=ft.Text('Cadastros'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Novo usuário'),
                            leading=ft.Icon(ft.Icons.ADD),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=user_registration,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Usuários do sistema'),
                            leading=ft.Icon(ft.Icons.MANAGE_ACCOUNTS),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=list_users,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Clientes'),
                            leading=ft.Icon(ft.Icons.PERSON_PIN),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=screen_list_clients,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Motocicletas'),
                            leading=ft.Icon(ft.Icons.MOTORCYCLE),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=screen_list_motocicletas,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Funcionários'),
                            leading=ft.Icon(ft.Icons.BADGE),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=handle_menu_item_click,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Serviços'),
                            leading=ft.Icon(ft.Icons.HANDYMAN),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=screen_list_services,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text('Produtos'),
                            leading=ft.Icon(ft.Icons.INVENTORY_2),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(5),
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_GREY_800
                                },
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Frente de Caixa'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Usuário'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Estoque'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Visualizar estoque'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Financeiro'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Contas a pagar'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Fiscal'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Visualizar estoque'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Relatórios'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Relátorio de vendas'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text('Configurações Gerais'),
                    on_open=handle_submenu_open,
                    on_close=handle_submenu_close,
                    on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text('Visualizar estoque'),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.HOVERED: ft.Colors.GREEN_100
                                }
                            ),
                            on_click=handle_menu_item_click,
                        ),
                    ],
                ),
            ],
        )

        # pega no sistema a data do dia
        data_atual = date.today()

        # textos do rodape com dados do usuario
        text_data_atual = texts.criar_texto(f'Data: {data_atual}')
        text_usuario = texts.criar_texto(f'Usuário: {user[1]}')
        text_grupo_usuario = texts.criar_texto(f'Grupo: {user[5]}')
        text_loja = texts.criar_texto(f'Loja: {user[6]}')

        # criação do rodape para a tela home
        rodape = ft.Container(
            content=ft.Row(
                controls=[
                    text_usuario,
                    text_grupo_usuario,
                    text_loja,
                    text_data_atual,
                ],
            ),
            padding=10,
            bgcolor='#1c4861',
        )

        # container contendo o menu
        barramenu = ft.Container(content=ft.Row(controls=[menu]))

        # criação da tela home
        page.add(
            ft.Column(
                controls=[barramenu, screen_content, rodape],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )

    # mensagem informando usuario ou senha invalido
    msg_login = texts.criar_texto('')

    # função que realiza o login
    def efetuar_Login(login, senha, msg_login):
        login_efetuado = validationlogin.validation_login(login, senha)
        print(login_efetuado)
        if login_efetuado is False:
            msg_login.value = 'Usuário ou senha incorretos. Tente novamente.'
            page.update()
        else:
            home(login_efetuado)

    def forcar_maiusculo(e):
        e.control.value = e.control.value.upper()
        e.control.update()

    # chamada da funcao para criar os inputs login e senha
    input_login = inputs.criar_input(
        '', prefix_icon=ft.Icons.ACCOUNT_CIRCLE, on_change=forcar_maiusculo
    )
    input_senha = inputs.criar_input(
        '',
        prefix_icon=ft.Icons.LOCK,
        password=True,
        text_align=ft.alignment.center,
    )

    # chamada da funcao para criar o botao de login
    botao_login = buttons.elevated(
        'LOGIN',
        color=ft.Colors.WHITE,
        bgcolor='#1c4861',
        icon=ft.Icons.LOGOUT,
        on_click=lambda e: efetuar_Login(
            input_login.value, input_senha.value, msg_login
        ),
    )

    # criando a tela de login
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[input_login, input_senha, botao_login, msg_login],
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
    )


ft.app(target=main)
