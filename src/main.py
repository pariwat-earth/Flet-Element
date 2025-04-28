import flet as ft

from element.base_box import base_empty_box, base_info_report_box
from element.base_button import (
    base_button_gradient,
    base_button_normal,
    base_button_with_icon,
)
from element.base_appbar import base_appbar
from element.constance import Deep_Purple, Neo_Mint, White

page_name = "ฟาร์มรัก"


def print_name(e):
    print(page_name)


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
                [
                    base_appbar(page_name),
                    base_empty_box(5),
                    ft.Row(
                        [
                            base_empty_box(2),
                            base_button_with_icon("ผสมพันธุ์ใหม่", "FAVORITE", print_name),
                            base_button_with_icon("เพิ่มหนูใหม่", "ADD_CIRCLE", print_name),
                            base_button_with_icon("บันทึกสุขภาพ", "LOCAL_HOSPITAL", print_name),
                            base_button_with_icon("รายงาน", "LIBRARY_BOOKS", print_name),
                            base_empty_box(2),
                        ],
                    ),
                    base_empty_box(5),
                    base_button_gradient(
                        "เพิ่มฟาร์มใหม่", "ADD_CIRCLE_OUTLINE", print_name
                    ),
                    base_empty_box(5),
                    base_button_normal("ยกเลิก", "", print_name),
                    base_empty_box(5),
                    base_button_normal(
                        "เพิ่มการผสมพันธุ์", "ADD_CIRCLE_OUTLINE", print_name, Neo_Mint
                    ),
                    base_empty_box(5),
                    base_button_normal(
                        "แนะนำคู่ผสมพันธุ์", "FAVORITE_BORDER", print_name, Deep_Purple
                    ),
                    base_empty_box(5),
                    ft.Row(
                        [
                            base_empty_box(2),
                            base_info_report_box(
                                "จำนวนหนูทั้งหมด",
                                "128",
                                "ตัว",
                                Neo_Mint,
                            ),
                            base_info_report_box(
                                "บ่อเลี้ยงที่ใช้งาน",
                                "12",
                                "/15 บ่อ",
                                Deep_Purple,
                            ),
                            base_empty_box(2),
                        ]
                    ),
                ],
                spacing=0,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                expand=True,
            ),
            expand=True,
        )
    )


ft.app(main)
