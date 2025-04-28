import flet as ft

from element.constance import *


def base_empty_box(margin: ft.Margin = None):
    if margin is None:
        margin = ft.margin.only(left=0, right=0, top=0, bottom=0)

    empty_box = ft.Container(
        width=0,
        height=0,
        bgcolor="#FFFFFF",
        margin=margin,
    )

    return empty_box


def base_info_report_box(topic: str, content: str, units: str = None, color: str = None):
    if units is None:
        units = ""
    else:
        units = f" {units}"

    info_report_box = ft.Container(
        expand=True,
        bgcolor=White,
        border_radius=10,
        padding=ft.padding.all(10),
        content=ft.Column(
            [
                ft.Text(
                    topic,
                    size=11,
                    color=Grey,
                    weight=ft.FontWeight.NORMAL,
                ),
                ft.Row(
                    [
                        ft.Text(
                            content,
                            size=15,
                            color=Back,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            units,
                            size=11,
                            color=Grey,
                            weight=ft.FontWeight.NORMAL,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                ),
            ],
            spacing=5,
            tight=True,
        ),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=2,
            color=color,
            offset=ft.Offset(0, 3), 
        ),
    )
    return info_report_box
