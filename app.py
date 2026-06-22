import flet as ft

async def main(page: ft.Page):
    page.title = "BgRemover - Quitar Fondo de Imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"

    # Componentes de la interfaz
    titulo = ft.Text("Quitar Fondo a Imágenes", style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.BOLD)
    status_text = ft.Text("Selecciona una imagen para empezar...", color=ft.Colors.GREY_600)
    
    # Marcadores de posición para las imágenes
    img_original = ft.Image(src="", width=50, height=50, fit=ft.BoxFit.CONTAIN, visible=False)
    
    # Manejador de selección de archivos
    async def on_file_click(e):
        files = await ft.FilePicker().pick_files(allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg"])
        if files:
            img_original.src = files[0].path
            img_original.visible = True
            status_text.value = f"Imagen cargada: {files[0].name}"
            await page.update_async()

    btn_cargar = ft.Button(
        "Seleccionar Imagen",
        icon=ft.Icons.IMAGE,
        on_click=on_file_click
    )

    # Agregar elementos a la página
    page.add(
        titulo,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        btn_cargar,
        status_text,
        ft.Row([img_original], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.run(main)