import os
from flask import Flask, jsonify

app = Flask(__name__)

autos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "anio": 2022, "combustible": "Bencina", "precio": 15000000},
    {"id": 2, "marca": "Tesla", "modelo": "Model 3", "anio": 2023, "combustible": "Eléctrico", "precio": 35000000},
    {"id": 3, "marca": "Hyundai", "modelo": "Accent", "anio": 2021, "combustible": "Bencina", "precio": 12000000},
    {"id": 4, "marca": "Chevrolet", "modelo": "Spark", "anio": 2020, "combustible": "Bencina", "precio": 9000000},
    {"id": 5, "marca": "Kia", "modelo": "Rio", "anio": 2022, "combustible": "Bencina", "precio": 13000000},
    {"id": 6, "marca": "Ford", "modelo": "Ranger", "anio": 2023, "combustible": "Diesel", "precio": 28000000},
    {"id": 7, "marca": "BMW", "modelo": "X5", "anio": 2023, "combustible": "Bencina", "precio": 60000000},
    {"id": 8, "marca": "Audi", "modelo": "A4", "anio": 2022, "combustible": "Bencina", "precio": 40000000},
    {"id": 9, "marca": "Mercedes-Benz", "modelo": "C-Class", "anio": 2023, "combustible": "Bencina", "precio": 45000000},
    {"id": 10, "marca": "Nissan", "modelo": "Versa", "anio": 2021, "combustible": "Bencina", "precio": 11000000},
    {"id": 11, "marca": "Mazda", "modelo": "CX-5", "anio": 2022, "combustible": "Bencina", "precio": 25000000},
    {"id": 12, "marca": "Volkswagen", "modelo": "Golf", "anio": 2021, "combustible": "Bencina", "precio": 20000000},
    {"id": 13, "marca": "Subaru", "modelo": "Forester", "anio": 2023, "combustible": "Bencina", "precio": 27000000},
    {"id": 14, "marca": "Peugeot", "modelo": "208", "anio": 2022, "combustible": "Bencina", "precio": 14000000},
    {"id": 15, "marca": "Renault", "modelo": "Duster", "anio": 2021, "combustible": "Diesel", "precio": 18000000},
    {"id": 16, "marca": "Jeep", "modelo": "Wrangler", "anio": 2023, "combustible": "Bencina", "precio": 50000000},
    {"id": 17, "marca": "Volvo", "modelo": "XC60", "anio": 2023, "combustible": "Híbrido", "precio": 55000000},
    {"id": 18, "marca": "Honda", "modelo": "Civic", "anio": 2022, "combustible": "Bencina", "precio": 22000000},
    {"id": 19, "marca": "Suzuki", "modelo": "Swift", "anio": 2021, "combustible": "Bencina", "precio": 10000000},
    {"id": 20, "marca": "Mitsubishi", "modelo": "L200", "anio": 2023, "combustible": "Diesel", "precio": 26000000},
    {"id": 21, "marca": "Chery", "modelo": "Tiggo 2", "anio": 2022, "combustible": "Bencina", "precio": 9000000},
    {"id": 22, "marca": "BYD", "modelo": "Dolphin", "anio": 2023, "combustible": "Eléctrico", "precio": 20000000},
    {"id": 23, "marca": "Great Wall", "modelo": "Poer", "anio": 2023, "combustible": "Diesel", "precio": 24000000},
    {"id": 24, "marca": "Mini", "modelo": "Cooper", "anio": 2022, "combustible": "Bencina", "precio": 30000000},
    {"id": 25, "marca": "Porsche", "modelo": "911", "anio": 2023, "combustible": "Bencina", "precio": 120000000}
]

@app.route('/')
def home():
    return jsonify({"mensaje de verificación": "API de Autos funcionando!!!"})

@app.route('/autos')
def get_autos():
    return jsonify(autos)

@app.route('/autos/<int:id>')
def get_auto(id):
    auto = next((a for a in autos if a["id"] == id), None)
    if auto:
        return jsonify(auto)
    return jsonify({"error": "Auto no encontrado"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)