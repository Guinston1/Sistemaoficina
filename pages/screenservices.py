import flet as ft

from componentes import buttons, inputs, texts
from services import connectdb, searchservices


def screen_list_services():
    list_services = ft.ListView(
        expand=True, spacing=0, padding=0, auto_scroll=False
    )

    return list_services


def add_services():
    services = searchservices.search_services()
