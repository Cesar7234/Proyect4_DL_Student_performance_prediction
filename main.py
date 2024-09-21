from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd


app = FastAPI()

# Cargar el modelo y el preprocesador
model = load_model('D:/Documentos/Ai Labs/Clases/Sesión 13 cuatro proyectos/Proyecto 4 Regresión DL v2/student_performance_model.h5')
preprocessor = joblib.load('D:/Documentos/Ai Labs/Clases/Sesión 13 cuatro proyectos/Proyecto 4 Regresión DL v2/preprocessor.joblib')

class StudentFeatures(BaseModel):
    hours_studied: float
    previous_scores: float
    extracurricular_activities: str
    sleep_hours: float
    sample_question_papers_practiced: int

@app.post("/predict")
async def predict_performance(student: StudentFeatures):
    try:
        # Convertir los datos de entrada en un DataFrame
        input_data = np.array([[
            student.hours_studied,
            student.previous_scores,
            student.extracurricular_activities,
            student.sleep_hours,
            student.sample_question_papers_practiced
        ]])
        input_df = pd.DataFrame(input_data, columns=[
            'Hours Studied', 'Previous Scores', 'Extracurricular Activities',
            'Sleep Hours', 'Sample Question Papers Practiced'
        ])

        # Preprocesar los datos
        input_preprocessed = preprocessor.transform(input_df)

        # Hacer la predicción
        prediction = model.predict(input_preprocessed)

        return {"predicted_performance_index": float(prediction[0][0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)