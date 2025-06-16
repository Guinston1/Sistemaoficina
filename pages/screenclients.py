from flet.core.types import MainAxisAlignment
from pages import screenregistrationclient
from services import searchclientsdb
from componentes import inputs, texts, buttons
import flet as ft


#funcao para criar a tela de clientes
def screen_clients():

    list_clients = ft.ListView(
        expand=True,
        spacing=0,
        padding=0,
        auto_scroll=False
    )

    return list_clients


def add_clients(list_clients):

    clientes_lista = searchclientsdb.search_clients()

    def registration_new_client(e):

        tela_cadastro_clientes = screenregistrationclient.screen_registration_clients()
        list_clients.controls.clear()
        list_clients.controls.append(tela_cadastro_clientes)
        list_clients.update()



    def atualizar_list(clientes_lista, container_linha):

        list_clients.controls.clear()
        list_clients.controls.append(container_linha)

        header = ft.Row([
            ft.Container(ft.Text("ID", size=14, weight=ft.FontWeight.BOLD), width=50, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("NOME", size=14, weight=ft.FontWeight.BOLD), expand=True, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center_left),
            ft.Container(ft.Text("SOBRENOME", size=14, weight=ft.FontWeight.BOLD),expand=True, width=120, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("CPF", size=14, weight=ft.FontWeight.BOLD),expand=True, width=100, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("TELEFONE", size=14, weight=ft.FontWeight.BOLD),expand=True, width=100, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("ENDEREÇO", size=14, weight=ft.FontWeight.BOLD),expand=True, width=70, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("BAIRRO", size=14, weight=ft.FontWeight.BOLD), expand=True, width=70,
                         border=ft.border.all(1, "black"),
                         bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("CIDADE",size=14, weight=ft.FontWeight.BOLD), expand=True, width=100,
                     border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("ESTADO",size=14, weight=ft.FontWeight.BOLD), expand=True, width=100,
                     border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("CADASTRO",size=14, weight=ft.FontWeight.BOLD),expand=True, width=100, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ft.Container(ft.Text("", weight=ft.FontWeight.BOLD), width=50, border=ft.border.all(1, "black"),
                     bgcolor="#0e3249", alignment=ft.alignment.center),
            ], spacing=0)


        list_clients.controls.append(header)

        for id_client, first_name, last_name, cpf, telefone, bairro, cidade, estado, endereco, data_cadastro in clientes_lista:

            line = ft.Container(
                padding=0,
                border_radius=5,
                content=ft.Row([
                    ft.Container(
                        content=ft.Text(id_client),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        bgcolor="#1c4861",
                        width=50,
                        alignment=ft.alignment.center,

                    ),
                    ft.Container(
                        content=ft.Text(first_name, weight=ft.FontWeight.BOLD, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center_left
                    ),
                    ft.Container(
                        content=ft.Text(last_name, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=120,
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(cpf, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=100,
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(telefone, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=100,
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(endereco, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=70,
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(bairro, size=12),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=100,
                        expand=True,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(cidade, size=12),
                        padding=1,
                        expand=True,
                        border=ft.border.all(1, "black"),
                        width=70,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),ft.Container(
                        content=ft.Text(estado, size=12),
                        padding=1,
                        expand=True,
                        border=ft.border.all(1, "black"),
                        width=70,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text(data_cadastro, size=12),
                        padding=1,
                        expand=True,
                        border=ft.border.all(1, "black"),
                        width=70,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.Icons.EDIT,
                            height=20,
                            icon_size=15,
                            tooltip="Editar",
                            data=id_client,
                            bgcolor="#1c4861",
                            on_click=lambda e: print(f"Editar {e.control.data}")
                        ),
                        padding=1,
                        border=ft.border.all(1, "black"),
                        width=50,
                        bgcolor="#1c4861",
                        alignment=ft.alignment.center
                    ),
                ], spacing=0, alignment=ft.MainAxisAlignment.START)
            )
            list_clients.controls.append(line)

        list_clients.update()

    def filtrar_clientes(e):
        termo = e.control.value.title()
        clientes_filtrados = [c for c in clientes_lista if  termo in c[1] or
                                                            termo in c[3]
        ]
        atualizar_list(clientes_filtrados,container_linha)

    btn_new_client = buttons.iconbutton(
        icone=ft.Icons.ADD_BOX,
        on_click=registration_new_client,
        bgcolor="#397490",
        icon_size=15,
        tooltip="Cadastrar cliente."

    )

    title_campo_procurar = texts.criar_texto(
        "Pesquisar:"
    )

    procurador = inputs.criar_input(
        height=30,
        border_color="black",
        bgcolor="#2b5e78",
        cursor_height=20,
        hint_text="Nome ou CPF",
        on_change=filtrar_clientes,
        content_padding=ft.padding.symmetric(5, 5)
    )

    headerup = ft.Row(
        controls=[
            title_campo_procurar,
            procurador,
            btn_new_client
        ],
    )

    container_linha = ft.Container(
        content=headerup,
        margin=10
    )


    list_clients.controls.append(container_linha)
    atualizar_list(clientes_lista, container_linha)
