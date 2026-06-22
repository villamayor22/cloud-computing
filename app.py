import flet as ft
from rembg import remove
from PIL import Image
import os

async def main(page: ft.Page):
    page.title = "BgRemover - Quitar Fondo de Imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20  # Un poco de margen para que no quede pegado a los bordes

    # 1. FIX: Se crea el FilePicker una sola vez fuera del handler.
    # Crearlo dentro del clic causa un TimeoutException en modo web.
    file_picker = ft.FilePicker()

    async def on_file_click(e):
        # Deshabilitar el botón para evitar clics múltiples mientras se procesa
        btn_cargar.disabled = True
        page.update()
        
        try:
            # 2. FIX: Se usa pick_files() en lugar de pick_files_async() 
            # (en Flet actual el método ya es asíncrono por defecto).
            files = await file_picker.pick_files(
                allow_multiple=False, 
                allowed_extensions=["png", "jpg", "jpeg"]
            )
            
            if files:
                input_path = files[0].path
                
                if not input_path:
                    print("Error: La ruta del archivo no está disponible.")
                    return

                # Guardar el archivo en el mismo directorio que el original
                output_path = os.path.join(os.path.dirname(input_path), "imagen_sin_fondo.png")
                
                input_image = Image.open(input_path)
                output_image = remove(input_image)
                output_image.save(output_path)
                
                print(f"¡Fondo removido con éxito! Imagen guardada en: {output_path}")
                
        except Exception as ex:
            print(f"Error al procesar la imagen: {str(ex)}")
        finally:
            # Volver a habilitar el botón al terminar (éxito o error)
            btn_cargar.disabled = False
            page.update()

    # 3. FIX: Se cambia 'style' por 'theme_style' para usar correctamente el enum
    titulo = ft.Text(
        "Selecciona la imagen para quitar el fondo", 
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE, 
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    btn_cargar = ft.ElevatedButton(
        "Seleccionar Imagen",
        icon=ft.Icons.UPLOAD_FILE,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        on_click=on_file_click
    )

    # Interfaz simplificada: solo título y botón
    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                btn_cargar
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    )

if __name__ == "__main__":
    ft.app(main)
