
# EQUIPO 1 - EasyOCR con servicio web en Flask

## Aplicación de OCR con Flask

Esta aplicación web, desarrollada por el Equipo 1, ofrece un servicio que permite a los usuarios cargar archivos PDF y extraer texto utilizando OCR a través de EasyOCR.

## Características

- Carga de archivos PDF a través de una interfaz web intuitiva.
- Conversión de páginas de PDF a imágenes PNG para procesamiento OCR.
- Extracción de texto utilizando EasyOCR.
- Visualización del texto extraído y las imágenes procesadas en la página web.

## Funcionamiento
Diagrama de secuencia sobre la comunicación y procesos del servidor.
![](https://github.com/Chiscock323/EQUIPO1OCR/blob/main/Diagrama%20funcionamiento.png)

- Usuario envía PDF: El usuario selecciona un archivo PDF en la interfaz web y lo sube al servidor. Esto se hace a través del navegador web que envía una solicitud POST a la ruta /upload_pdf del servidor Flask.
- Almacenamiento temporal de PDF: El servidor Flask recibe el archivo PDF y lo almacena temporalmente en el sistema de archivos del servidor para su procesamiento.
- Conversión de PDF a PNG: Se llama a la función pdf2png() para convertir cada página del PDF en una imagen PNG. Esta función utiliza la biblioteca fitz (PyMuPDF) para leer el PDF y extraer cada página como una imagen.
- Procesamiento OCR de imágenes: Las imágenes PNG generadas se procesan utilizando EasyOCR. La clase Reader, definida en el servidor, utiliza EasyOCR para detectar y extraer texto de las imágenes.
- Almacenamiento temporal de resultados: El texto extraído y las imágenes resultantes se almacenan temporalmente en el servidor. Esto incluye el texto reconocido y las imágenes procesadas, que pueden ser dibujadas con cuadros alrededor del texto reconocido.
- Envío de resultados al navegador: El servidor Flask compila los resultados (texto y referencias a las imágenes procesadas) y los envía de vuelta al navegador como una respuesta JSON. Esta respuesta incluye el texto extraído, las imágenes procesadas (en base64 si se incluyen directamente en la respuesta) y la ruta al archivo de texto temporal donde se ha guardado el texto extraído.
- Visualización de resultados: Finalmente, el navegador del usuario recibe los datos y los muestra en la interfaz web. Esto incluye mostrar las imágenes procesadas y ofrecer opciones para descargar el texto extraído o las imágenes.

Diagrama de bloque sobre la estructura de procesos (clases, métodos, funciones, entradas y salidas).
![](https://github.com/Chiscock323/EQUIPO1OCR/blob/main/diagrama_bloque_easyocr_equipo1.png)

### Prerrequisitos

- Python 3.6 o superior (solo para ejecución, no se requiere instalación de dependencias).
- Al menos 2 GB de espacio libre en disco para la ejecución y almacenamiento de los archivos procesados.
- Acceso a una cuenta de Gmail para la utilización de Google Drive.

### Instalación
- Revise el INSTALL.md para seguir los pasos de instalación y ejecución del servidor.

### Notas Importantes

- El ejecutable incluye todas las dependencias necesarias para correr la aplicación, por lo que no necesitarás realizar ninguna instalación adicional.
- Asegúrate de tener permisos adecuados para ejecutar el archivo `.exe` en tu sistema.

## Autores

- Angel Sandria, Francisco Morales, Eduardo Morato, Eliseo Ortíz

## Contacto

- [202060400@ucc.mx]

Si tienes preguntas o necesitas asistencia, por favor contacta al equipo a través del correo proporcionado.

