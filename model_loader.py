import joblib
import numpy as np

# Загрузка обученной модели Random Forest и нормализатора
rf_model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

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
    
    # Проверка количества признаков
    if input_features.shape[1] != 12:
        raise ValueError("Ожидается 12 признаков для ввода.")
    
    # Нормализация только признаков
    input_features_normalized = scaler.transform(input_features)
    
    # Предсказание
    prediction = rf_model.predict(input_features_normalized)
    return round(prediction[0], 2)
