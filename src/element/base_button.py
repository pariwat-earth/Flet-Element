import flet as ft

from element.constance import Deep_Purple, Neo_Mint, White

White = "#FFFFFF"
Black = "#000000"


def base_button_gradient(
    button_name: str = "gradient_button", icon: str = None, on_click=None
):

    base_button = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[Neo_Mint, Deep_Purple],
        ),
        border_radius=10,
        padding=10,
        margin=ft.margin.only(left=15, right=15),
        width=150,
        ink=True,
        on_click=on_click,
        content=ft.Row(
            [
                ft.Icon(icon, color=ft.colors.WHITE) if icon else ft.Container(width=0),
                ft.Text(
                    button_name,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        ),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color=ft.colors.GREY,
            offset=ft.Offset(0, 1),
        ),
    )

    return base_button


def base_button_normal(
    button_name: str = "normal_button",
    icon: str = None,
    on_click=None,
    background_color=None,
    text_color=None,
    icon_color=None,
):

    if background_color is None:
        background_color = White

    if text_color is None:
        if background_color.lower() in ["#ffffff", "white", ft.colors.WHITE]:
            text_color = Black
        else:
            text_color = White

    if icon_color is None:
        icon_color = text_color

    base_button = ft.Container(
        bgcolor=background_color,
        border_radius=10,
        padding=10,
        margin=ft.margin.only(left=15, right=15),
        width=150,
        ink=True,
        on_click=on_click,
        content=ft.Row(
            [
                ft.Icon(icon, color=icon_color) if icon else ft.Container(width=0),
                ft.Text(
                    button_name,
                    color=text_color,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        ),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color=ft.colors.GREY,
            offset=ft.Offset(0, 1),
        ),
    )

    return base_button

def base_button_with_icon(
    button_name: str = "normal_button",
    icon: str = None,
    on_click=None,
    background_color=None,
    text_color=None,
    icon_color=None,
):

    if background_color is None:
        background_color = White

    if text_color is None:
        if background_color.lower() in ["#ffffff", "white", ft.colors.WHITE]:
            text_color = Black
        else:
            text_color = White

    if icon_color is None:
        icon_color = text_color

    base_button = ft.Container(
        expand=True,
        bgcolor=background_color,
        border_radius=10,
        padding=10,
        ink=True,
        on_click=on_click,
        content=ft.Column(
            [
                ft.Row(
                    [ft.Icon(icon, color=icon_color)] if icon else [],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    button_name,
                    color=text_color,
                    size=11,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        ),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color=ft.colors.GREY,
            offset=ft.Offset(0, 1),
        ),
    )

    return base_button
