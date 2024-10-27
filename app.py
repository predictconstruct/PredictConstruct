from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload-schedule', methods=['POST'])
def upload_schedule():
    project_name = request.form['projectName']
    deadline = request.form['deadline']
    milestones = request.form['milestones']
    
    # Guardar el archivo subido
    file = request.files['file']
    file.save(f"./uploads/{file.filename}")  # Asegúrate de crear la carpeta uploads

    # Procesar el archivo (por ejemplo, un CSV)
    df = pd.read_csv(f"./uploads/{file.filename}")
    
    # Aquí agregarías lógica para analizar el cronograma y usar IA
    
    return jsonify({"message": "Datos cargados exitosamente"})

if __name__ == "__main__":
    app.run(debug=True)
