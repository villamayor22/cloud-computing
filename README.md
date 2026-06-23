# cloud-computing
Trabajo de la materia de Cloud Computing - UNINORTE

## Alumno
José Villamayor

## Profesor
Ing. Julio Cesar Saucedo

## Link del tablero de Trello
https://trello.com/invite/b/6a396a2c368524d89e6c9775/ATTI96c5f1c021b3aa5f026ede194b174b0a91E24606/coud-computing

## Descripción de la aplicación
Esta aplicación permite eliminar automáticamente el fondo de imágenes utilizando inteligencia artificial y generar una nueva imagen con fondo transparente en formato PNG.
Una vez procesada la imagen, el archivo resultante se guarda automáticamente en la misma carpeta donde se encuentra la imagen original, facilitando su localización y uso posterior.

### Características principales
- Eliminación automática de fondos de imágenes.
- Exportación en formato PNG con transparencia.
- Interfaz gráfica intuitiva y fácil de usar.
- Guardado automático de la imagen procesada en la ubicación original.
- Procesamiento rápido y eficiente.

### Tecnologías utilizadas
- **Flet**: Desarrollo de la interfaz gráfica multiplataforma.
- **rembg**: Eliminación de fondos mediante modelos de inteligencia artificial.
- **Pillow (PIL)**: Manipulación y procesamiento de imágenes.
- **os**: Gestión de archivos y directorios.
- **asyncio**: Ejecución asíncrona para mejorar la fluidez de la aplicación.

## Cambios o mejoras realizadas
1. Se integró REMBG para el procesamiento y la remoción del fondo de la imagen para convertirlo en .png
2. Se mejoró el estilo de la interfaz, quitando un rectangulo gris que obstruia una parte de la vista
3. Se agregó la barra de progreso y el indicativo de proceso exitoso en la interfaz
4. Se agregó el foton para mostrar la ubicacion del archivo .png

## Requisitos para ejecutar el codigo localmente
1. Tener conexión a internet
2. Tener instalado Python en su Version 3.8 +
3. Clonar el respositorio en tu ordenador, puedes ejecutar este codigo en la terminal integrada de tu editor de codigo (Ej: VsCode):
   ```bash
   git clone <URL_DE_TU_REPOSITORIO_AQUÍ>
   cd <NOMBRE_DE_TU_CARPETA>

4. Instalar las dependencias necesarias para que se pueda ejecutar el programa, utiliza este comando en la terminal integrada de tu editor de codigo:
   ```bash
   pip install flet rembg pillow

5. Ejecuta la aplicación desde la terminal integrada de tu editor de código utilizando el siguiente comando:
```bash
python main.py
