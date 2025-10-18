from flask import Flask, request, Response
from dataclasses import dataclass
from Src.Logics.factory_entities import factory_entities
app = Flask(__name__)
#тестовые модели
@dataclass
class Nomenclature:
    name: str
    code: str
    price: float

@dataclass
class Unit:
    name: str
    symbol: str
#данные
NOMENCLATURE_DATA = [
    Nomenclature("Item1", "A001", 100.0),
    Nomenclature("Item2", "B002", 200.0),
    Nomenclature("Item3", "C003", 300.0)
]

UNIT_DATA = [
    Unit("Kilogram", "kg"),
    Unit("Meter", "m"),
    Unit("Piece", "pc")
]
factory = factory_entities()
@app.route("/api/accessibility", methods=['GET'])
def accessibility():
    return "GOOD JOB"
@app.route("/api/data", methods=['GET'])
def get_data():
    entity_type = request.args.get("type", "nomenclature").lower()
    fmt = request.args.get("format", "json").lower()
    # Выбираем данные
    if entity_type == "nomenclature":
        data = NOMENCLATURE_DATA
    elif entity_type == "unit":
        data = UNIT_DATA
    else:
        return f"Неизвестный тип сущности: {entity_type}", 400

    #cоздаём объект ответа
    try:
        response_obj = factory.create(fmt)
        text = response_obj.build(fmt, data)
        mime = "text/plain"
        if fmt == "json":
            mime = "application/json"
        return Response(text, mimetype=mime)
    except Exception as e:
        return f"Ошибка при формировании данных: {e}", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
