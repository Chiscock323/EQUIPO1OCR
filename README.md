
# EQUIPO 1 - EasyOCR con servicio web en Flask

## Aplicación de OCR con Flask

Esta aplicación web, desarrollada por el Equipo 1, ofrece un servicio que permite a los usuarios cargar archivos PDF y extraer texto utilizando OCR a través de EasyOCR.

## Características

- Carga de archivos PDF a través de una interfaz web intuitiva.
- Conversión de páginas de PDF a imágenes PNG para procesamiento OCR.
- Extracción de texto utilizando EasyOCR.
- Visualización del texto extraído y las imágenes procesadas en la página web.

## Instalación y Uso

### Prerrequisitos

- Python 3.6 o superior (solo para ejecución, no se requiere instalación de dependencias).
- Al menos 2 GB de espacio libre en disco para la ejecución y almacenamiento de los archivos procesados.
- Acceso a una cuenta de Gmail para la utilización de Google Drive.

### Configuración del entorno y Ejecución

1. Descarga el archivo ZIP del proyecto desde el siguiente enlace de Google Drive:

   [Enlace de descarga de Google Drive](https://drive.google.com/file/d/1LyVNSAUMfIihBpZw5nfy7QSSSR3qiRF5/view?usp=sharing)

2. Una vez descargado, extrae el contenido del archivo ZIP en tu sistema.

3. Navega a la carpeta donde se extrajo el archivo, específicamente al directorio `dist` dentro de `EasyOCR-Flask-Equipo1UCC`:

cd ruta/a/EasyOCR-Flask-Equipo1UCC/EasyOCR-Flask-Equipo1UCC/dist/easyocr_flask_equipo1

4. Ejecuta el archivo `easyocr_flask_equipo1.exe`. Al hacerlo, se abrirá una consola de comandos y se iniciará automáticamente el servidor de Flask.

5. Con el servidor en ejecución, abre tu navegador y visita:

http://127.0.0.1:5000/


6. En la página web que se abre, sigue estos pasos para cargar y procesar un archivo PDF:
- Haz clic en el botón "Seleccionar archivo" para elegir un archivo PDF desde tu computadora.
- Después de seleccionar el archivo, haz clic en el botón "Enviar" para subir el archivo y comenzar el proceso de OCR.
- Espera mientras el servidor procesa el archivo. Una vez completado, la página web mostrará el texto extraído en formato JSON y las imágenes resultantes de la conversión de PDF a PNG.


Resultado 
se obtienen y reproducen las imágenes generadas en la página para descargar, se muestra el archivo txt para descargar, se recibe un json con las imágenes codificadas en base64 y el texto extraído en un response

### Notas Importantes

- El ejecutable incluye todas las dependencias necesarias para correr la aplicación, por lo que no necesitarás realizar ninguna instalación adicional.
- Asegúrate de tener permisos adecuados para ejecutar el archivo `.exe` en tu sistema.

## Autores

- Angel Sandria, Francisco Morales, Eduardo Morato, Eliseo Ortíz

## Contacto

- [202060400@ucc.mx]

Si tienes preguntas o necesitas asistencia, por favor contacta al equipo a través del correo proporcionado.

