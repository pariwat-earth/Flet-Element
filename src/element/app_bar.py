import flet as ft

from element.constance import Deep_Purple, Neo_Mint

manager_name = "ปริวัฒน์"

def appbar(title_name = "หนูพุกใหญ่พรหมพิราม"):
    gradient_container = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[Neo_Mint, Deep_Purple],
        ),
        width=None,
        height=100,
        border_radius=0,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    title_name, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
                ),
                ft.Text(
                    f"ยินดีต้อนรับ คุณ{manager_name}", size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
                )
            ],
            # alignment=ft.MainAxisAlignment.START,
            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return gradient_container
