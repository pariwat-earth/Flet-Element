import flet as ft

from element.app_bar import appbar

page_name = 'ฟาร์มรัก'


def main(page: ft.Page):

    page.fonts = {
        "Sarabun": "https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;700&display=swap"
    }

    page.theme = ft.Theme(font_family="Sarabun")

    page.padding = 0
    page.margin = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    
    page.add(
        ft.SafeArea(
            ft.Column(
                [appbar(page_name)],
                spacing=0,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                expand=True,
            ),
            expand=True
        )
    )


ft.app(main)