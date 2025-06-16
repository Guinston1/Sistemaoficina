import re
from encodings.aliases import aliases

import flet as ft
from flet.core.types import CrossAxisAlignment, MainAxisAlignment

from componentes import buttons, inputs, texts
from services import clientsavedb


#funcao para tela de cadastro de clientes
def screen_registration_clients():


    def save_client(e):
        if( not input_nome.value or not
                input_sobrenome.value or not
                input_cpf.value or not
                input_telefone.value or not
                input_endereco.value or not
                input_bairro.value or not
                input_cidade.value or not
                input_estado.value or not
                input_marca.value or not
                input_modelo.value or not
                input_ano.value or not
                input_placa.value
        ):
            msg_save_client.value = "Preencha todos os campos!"
            msg_save_client.update()
        else:
            nome = input_nome.value
            sobrenome = input_sobrenome.value
            cpf      =  input_cpf.value
            telefone =  input_telefone.value
            endereco =  input_endereco.value
            bairro   =  input_bairro.value
            cidade   =  input_cidade.value
            estado   =  input_estado.value
            marca    =  input_marca.value
            modelo   =  input_modelo.value
            ano      =  input_ano.value
            placa    =  input_placa.value

            salvar_cliente = clientsavedb.save_client_db(nome,sobrenome,cpf,telefone,bairro,cidade, estado, endereco,  marca, modelo, ano, placa)
            print(salvar_cliente)
            if salvar_cliente is True:
                msg_save_client.value = "Usuário cadastrado com sucesso!"
                msg_save_client.update()

                input_nome.value = ""
                input_nome.update()
                input_sobrenome.value = ""
                input_sobrenome.update()
                input_cpf.value = ""
                input_cpf.update()
                input_telefone.value = ""
                input_telefone.update()
                input_endereco.value = ""
                input_endereco.update()
                input_bairro.value = ""
                input_bairro.update()
                input_cidade.value = ""
                input_cidade.update()
                input_estado.value = ""
                input_estado.update()
                input_marca.value = ""
                input_marca.update()
                input_modelo.value = ""
                input_modelo.update()
                input_ano.value = ""
                input_ano.update()
                input_placa.value = ""
                input_placa.update()


    def formatar_ano(valor):
        numeros = ''.join(filter(str.isdigit, valor))[:4]  # aceita só números e limita 4 dígitos
        return numeros

    def ao_digitar_ano(e):
        e.control.value = formatar_ano(e.control.value)
        e.control.update()

    def formatar_placa(valor):
        placa = re.sub(r'\W', '', valor).upper()[:7]  # Remove não alfanuméricos e limita a 7 caracteres

        # Detecta se é do padrão antigo (3 letras seguidas de 4 números)
        if re.fullmatch(r'[A-Z]{3}[0-9]{4}', placa):
            return f"{placa[:3]}-{placa[3:]}"  # AAA-1234
        else:
            return placa  # Padrão Mercosul ou parcial

    def ao_digitar_placa(e):
        e.control.value = formatar_placa(e.control.value)
        e.control.update()


    def formatar_cpf(valor):
        numeros = re.sub(r'\D', '', valor)[:11]  # Remove tudo que não for número e limita a 11

        if len(numeros) >= 9:
            return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        elif len(numeros) >= 6:
            return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}"
        elif len(numeros) >= 3:
            return f"{numeros[:3]}.{numeros[3:]}"
        else:
            return numeros

    def ao_digitar_cpf(e):
        e.control.value = formatar_cpf(e.control.value)
        e.control.update()

    def formatar_celular(valor):
        numeros = re.sub(r'\D', '', valor)[:11]  # Remove não dígitos e limita a 11

        if len(numeros) >= 2:
            parte1 = f"({numeros[:2]})"
        else:
            parte1 = f"({numeros}"

        if len(numeros) >= 7:
            parte2 = f" {numeros[2:7]}-{numeros[7:]}"
        elif len(numeros) > 2:
            parte2 = f" {numeros[2:]}"
        else:
            parte2 = ""

        return parte1 + parte2

    def ao_digitar_telefone(e):
        e.control.value = formatar_celular(e.control.value)
        e.control.update()


    def letras_maiusculas(e):
        e.control.value = e.control.value.upper()
        e.control.update()

    def inicial_maiuscula(e):
        e.control.value = e.control.value.title()
        e.control.update()


    msg_save_client = ft.Text("",size=15, weight=ft.FontWeight.BOLD)
    btn_salve = buttons.elevated("Salvar", on_click=save_client, color="white",bgcolor="green", icon=ft.Icons.SAVE, width=200)

    text_nome = texts.criar_texto("Nome:", size=16)
    text_sobrenome = texts.criar_texto("Sobrenome:",size=16)
    text_cpf = texts.criar_texto("CPF:",size=16)
    text_telefone = texts.criar_texto("Telefone:",size=16)
    text_bairro = texts.criar_texto("Bairro:",size=16)
    text_cidade = texts.criar_texto("Cidade:",size=16)
    text_estado = texts.criar_texto("Estado:",size=16)
    text_marca = texts.criar_texto("Marca:",size=16)
    text_endereco = texts.criar_texto("Endereço:")
    text_modelo = texts.criar_texto("Modelo:",size=16)
    text_ano = texts.criar_texto("Ano do modelo:",size=16)
    text_placa = texts.criar_texto("Placa:",size=16)

    container_text_nome = ft.Container(content=text_nome, width=100)
    container_text_sobrenome = ft.Container(content=text_sobrenome, width=100)
    container_text_cpf = ft.Container(content=text_cpf, width=100)
    container_text_telefone = ft.Container(content=text_telefone, width=100)
    container_text_endereco = ft.Container(content=text_endereco, width=100)
    container_text_bairro = ft.Container(content=text_bairro, width=100)
    container_text_cidade = ft.Container(content=text_cidade, width=100)
    container_text_estado = ft.Container(content=text_estado, width=100)
    container_text_marca = ft.Container(content=text_marca, width=100)
    container_text_modelo= ft.Container(content=text_modelo, width=100)
    container_text_ano = ft.Container(content=text_ano, width=100)
    container_text_placa = ft.Container(content=text_placa, width=100)


    input_nome = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.PERSON)
    input_sobrenome = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.PERSON_OUTLINE)
    input_cpf = inputs.criar_input(on_change=ao_digitar_cpf,prefix_icon=ft.Icons.BADGE)
    input_telefone = inputs.criar_input(on_change=ao_digitar_telefone, prefix_icon=ft.Icons.PHONE)
    input_endereco = inputs.criar_input(on_change=inicial_maiuscula,prefix_icon=ft.Icons.HOME)
    input_bairro = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.LOCATION_CITY)
    input_cidade = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.LOCATION_ON)
    input_estado = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.PUBLIC)
    input_marca = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.FACTORY)
    input_modelo = inputs.criar_input(on_change=inicial_maiuscula, prefix_icon=ft.Icons.DESIGN_SERVICES)
    input_ano = inputs.criar_input(on_change=ao_digitar_ano, prefix_icon=ft.Icons.CALENDAR_MONTH)
    input_placa = inputs.criar_input(on_change=ao_digitar_placa, prefix_icon=ft.Icons.CONFIRMATION_NUMBER)

    linha_nome = ft.Row(controls=[container_text_nome, input_nome], alignment=ft.MainAxisAlignment.CENTER)
    linha_sobrenome = ft.Row(controls=[container_text_sobrenome, input_sobrenome],alignment=ft.MainAxisAlignment.CENTER)
    linha_cpf = ft.Row(controls=[container_text_cpf, input_cpf], alignment=ft.MainAxisAlignment.CENTER)
    linha_telefone = ft.Row(controls=[container_text_telefone, input_telefone],alignment=ft.MainAxisAlignment.CENTER)
    linha_endereco = ft.Row(controls=[container_text_endereco, input_endereco], alignment=ft.MainAxisAlignment.CENTER)
    linha_bairro = ft.Row(controls=[container_text_bairro, input_bairro],alignment=ft.MainAxisAlignment.CENTER)
    linha_cidade = ft.Row(controls=[container_text_cidade, input_cidade],alignment=ft.MainAxisAlignment.CENTER)
    linha_estado = ft.Row(controls=[container_text_estado, input_estado],alignment=ft.MainAxisAlignment.CENTER)
    linha_marca = ft.Row(controls=[container_text_marca, input_marca],alignment=ft.MainAxisAlignment.CENTER)
    linha_modelo = ft.Row(controls=[container_text_modelo, input_modelo],alignment=ft.MainAxisAlignment.CENTER)
    linha_ano = ft.Row(controls=[container_text_ano, input_ano],alignment=ft.MainAxisAlignment.CENTER)
    linha_placa = ft.Row(controls=[container_text_placa, input_placa],alignment=ft.MainAxisAlignment.CENTER)


    container_dados_pessoas = ft.Container(
        content=ft.Column(
            controls=[ft.Row(controls=[
                ft.Icon(ft.Icons.ACCOUNT_BOX, color="white"),
                ft.Text("Cliente", size=20, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
                linha_nome,
                linha_sobrenome,
                linha_cpf,
                linha_telefone
            ], alignment=ft.MainAxisAlignment.CENTER, expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ), bgcolor="#0e3249", expand=True,height=300, border=ft.border.all(2, "black")
    )

    container_localizacao = ft.Container(
        content=ft.Column(
            controls=[ft.Row(controls=[
                ft.Icon(ft.Icons.MAP, color="white"),
                ft.Text("Localização", size=20, weight=ft.FontWeight.BOLD),],alignment=ft.MainAxisAlignment.CENTER),
                linha_endereco,
                linha_bairro,
                linha_cidade,
                linha_estado,
                msg_save_client,
                btn_salve
            ], alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True
        ), bgcolor="#0e3249", expand=True, height=300, border=ft.border.all(2, "black")
    )

    container_motocicleta = ft.Container(
        content=ft.Column(
            controls=[ft.Row(controls=[
                ft.Icon(ft.Icons.MOTORCYCLE, color="white"),
                ft.Text("Motocicleta",size=20, weight=ft.FontWeight.BOLD)],alignment=ft.MainAxisAlignment.CENTER),
                linha_marca,
                linha_modelo,
                linha_ano,
                linha_placa
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        ), bgcolor="#0e3249", expand=True, height=300,border=ft.border.all(2, "black")
    )

    linha_containers = ft.Row(controls=[container_dados_pessoas, container_motocicleta])

    tela_cadastro_clientes = ft.Container(
        content=ft.Column(
            controls=[
                linha_containers,
                container_localizacao
            ], expand=True
        ), expand=True
    )

    return tela_cadastro_clientes