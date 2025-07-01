import re
import time

import flet as ft

from componentes import buttons, inputs, texts
from componentes.texts import criar_texto
from services import connectdb, searchservices


def screen_list_services():
    list_services = ft.ListView(
        expand=True, spacing=0, padding=0, auto_scroll=False
    )

    return list_services


def add_services(list_services):
    dados_services = searchservices.search_services()

    dados_servic = []

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
                                tooltip='Editar',
                                data=id_service,
                                bgcolor='#1c4861',
                                on_click=editar_service,
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

    def save_servico_db(e):
        save_service = searchservices.save_service(
            input_nome_service.value,
            input_tempo_service.value,
            input_descricao_service.value,
            input_preco_service.value,
        )
        if save_service is True:
            msg_db.value = 'Serviço cadastrado com sucesso.'
            msg_db.update()
            input_nome_service.value = ''
            input_nome_service.update()
            input_descricao_service.value = ''
            input_descricao_service.update()
            input_tempo_service.value = ''
            input_tempo_service.update()
            input_preco_service.value = ''
            input_preco_service.update()
            time.sleep(2)

            msg_db.value = ''
            msg_db.update()
            dados_services_atualizado = searchservices.search_services()
            atualizar_lista(dados_services_atualizado, cont_cabecalho)
        else:
            msg_db.value = 'Falha ao salvar o serviço no banco de dados.'
            msg_db.update()

    def save_edit(e):
        print(input_edit_nome.value)

        id_servic = dados_servic[0][0]
        print(id_servic)
        service_atualizado = searchservices.update_service(
            id_servic,
            input_edit_nome.value,
            input_edit_tempo.value,
            input_edit_descricao.value,
            input_edit_preco.value,
        )

        if service_atualizado is True:
            print('Serviço atualizado com sucesso.')

            text_edit_nome.visible = False
            input_edit_nome.visible = False
            text_edit_tempo.visible = False
            input_edit_tempo.visible = False
            text_edit_descricao.visible = False
            input_edit_descricao.visible = False
            text_edit_preco.visible = False
            input_edit_preco.visible = False
            btn_save_edit.visible = False

            loader.visible = True
            formulario_edit.update()
            time.sleep(2)
            loader.visible = False
            formulario_edit.update()

            text_msg_atualizado.visible = True
            text_msg_atualizado.value = 'Serviço atualizado com sucesso.'
            text_msg_atualizado.update()
            formulario_edit.update()
            time.sleep(2)

            dados_atualizados = searchservices.search_services()
            text_msg_atualizado.value = ''
            text_msg_atualizado.update()
            atualizar_lista(dados_atualizados, cont_cabecalho)
        else:
            print('Erro ao atualizar o serviço')
            text_msg_atualizado.value = (
                'Falha ao atualizar o serviço no banco de dados.'
            )
            text_msg_atualizado.update()

    def editar_service(e):
        dados_services_atualizar = searchservices.search_services()
        print(e.control.data)
        servico_select = e.control.data
        print(servico_select)
        list_services.controls.clear()
        list_services.update()
        for item in dados_services_atualizar:
            if servico_select in item:
                if len(dados_servic) == 1:
                    dados_servic.clear()
                    dados_servic.append(item)
                else:
                    dados_servic.append(item)

                print(dados_servic)

        list_services.controls.append(formulario_edit)
        list_services.update()
        if input_edit_nome.visible is False:
            text_edit_nome.visible = True
            text_edit_nome.update()
            input_edit_nome.visible = True
            text_edit_tempo.visible = True
            text_edit_tempo.update()
            input_edit_tempo.visible = True
            text_edit_descricao.visible = True
            text_edit_descricao.update()
            input_edit_descricao.visible = True
            text_edit_preco.visible = True
            text_edit_preco.update()
            input_edit_preco.visible = True
            btn_save_edit.visible = True
            btn_save_edit.update()

        input_edit_nome.value = dados_servic[0][1]
        input_edit_nome.update()
        input_edit_tempo.value = dados_servic[0][2]
        input_edit_tempo.update()
        input_edit_descricao.value = dados_servic[0][3]
        input_edit_descricao.update()
        input_edit_preco.value = dados_servic[0][4]
        input_edit_preco.update()

    def new_service(e):
        list_services.controls.clear()
        list_services.controls.append(formulario_service)
        list_services.update()

    def formatar_preco(valor):
        numeros = re.sub(r'\D', '', valor)[:9]

        numeros = re.sub(r'\D', '', valor)  # remove tudo que não for número
        if len(numeros) < 3:
            return numeros  # ainda não tem 2 casas decimais
        return f'{numeros[:-2]}.{numeros[-2:]}'

    def ao_digitar_preco(e):
        e.control.value = formatar_preco(e.control.value)
        e.control.update()

    def ao_digitar_nome(e):
        texto = e.control.value.title()
        input_nome_service.value = texto
        input_nome_service.update()

    def filter_services(e):
        termo = e.control.value.upper()
        servicos_filtrados = [
            c
            for c in dados_services
            if termo in str(c[0]) or termo in c[1].upper()
        ]
        atualizar_lista(servicos_filtrados, cont_cabecalho)

    text_msg_atualizado = ft.Text(
        '', size=20, weight=ft.FontWeight.BOLD, color='green'
    )

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

    loader = ft.ProgressRing(
        width=20, height=20, stroke_width=4, visible=False
    )

    text_edit_nome = ft.Container(content=ft.Text('Nome:'), width=50)
    text_edit_tempo = ft.Container(content=ft.Text('Tempo:'), width=50)

    text_edit_descricao = ft.Container(content=ft.Text('Descrição:'), width=70)
    text_edit_preco = ft.Container(content=ft.Text('Preço:'), width=50)

    input_edit_nome = inputs.criar_input(
        '',
        height=30,
        width=150,
        on_change=ao_digitar_nome,
        bgcolor='#1c4861',
        border_color='black',
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_edit_tempo = inputs.criar_input(
        '',
        height=30,
        width=50,
        bgcolor='#1c4861',
        border_color='black',
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_edit_descricao = inputs.criar_input(
        '',
        height=100,
        width=300,
        bgcolor='#1c4861',
        max_lines=5,
        multiline=True,
        min_lines=1,
        border_color='black',
        content_padding=ft.padding.symmetric(5, 5),
    )
    input_edit_preco = inputs.criar_input(
        '',
        height=30,
        on_change=ao_digitar_preco,
        width=100,
        bgcolor='#1c4861',
        border_color='black',
        content_padding=ft.padding.symmetric(5, 5),
    )
    btn_save_edit = buttons.elevated(
        'Salvar',
        icon=ft.Icons.SAVE,
        on_click=save_edit,
        width=100,
        color='white',
        bgcolor='green',
    )

    container_descricao = ft.Container(
        content=input_edit_descricao,
        margin=ft.Margin(left=0, top=40, right=0, bottom=0),
    )

    linha_nome = ft.Row(
        controls=[
            text_edit_nome,
            input_edit_nome,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    linha_tempo = ft.Row(
        controls=[text_edit_tempo, input_edit_tempo],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    linha_descricao = ft.Row(
        controls=[text_edit_descricao, container_descricao],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    linha_preco = ft.Row(
        controls=[text_edit_preco, input_edit_preco],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    formulario_edit = ft.Container(
        content=ft.Row(
            controls=[
                linha_nome,
                linha_descricao,
                loader,
                text_msg_atualizado,
                linha_tempo,
                linha_preco,
                btn_save_edit,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=True,
        ),
        alignment=ft.alignment.center,
        margin=ft.Margin(left=0, right=0, bottom=0, top=20),
        expand=True,
    )

    msg_db = ft.Text('')
    input_nome_service = inputs.criar_input(
        'Nome',
        width=300,
        bgcolor='#1c4861',
        border_color='black',
        on_change=ao_digitar_nome,
    )
    input_tempo_service = inputs.criar_input(
        'Tempo', width=300, bgcolor='#1c4861', border_color='black'
    )
    input_descricao_service = inputs.criar_input(
        'Descrição', width=300, bgcolor='#1c4861', border_color='black'
    )
    input_preco_service = inputs.criar_input(
        'Preço',
        width=300,
        bgcolor='#1c4861',
        border_color='black',
        on_change=ao_digitar_preco,
    )
    btn_salvar_service = buttons.elevated(
        'Salvar',
        color='white',
        bgcolor='green',
        on_click=save_servico_db,
        icon=ft.Icons.SAVE,
    )
    titulo_cadastro_service = texts.criar_texto(
        'Cadastro de Serviço',
        size=20,
        weight=ft.FontWeight.BOLD,
    )

    formulario_service = ft.Container(
        content=ft.Column(
            controls=[
                titulo_cadastro_service,
                input_nome_service,
                input_tempo_service,
                input_descricao_service,
                input_preco_service,
                btn_salvar_service,
                msg_db,
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor='#0e3249',
        padding=20,
        alignment=ft.alignment.center,
        margin=ft.Margin(left=100, top=40, right=20, bottom=40),
        expand=True,
    )

    atualizar_lista(dados_services, cont_cabecalho)
