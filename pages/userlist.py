import flet as ft
from mysql.connector import Error

from componentes import buttons, inputs, texts
from services import connectdb, searchusersdb


#função para listar os usuarios
def list_users() -> ft.Container:
    list = ft.ListView(
        expand=True,
        spacing=0,
        padding=0,
        auto_scroll=False  # Deixe como True se quiser rolar automaticamente pro fim
    )
    return list

def add_users(users_list):
    users = searchusersdb.users_search_db()
    print(f"list with users{users}")
    
    header = ft.Row([
        ft.Container(ft.Text("ID", weight=ft.FontWeight.BOLD), width=50, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),
        ft.Container(ft.Text("NOME", weight=ft.FontWeight.BOLD), expand=True, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center_left),
        ft.Container(ft.Text("LOGIN", weight=ft.FontWeight.BOLD), width=120, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),
        ft.Container(ft.Text("GRUPO", weight=ft.FontWeight.BOLD), width=100, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),
        ft.Container(ft.Text("LOJA", weight=ft.FontWeight.BOLD), width=100, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),
        ft.Container(ft.Text("STATUS", weight=ft.FontWeight.BOLD), width=70, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),
        ft.Container(ft.Text("", weight=ft.FontWeight.BOLD), width=50, border=ft.border.all(1, "black"),
                     bgcolor="#0f3c56", alignment=ft.alignment.center),

    ], spacing=0)

    users_list.controls.append(header)
    for id_usuario, nome, login, tipo_usuario, loja, status in users:

        status_str = "Ativo" if str(status) == "1" or status == 1 else "Inativo"
        line = ft.Container(
            padding=0,
            #bgcolor="#1c4861",
            border_radius=5,
            content=ft.Row([
                ft.Container(
                    content=ft.Text(str(id_usuario)),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    bgcolor="#1c4861",
                    width=50,
                    alignment=ft.alignment.center,

                ),
                ft.Container(
                    content=ft.Text(nome, weight=ft.FontWeight.BOLD, size=14),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    expand=True,
                    bgcolor="#1c4861",
                    alignment=ft.alignment.center_left
                ),
                ft.Container(
                    content=ft.Text(login, size=14),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    width=120,
                    bgcolor="#1c4861",
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(tipo_usuario, size=14),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    width=100,
                    bgcolor="#1c4861",
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(loja, size=14),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    width=100,
                    bgcolor="#1c4861",
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(status_str, size=14),
                    padding=1,
                    border=ft.border.all(1, "black"),
                    width=70,
                    bgcolor="#1c4861",
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.EDIT,
                        height=19,
                        icon_size=10,
                        tooltip="Editar",
                        data=id_usuario,
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
        users_list.controls.append(line)

    users_list.update()






