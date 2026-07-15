import flet as ft

from ui.libro_form import libro_form

def main_window(page: ft.Page):
    # Configurar pagina
    page.title = "Sistema de Gestion de Biblioteca"
    page.window_width = 1100
    page.window_height = 700
    page. padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #Elementos del contenedor principal

    titulo = ft.Text(
        "Sistema de getion de biblioteca",
        size = 24,
        weight = ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opcion del manu",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Creacon del contenedor principal
    contenido = ft.Container(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing= 10,
        ),
        padding = 30,
        expand = True
    )

    def mostrar_formulario_libro(e):
        contenido.content = libro_form()
        page.update()

    # Creacion del menu lateral
    menu_lateral = ft.Container(
        width= 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls =[
                ft.Text(
                "Biblioteca",
                size = 22,
                weight = ft.FontWeight.BOLD,
                color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de Gestion",
                    size = 12,
                    color = ft.Colors.WHITE
                ),
                ft.Divider(color=ft.Colors.BLUE_GREY_700),
                #botones
                ft.ElevatedButton(
                    "Libros",
                    icon=ft.Icons.BOOK,
                    width = 180,
                    on_click= mostrar_formulario_libro
                ),
                ft.ElevatedButton(
                    "Usuarios",
                    icon=ft.Icons.PERSON,
                    width = 180
                ),
                ft.ElevatedButton(
                    "Prestamos",
                    icon=ft.Icons.SWAP_HORIZ,
                    width = 180
                ),
                ft.ElevatedButton(
                    "Devoluciones",
                    icon=ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),
            ],
            spacing=15
        )
    )

    # Layout de la pagina
    layout = ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand=True
    )

    page.add(layout)