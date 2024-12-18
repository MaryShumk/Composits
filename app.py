from flask import Flask, render_template, request
from model_loader import get_prediction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    message = None
    values = {}

    if request.method == "POST":
        try:
            # Список полей формы
            fields = [
                "Matrix_Filler_Ratio", "Density", "Elastic_Modulus", "Hardener_Content",
                "Epoxy_Group_Content", "Flash_Point_Temperature", "Surface_Density",
                "Tensile_Elastic_Modulus", "Resin_Consumption", "Stripe angle",
                "Stitch_Pitch", "Stitch_Density"
            ]

            values = {field: request.form.get(field) for field in fields}

            # Проверка заполнения всех полей
            if any(value is None or value.strip() == "" for value in values.values()):
                error = "Все поля обязательны к заполнению"
            else:
                # Получаем предсказание с использованием модели
                features = [float(values[field]) for field in fields]
                prediction = get_prediction(*features)
                message = f"Прогнозируемая прочность при растяжении, МПа составляет {prediction} МПа"

        except Exception as e:
            error = f"Ошибка: {str(e)}"

    return render_template("index.html", message=message, error=error, values=values)

if __name__ == "__main__":
    app.run(debug=True)
