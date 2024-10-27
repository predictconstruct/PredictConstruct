from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ruta para cargar cronograma
@app.route('/upload-schedule', methods=['POST'])
def upload_schedule():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Guardar el archivo en la carpeta 'uploads'
    file.save(os.path.join('uploads', file.filename))

    # Aquí es donde agregarías la lógica para procesar el archivo

    return jsonify({'message': 'Archivo cargado con éxito!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
