import flet as ft


def elevated(
    texto: str,
    on_click=None,
    color: str = None,
    bgcolor: str = None,
    width: int = 250,
    height: int = 30,
    tooltip: str = None,
    icon: str = None,
    radius: int = 10,
) -> ft.ElevatedButton:
    return ft.ElevatedButton(
        text=texto,
        on_click=on_click,
        width=width,
        height=height,
        icon=icon,
        tooltip=tooltip,
        style=ft.ButtonStyle(
            color=color,
            bgcolor=bgcolor,
            shape=ft.RoundedRectangleBorder(radius=radius),
            overlay_color=ft.Colors.with_opacity(0.1, 'white'),
        ),
    )


def menuitembt(
    texto: str,
    icon: str = None,
    bgcolor: str = '#1c4861',
    radius: int = 5,
    on_click=None,
    on_hover=None,
) -> ft.MenuItemButton:
    return ft.MenuItemButton(
        content=ft.Text(texto),
        leading=ft.Icon(icon) if icon else None,
        on_click=on_click,
        on_hover=on_hover,
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.HOVERED: '#397490',
                ft.ControlState.FOCUSED: '#1c4861',
                ft.ControlState.DEFAULT: '#1c4861',
            },
            color='white',
            shape=ft.RoundedRectangleBorder(radius=radius),
        ),
    )


def iconbutton(
    icone: str = None,
    tooltip: str = '',
    on_click=None,
    bgcolor: str = None,
    icon_size: int = 20,
    height: int = 30,
    width: int = 30,
    data=None,
    radius: int = 5,
    disabled: bool = False,
    icon_color: str = 'white',
):
    return ft.IconButton(
        icon=icone,
        icon_size=icon_size,
        height=height,
        width=width,
        tooltip=tooltip,
        on_click=on_click,
        bgcolor=bgcolor,
        data=data,
        alignment=ft.alignment.center,
        disabled=disabled,
        icon_color=icon_color,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=radius)),
    )
