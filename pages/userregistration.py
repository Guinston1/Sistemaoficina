import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.types import CrossAxisAlignment, FontWeight, MainAxisAlignment

from componentes import buttons, inputs, texts
from services import listgroups, usersalvedb


def newuser() -> ft.Container:

    #funcao para buscar o grupo de usuarios
    groups_list = listgroups.searchlistgroups()

    campo_grupo = ft.Dropdown(
        label="Grupo",
        options=[ft.dropdown.Option(opcao[0]) for opcao in groups_list],
        width=250,
        prefix_icon=ft.Icons.GROUP,
        menu_height=100,
        expand=True,
        bgcolor="#2b5e78",
    )

    container_grupo = ft.Container(
        content=campo_grupo,
        bgcolor="#2b5e78",
        height=40
        )

    msg_cadastro = texts.criar_texto(
        "",
        size=15,
        weight=FontWeight.BOLD,
        )

    def format_uppercase(e):
        e.control.value = e.control.value.upper()
        e.control.update()

    campo_nome = inputs.criar_input("Nome",
                       prefix_icon=ft.Icons.FACE,
                       bgcolor="#2b5e78",
                       border_color="black")

    campo_user = inputs.criar_input("Login",
                       prefix_icon=ft.Icons.ACCOUNT_CIRCLE,
                       bgcolor="#2b5e78",
                       border_color="black",
                        on_change=format_uppercase
                       )
    campo_senha = inputs.criar_input("Senha",
                        prefix_icon=ft.Icons.LOCK,
                        bgcolor="#2b5e78",
                        border_color="black",
                        password=True,
                        max_length=8
                        )
    campo_confirmesenha = inputs.criar_input("Confirme a senha",
                                     prefix_icon=ft.Icons.LOCK_OUTLINED,
                                     bgcolor="#2b5e78",
                                     border_color="black",
                                     password=True,
                                     max_length=8
                                     )
    #campo_grupo = inputs.criar_input("Grupo",
                      # prefix_icon=ft.Icons.GROUP,
                      # bgcolor="#2b5e78",
                      # border_color="black"
                      # )
    campo_loja = inputs.criar_input("Loja",
                       prefix_icon=ft.Icons.STORE,
                       bgcolor="#2b5e78",
                       border_color="black",
                        on_change=format_uppercase

                       )

    #funcao para gravar o usuario no banco de dados
    def salvar_usuario(e):

        if not campo_nome.value or not campo_user.value or not campo_senha.value or not campo_grupo.value or not campo_loja.value:
            print("Preencha todos os campos!")
            msg_cadastro.value = "Preencha todos os campos"
            e.page.update()
        elif campo_senha.value != campo_confirmesenha.value:
            print("Senhas não conferem")
            msg_cadastro.value = "As senhas não coincidem. Verifique e tente novamente."
            e.page.update()
        else:

            cad_nome = campo_nome.value.title()
            cad_usuario = campo_user.value.upper()
            cad_senha = campo_senha.value
            cad_grupo = campo_grupo.value.title()
            cad_loja = campo_loja.value.upper()

            print(f"{cad_usuario}")
            print(f"{cad_senha}")
            print(f"{cad_grupo}")
            print(f"{cad_loja}")

            resultado = usersalvedb.user_salve(cad_nome,cad_usuario, cad_senha, cad_grupo, cad_loja)
            print(resultado)
            if resultado is True:
                msg_cadastro.value = "Usuário cadastrado com sucesso."
                campo_nome.value = ""
                campo_user.value = ""
                campo_senha.value = ""
                campo_grupo.value = ""
                campo_loja.value = ""
                campo_confirmesenha.value = ""
                e.page.update()
            else:
                msg_cadastro.value = "Erro ao cadastrar o usuário. "
                e.page.update()
        e.page.update()

    #criação do botão de salvar
    botao_salvar = buttons.elevated("Salvar",
                       icon=ft.Icons.SAVE,
                       bgcolor="#0e3249",
                       color="white",
                        on_click=salvar_usuario
                        )

    #retorna o container para a criação de tela de cadastro
    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Cadastro de Usuário", size=20, weight=ft.FontWeight.BOLD),
                campo_nome,
                campo_user,
                campo_senha,
                campo_confirmesenha,
                container_grupo,
                #campo_grupo,
                campo_loja,
                botao_salvar,
                msg_cadastro,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=5,
        alignment=ft.alignment.center,
    )

    return formulario