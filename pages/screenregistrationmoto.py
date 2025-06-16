import re

import flet as ft
from flet.core.types import MainAxisAlignment

from componentes import buttons, inputs, texts
from services.searchclienteselect import search_client_select

def screen_registration_moto():


    def buscar_cliente(e):
        cliente_selecionado = search_client_select(input_cpf.value)

        id_client, nome, last_name = cliente_selecionado

        text_nome_cliente.value = f'ID: {id_client}  Cliente: {nome} {last_name}'
        text_nome_cliente.update()


    def formatar_ano(valor):
        numeros = ''.join(filter(str.isdigit, valor))[
            :4
        ]  # aceita só números e limita 4 dígitos
        return numeros

    def ao_digitar_ano(e):
        e.control.value = formatar_ano(e.control.value)
        e.control.update()

    def formatar_placa(valor):
        placa = re.sub(r'\W', '', valor).upper()[
            :7
        ]  # Remove não alfanuméricos e limita a 7 caracteres

        # Detecta se é do padrão antigo (3 letras seguidas de 4 números)
        if re.fullmatch(r'[A-Z]{3}[0-9]{4}', placa):
            return f'{placa[:3]}-{placa[3:]}'  # AAA-1234
        else:
            return placa  # Padrão Mercosul ou parcial

    def ao_digitar_placa(e):
        e.control.value = formatar_placa(e.control.value)
        e.control.update()

    def inicial_maiuscula(e):
        e.control.value = e.control.value.title()
        e.control.update()

    def formatar_cpf(valor):
        numeros = re.sub(r'\D', '', valor)[
            :11
        ]  # Remove tudo que não for número e limita a 11

        if len(numeros) >= 9:
            return f'{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}'
        elif len(numeros) >= 6:
            return f'{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}'
        elif len(numeros) >= 3:
            return f'{numeros[:3]}.{numeros[3:]}'
        else:
            return numeros

    def ao_digitar_cpf(e):
        e.control.value = formatar_cpf(e.control.value)
        e.control.update()

    text_nome_cliente = texts.criar_texto(
        ""
    )
    text_pesquisar = texts.criar_texto("Cliente: ")


    input_cpf = inputs.criar_input(
        "",
        height=30,
        border_color='black',
        width=200,
        bgcolor='#2b5e78',
        cursor_height=20,
        hint_text='busca por CPF...',
        on_change=ao_digitar_cpf,
        content_padding=ft.padding.symmetric(5, 5),
    )

    input_marca = inputs.criar_input(
        on_change=inicial_maiuscula,
        prefix_icon=ft.Icons.FACTORY,
        label="Marca"
    )
    input_modelo = inputs.criar_input(
        on_change=inicial_maiuscula,
        prefix_icon=ft.Icons.DESIGN_SERVICES,
        label='Modelo'
    )
    input_ano = inputs.criar_input(
        on_change=ao_digitar_ano,
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        label='Ano do modelo',
    )
    input_placa = inputs.criar_input(
        on_change=ao_digitar_placa,
        prefix_icon=ft.Icons.CONFIRMATION_NUMBER,
        label='Placa'
    )

    btn_salvar_moto = buttons.elevated(
        "Salvar",
        icon=ft.Icons.SAVE,
        color='white',
        bgcolor='green',
        width=150,
        on_click=buscar_cliente,

    )

    btn_buscar_cliente = buttons.elevated(
        "Buscar",
        icon=ft.Icons.SEARCH,
        on_click=buscar_cliente,
        color='white',
        bgcolor='#1c4861',
        width=100,

    )

    linha_cliente = ft.Container(
        content=ft.Row(
            controls=[
                text_pesquisar,
                input_cpf,
                btn_buscar_cliente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),expand=True
    )

    coluna_cad_moto = ft.Container(
        content=ft.Column(
            controls=[
                linha_cliente,
                text_nome_cliente,
                input_marca,
                input_modelo,
                input_ano,
                input_placa,
                btn_salvar_moto
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        expand=True,
        alignment=ft.alignment.center,
        margin=20
    )
    return coluna_cad_moto

