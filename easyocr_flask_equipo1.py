import os
import cv2
import easyocr
import fitz
import tempfile
from PIL import Image
from flask import Flask, jsonify, request, render_template, send_file
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó ningún archivo PDF'}), 400

    pdf_file = request.files['file']
    pdf_content = pdf_file.read()

    # Guardar el archivo PDF en un archivo temporal
    temp_pdf_file = tempfile.NamedTemporaryFile(delete=False)
    temp_pdf_file.write(pdf_content)
    temp_pdf_file.close()

    try:
        generated_files = pdf2png(temp_pdf_file.name)
    finally:
        os.unlink(temp_pdf_file.name)

    reader = Reader()
    extracted_text_all = []
    extracted_imgs = []

    # Método OCR de extracción para cada archivo de imagen generado
    for generated_file in generated_files:
        img = reader.read_img(generated_file)
        extracted_text, img_bytes = reader.extract_text(img)
        extracted_text_all.extend(extracted_text)
        extracted_imgs.append(img_bytes)

    text = join_txt(extracted_text_all)
    print('###### Extracted text ######')
    print(text)

    temp_txt_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    temp_txt_file.write(text.encode('utf-8'))
    temp_txt_file.close()
    text_file_path = temp_txt_file.name

    # Redireccionar a la página de resultados
    return jsonify(extracted_text=text, extracted_images=extracted_imgs, text_file_path=text_file_path), 200

@app.route('/download_text', methods=['GET'])
def download_text():
    text_file_path = request.args.get('text_file_path')
    return send_file(text_file_path, as_attachment=True)

def pdf2png(pdf_file_path):

    generated_images= []

    pdf_document = fitz.open(pdf_file_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        img = page.get_pixmap(matrix=fitz.Matrix(600 / 300, 600 / 300))
        img_pillow = Image.frombytes("RGB", [img.width, img.height], img.samples)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_img_file:
            img_pillow.save(temp_img_file.name)
            generated_images.append(temp_img_file.name)

    pdf_document.close()
    return sorted(generated_images)


class Reader:
    @staticmethod
    def read_img(img_path):
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def __init__(self):
        languages = ['en', 'es', 'fr', 'de', 'it', 'pt']
        self.reader = easyocr.Reader(languages, model_storage_directory=os.path.join('models'),
                                      download_enabled=True)

    def __call__(self, img):
        return self.extract_text(img)

    def extract_text(self, img, show_text=False, show_confidence=False):
        result = self.reader.readtext(img)
        extracted_text = []

        for text in filter(lambda x: x[-1] > .45, result):
            box, acc_text, confidence = text

            img = cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (0, 255, 0), 2)

            if show_text or show_confidence:
                img = cv2.putText(
                    img,
                    acc_text,
                    (int(box[0][0]), int(box[0][1] - 3)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.5,
                    color=(168, 90, 50),
                    thickness=2
                )

            extracted_text.append(acc_text)

        # Convertir la imagen a bytes
        is_success, buffer = cv2.imencode(".png", img)
        img_bytes = base64.b64encode(buffer).decode("utf-8")

        return extracted_text, img_bytes


def join_txt(text):
    text_joined = ','.join(text)
    text_completion = text_joined[:-1]
    return text_completion

if __name__ == '__main__':
    app.run(debug=True)
