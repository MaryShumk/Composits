import joblib
import numpy as np

# Загрузка обученной модели Random Forest
rf_model = joblib.load("random_forest_model.pkl")

def get_prediction(*features):
    """
    Делает предсказание с использованием обученной модели Random Forest.
    Параметры:
        *features: список значений признаков для предсказания.
    Возвращает:
        float: предсказанное значение.
    """
    # Преобразуем входные признаки в нужный формат (2D-массив)
    input_features = np.array(features).reshape(1, -1)
    prediction = rf_model.predict(input_features)
    return round(prediction[0], 2)