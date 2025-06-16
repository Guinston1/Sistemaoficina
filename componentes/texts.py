import flet as ft


#criação de textos
def criar_texto(
        conteudo:str,
        size: int = 16,
        weight: ft.FontWeight = str,
        color: str = "",
        align: ft.TextAlign = str,
        italic: bool = False,
        selectable: bool = False,
        max_lines: int = None,
        overflow: ft.TextOverflow = str,
)-> ft.Text:
    return ft.Text(
        value=conteudo,
        size=size,
        weight=weight,
        color=color,
        text_align=align,
        italic=italic,
        selectable=selectable,
        max_lines=max_lines,
        overflow=overflow
    )


