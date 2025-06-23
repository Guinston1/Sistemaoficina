import re
import time
import flet as ft
from flet.core.types import MainAxisAlignment

from componentes import buttons, inputs, texts
from services.searchclienteselect import search_client_select
from services.clientsavedb import motosave


def screen_registration_moto():

    def salvar_moto(e):

        cliente = search_client_select(input_cpf.value)
        id_cliente, nome_cliente,sobrenome_cliente = cliente

        gravar_moto = motosave(id_cliente,
                               input_marca.value,
                               input_modelo.value,
                               input_ano.value,
                               input_placa.value)
        if gravar_moto is True:
            text_responsedb.value = f"Motocicleta cadastrada com sucesso para o cliente {nome_cliente}{sobrenome_cliente}."
            text_responsedb.update()

            input_marca.value = ""
            input_marca.update()
            input_modelo.value = ""
            input_modelo.update()
            input_ano.value = ""
            input_ano.update()
            input_placa.value = ""
            input_placa.update()
            input_cpf.value = ""
            input_cpf.update()
        else:
            text_responsedb.value = "Falha ao tentar salvar motocicleta no banco de dados!"
            text_responsedb.update()


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


    text_titulo = texts.criar_texto(
        "Cadastrar Motocicleta",
        size=20,
        weight=ft.FontWeight.BOLD,
        color='white',
    )

    text_responsedb = texts.criar_texto(
        ""
    )

    input_cpf = inputs.criar_input(
        "CPF cliente",
        prefix_icon=ft.Icons.PERSON,
        border_color='black',
        bgcolor='#2b5e78',
        on_change=ao_digitar_cpf,
        content_padding=ft.padding.symmetric(5, 5),
    )

    input_marca = inputs.criar_input(
        on_change=inicial_maiuscula,
        bgcolor='#2b5e78',
        border_color='black',
        prefix_icon=ft.Icons.FACTORY,
        label="Marca"
    )
    input_modelo = inputs.criar_input(
        on_change=inicial_maiuscula,
        bgcolor='#2b5e78',
        border_color='black',
        prefix_icon=ft.Icons.DESIGN_SERVICES,
        label='Modelo'
    )
    input_ano = inputs.criar_input(
        on_change=ao_digitar_ano,
        bgcolor='#2b5e78',
        border_color='black',
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        label='Ano do modelo',
    )
    input_placa = inputs.criar_input(
        on_change=ao_digitar_placa,
        bgcolor='#2b5e78',
        border_color='black',
        prefix_icon=ft.Icons.CONFIRMATION_NUMBER,
        label='Placa'
    )

    btn_salvar_moto = buttons.elevated(
        "Salvar",
        icon=ft.Icons.SAVE,
        color='white',
        bgcolor='green',
        width=150,
        on_click=salvar_moto

    )

    coluna_cad_moto = ft.Container(
        content=ft.Column(
            controls=[
                text_titulo,
                input_cpf,
                input_marca,
                input_modelo,
                input_ano,
                input_placa,
                text_responsedb,
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

