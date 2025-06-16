import flet as ft


def criar_input(
        label: str = None,
        password: bool = False,
        hint_text: str = "",
        width: int = 250,
        height: int = 40,
        value: str = "",
        focused: str = None,
        bgcolor: str = "#001c32",
        border_color: str = "black",
        prefix_text: str = None,
        prefix_icon: str = None,
        suffix_text: str = None,
        sufix_icon: str = None,
        max_length: int = None,
        content_padding: str = None,
        on_change: str = None,
        cursor_height: int = None,
        text_align: ft.TextAlign = ft.TextAlign.LEFT
) -> ft.TextField:
    return ft.TextField(
        label=label,
        password=password,
        can_reveal_password=password,
        hint_text=hint_text,
        width=width,
        height=height,
        value=value,
        cursor_height=cursor_height,
        suffix_text=suffix_text,
        prefix_text=prefix_text,
        focused_color=focused,
        on_change=on_change,
        suffix_icon=sufix_icon,
        bgcolor=bgcolor,
        max_length=max_length,
        content_padding=content_padding,
        border_color=border_color,
        prefix_icon=prefix_icon,
        text_align=text_align
    )