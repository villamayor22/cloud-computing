import flet as ft
from rembg import remove
from PIL import Image
import os
import asyncio

async def main(page: ft.Page):
    page.title = "BgRemover - Quitar Fondo de Imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    file_picker = ft.FilePicker()

    # Componentes de progreso
    progress_bar = ft.ProgressBar(width=300, color=ft.Colors.BLUE_600, bgcolor=ft.Colors.GREY_200, visible=False)
    progress_text = ft.Text("", size=14, color=ft.Colors.BLUE_600, visible=False)
    success_icon = ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_600, size=48, visible=False)
    success_text = ft.Text("¡Listo!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600, visible=False)
    success_text_2 = ft.Text("Guardado en la misma carpeta que contiene tu imagen", size=12, color=ft.Colors.GREEN_600, visible=False)

    async def simulate_progress():
        """Simula el progreso mientras se procesa la imagen"""
        for i in range(0, 101, 5):
            progress_bar.value = i / 100
            progress_text.value = f"Procesando... {i}%"
            page.update()
            await asyncio.sleep(0.1)

    async def on_file_click(e):
        btn_cargar.disabled = True
        progress_bar.visible = True
        progress_text.visible = True
        success_icon.visible = False
        success_text.visible = False
        progress_bar.value = 0
        page.update()
        
        try:
            files = await file_picker.pick_files(
                allow_multiple=False, 
                allowed_extensions=["png", "jpg", "jpeg"]
            )
            
            if files:
                input_path = files[0].path
                
                if not input_path:
                    print("Error: La ruta del archivo no está disponible.")
                    return

                output_path = os.path.join(os.path.dirname(input_path), "imagen_sin_fondo.png")
                
                # Iniciar tarea de progreso en segundo plano
                progress_task = asyncio.create_task(simulate_progress())
                
                # Ejecutar el procesamiento pesado
                input_image = Image.open(input_path)
                output_image = remove(input_image)
                output_image.save(output_path)
                
                # Esperar a que termine la simulación de progreso
                await progress_task
                
                # Completar la barra al 100%
                progress_bar.value = 1.0
                progress_text.value = "Procesando... 100%"
                page.update()
                await asyncio.sleep(0.3)
                
                # Ocultar progreso y mostrar éxito
                progress_bar.visible = False
                progress_text.visible = False
                success_icon.visible = True
                success_text.visible = True
                success_text_2.visible = True
                
                print(f"¡Fondo removido con éxito! Imagen guardada en: {output_path}")
                
        except Exception as ex:
            print(f"Error al procesar la imagen: {str(ex)}")
            progress_bar.visible = False
            progress_text.visible = False
        finally:
            btn_cargar.disabled = False
            page.update()

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

    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                btn_cargar,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                progress_bar,
                progress_text,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                success_icon,
                success_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )
    )

if __name__ == "__main__":
    ft.app(main)
