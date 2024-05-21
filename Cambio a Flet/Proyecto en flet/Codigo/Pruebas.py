import flet as ft

def VerPantallaPersonal(page: ft.Page):
    def volver_atras(e):
        page.views.pop()
        page.update()

    return ft.View(
        appbar=ft.AppBar(
            title=ft.Text("Personal del Hospital", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.GREEN,
            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=volver_atras),
            actions=[
                ft.IconButton(icon=ft.icons.PERSON)
            ]
        ),
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Bacteriólogo.jpg", width=400, height=200),
                                        margin=ft.EdgeInsets.only(left=20),  # Desplaza la imagen a la derecha
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Bacteriólogos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 14", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los bacteriólogos se encargan de analizar muestras biológicas para detectar y diagnosticar enfermedades. "
                                                "Su trabajo es crucial para la identificación de patógenos y la prevención de brotes infecciosos. "
                                                "Ellos trabajan en laboratorios de microbiología, realizando cultivos y pruebas bioquímicas para proporcionar diagnósticos precisos.",
                                                width=300,
                                                height=200,
                                                color=ft.colors.BLACK,
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                        margin=ft.EdgeInsets.only(top=20)  # Mueve el texto hacia arriba
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(src="path/to/medico_image.png", width=100, height=300),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Médicos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Trabajadores disponibles: 20"),
                                            ft.Text(
                                                "Los médicos son responsables de la atención primaria y el diagnóstico de enfermedades. "
                                                "Ellos se aseguran de que los pacientes reciban el cuidado necesario y coordinan con otros especialistas para tratamientos más complejos."
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Añadir más contenedores similares para otras profesiones
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(src="path/to/medico_image.png", width=100, height=300),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Médicos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Trabajadores disponibles: 20"),
                                            ft.Text(
                                                "Los médicos son responsables de la atención primaria y el diagnóstico de enfermedades. "
                                                "Ellos se aseguran de que los pacientes reciban el cuidado necesario y coordinan con otros especialistas para tratamientos más complejos."
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                    ],
                    alignment="start",
                    spacing=10,
                    scroll=ft.ScrollMode.ALWAYS,
                ),
                padding=10,
                expand=True,
            )
        ]
    )

# Supongamos que el archivo main.py ya incluye una referencia a VerPantallaPersonal
if __name__ == "__main__":
    ft.app(target=VerPantallaPersonal)