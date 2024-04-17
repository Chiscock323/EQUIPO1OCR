import os
import cv2
import easyocr
import fitz
import tempfile
from PIL import Image
from flask import Flask, jsonify, request, render_template

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
    input_file_name = pdf_file.filename

    # Guardar el archivo PDF en un archivo temporal
    temp_pdf_file = tempfile.NamedTemporaryFile(delete=False)
    temp_pdf_file.write(pdf_content)
    temp_pdf_file.close()

    try:
        generated_files = pdf2png(input_file_name,temp_pdf_file.name)
    finally:
        os.unlink(temp_pdf_file.name)
    
    reader = Reader()
    extracted_text_all = []
    extracted_imgs = []
    
    # Método OCR de extración para cada archivo de imagen generado
    for generated_file in generated_files:
        img = reader.read_img(generated_file)
        extracted_text, _ = reader(img)
        extracted_text_all.extend(extracted_text)
        extracted_imgs.append(img)
                
    text = create_txt(input_file_name, extracted_text_all)
    print('###### Extracted text ######')
    print(text)

    # Redireccionar a la página de resultados
    return jsonify('texto extraido:',text), 200


def pdf2png(file_name,pdf_file_path):
    directory_path = "./Output files/"
    
    base_name = os.path.splitext(os.path.basename(file_name ))[0]
    generated_files = []

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    existing_files = [f for f in os.listdir(directory_path) if f.startswith(base_name) and f.endswith('.png')]

    if existing_files:
        generated_files = [os.path.join(directory_path, f) for f in existing_files]

    pdf_document = fitz.open(pdf_file_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        img = page.get_pixmap(matrix=fitz.Matrix(600/300, 600/300))
        img_pillow = Image.frombytes("RGB", [img.width, img.height], img.samples)

        new_file_name = f"{directory_path}{base_name}_{page_number + 1}.png"

        if os.path.exists(new_file_name):
            continue
        else:
            img_pillow.save(new_file_name, "PNG")
            generated_files.append(new_file_name)

    pdf_document.close()
    return sorted(generated_files)

class Reader:
    @staticmethod
    def read_img(img_path):
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def __init__(self):
        languages = ['en','es','fr','de','it','pt']
        self.reader = easyocr.Reader(languages, model_storage_directory=os.path.join('models'), download_enabled=True)
       
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

        return extracted_text, img

def create_txt(output_file_name, text):
    output_file_path = f"./Output files/{output_file_name[:-4]}.txt"

    text_joined = ','.join(text)
    text_completion = text_joined[:-1]

    with open(output_file_path, 'w') as file2write:
        file2write.write(text_completion)

    return text_completion

if __name__ == '__main__':
    app.run(debug=True)
