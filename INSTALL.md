 ##Instalación y Uso

### Prerrequisitos

- Python 3.6 o superior (solo para ejecución, no se requiere instalación de dependencias).
- Al menos 2 GB de espacio libre en disco para la ejecución y almacenamiento de los archivos procesados.
- 

### Configuración del entorno y Ejecución

Clonar el repositorio.

1.Desde la línea de comandos, usa el siguiente comando para clonar el repositorio:

git clone https://github.com/Chiscock323/EQUIPO1OCR.git

2.(Opcional) Crear un ambiente virtualizado en python

En Windows, ejecuta

python -m venv <ruta>/env
<ruta>/env/Scripts/activate

En Linux, ejecuta:

python3 -m venv <ruta>/env
source <ruta>/env/bin/activate

3.Instalar las dependencias necesarias.
Para instalar las librerías y módulos necesarios, usa el archivo de requerimientos:

pip install -r requirements.txt

4.Ejecutar el servidor.
Una vez instaladas las dependencias, accede a la ruta del proyecto y ejecuta el servidor:

cd EQUIPO10CR-main

ejecuta el archivo :

easyocr_flask_equipo1.py

5. Con el servidor en ejecución, abre tu navegador y visita:
http://127.0.0.1:5000/

6.Desde un API Client, POSTMAN de preferencia, por método POST mandamos el archivo pdf a extraer el texto al endpoint siguiente: http://localhost:5000/.

7. En la página web que se abre, sigue estos pasos para cargar y procesar un archivo PDF:
- Haz clic en el botón "Seleccionar archivo" para elegir un archivo PDF desde tu computadora.
- Después de seleccionar el archivo, haz clic en el botón "Enviar" para subir el archivo y comenzar el proceso de OCR.
- Espera mientras el servidor procesa el archivo. Una vez completado, la página web mostrará el texto extraído en formato JSON y las imágenes resultantes de la conversión de PDF a PNG.


Resultado 
se obtienen y reproducen las imágenes generadas en la página para descargar, se muestra el archivo txt para descargar, se recibe un json con las imágenes codificadas en base64 y el texto extraído en un response
