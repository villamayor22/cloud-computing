import flet as ft
from rembg import remove
from PIL import Image
import os

async def main(page: ft.Page):
    page.title = "BgRemover - Quitar Fondo de Imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"

    titulo = ft.Text("Quitar Fondo a Imágenes", style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.BOLD)
    status_text = ft.Text("Selecciona una imagen para empezar...", color=ft.Colors.GREY_600)
    
    img_original = ft.Image(src="", width=250, height=250, fit=ft.BoxFit.CONTAIN, visible=False)
    img_procesada = ft.Image(src="", width=250, height=250, fit=ft.BoxFit.CONTAIN, visible=False)
    
    # Guardaremos la ruta de la imagen procesada de manera global en la sesión
    path_procesada = ft.Ref[str]()

    async def on_file_click(e):
        files = await ft.FilePicker().pick_files(allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg"])
        if files:
            input_path = files[0].path
            status_text.value = "Procesando imagen... Por favor, espera."
            page.update()
            
            try:
                # Mostrar la original
                img_original.src = input_path
                img_original.visible = True
                
                # Procesar remoción de fondo
                output_path = os.path.join(os.path.dirname(input_path), "temp_nobg.png")
                input_image = Image.open(input_path)
                output_image = remove(input_image)
                output_image.save(output_path)
                
                # Guardar ruta del archivo temporal
                path_procesada.current = output_path
                
                # Mostrar la procesada
                img_procesada.src = output_path
                img_procesada.visible = True
                status_text.value = "¡Fondo removido con éxito!"
            except Exception as ex:
                status_text.value = f"Error al procesar: {str(ex)}"
                status_text.color = ft.Colors.RED_400
                
            page.update()

    btn_cargar = ft.Button(
        "Seleccionar Imagen",
        icon=ft.Icons.IMAGE,
        on_click=on_file_click
    )

    page.add(
        titulo,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        btn_cargar,
        status_text,
        ft.Row([
            ft.Column([ft.Text("Original"), img_original], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.VerticalDivider(width=20),
            ft.Column([ft.Text("Sin Fondo"), img_procesada], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.run(main)
