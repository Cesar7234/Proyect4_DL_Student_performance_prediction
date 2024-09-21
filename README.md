# Proyecto de Predicción de Rendimiento Estudiantil

Este proyecto utiliza técnicas de Deep Learning para predecir el índice de rendimiento de estudiantes basado en varios factores.

## Descripción

El proyecto consta de dos partes principales:
1. Un modelo de Deep Learning entrenado con datos de rendimiento estudiantil.
2. Una API FastAPI que sirve el modelo para hacer predicciones en tiempo real.

## Estructura del Proyecto

```
student-performance-prediction/
│
├── train_model.py
├── api.py
├── student_performance_model.h5
├── preprocessor.joblib
├── requirements.txt
└── README.md
```

## Requisitos

Para ejecutar este proyecto, necesitarás Python 3.7+ y las siguientes bibliotecas:

- tensorflow
- pandas
- numpy
- scikit-learn
- fastapi
- uvicorn

Puedes instalar todas las dependencias con:

```
pip install -r requirements.txt
```

## Uso

### Entrenamiento del Modelo

Para entrenar el modelo, ejecuta:

```
python train_model.py
```

Esto creará los archivos `student_performance_model.h5` y `preprocessor.joblib`.

### Ejecución de la API

Para iniciar el servidor de la API, ejecuta:

```
python api.py
```

El servidor se iniciará en `http://localhost:8000`.

### Hacer Predicciones

Puedes hacer predicciones enviando una solicitud POST a `http://localhost:8000/predict` con un JSON que contenga los datos del estudiante. Ejemplo:

```json
{
  "hours_studied": 6.5,
  "previous_scores": 85,
  "extracurricular_activities": "Yes",
  "sleep_hours": 7.5,
  "sample_question_papers_practiced": 5
}
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)