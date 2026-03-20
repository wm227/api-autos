from flask import Flask, jsonify

app = Flask(__name__)

autos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "combustible": "Bencina", "precio": 15000000},
    {"id": 2, "marca": "Toyota", "modelo": "Hilux", "combustible": "Diésel", "precio": 25000000},
    {"id": 3, "marca": "Hyundai", "modelo": "Accent", "combustible": "Bencina", "precio": 12000000},
    {"id": 4, "marca": "Hyundai", "modelo": "Tucson", "combustible": "Diésel", "precio": 22000000},
    {"id": 5, "marca": "Kia", "modelo": "Rio", "combustible": "Bencina", "precio": 11000000},
    {"id": 6, "marca": "Kia", "modelo": "Sportage", "combustible": "Diésel", "precio": 23000000},
    {"id": 7, "marca": "Chevrolet", "modelo": "Spark", "combustible": "Bencina", "precio": 9000000},
    {"id": 8, "marca": "Chevrolet", "modelo": "Silverado", "combustible": "Bencina", "precio": 35000000},
    {"id": 9, "marca": "Ford", "modelo": "Ranger", "combustible": "Diésel", "precio": 28000000},
    {"id": 10, "marca": "Ford", "modelo": "Mustang", "combustible": "Bencina", "precio": 40000000},
    {"id": 11, "marca": "Nissan", "modelo": "Versa", "combustible": "Bencina", "precio": 13000000},
    {"id": 12, "marca": "Nissan", "modelo": "Navara", "combustible": "Diésel", "precio": 27000000},
    {"id": 13, "marca": "Mazda", "modelo": "Mazda3", "combustible": "Bencina", "precio": 18000000},
    {"id": 14, "marca": "Mazda", "modelo": "CX-5", "combustible": "Diésel", "precio": 26000000},
    {"id": 15, "marca": "BMW", "modelo": "Serie 3", "combustible": "Bencina", "precio": 42000000},
    {"id": 16, "marca": "BMW", "modelo": "X5", "combustible": "Diésel", "precio": 60000000},
    {"id": 17, "marca": "Audi", "modelo": "A4", "combustible": "Bencina", "precio": 39000000},
    {"id": 18, "marca": "Audi", "modelo": "Q5", "combustible": "Diésel", "precio": 55000000},
    {"id": 19, "marca": "Mercedes-Benz", "modelo": "Clase C", "combustible": "Bencina", "precio": 45000000},
    {"id": 20, "marca": "Mercedes-Benz", "modelo": "GLC", "combustible": "Diésel", "precio": 58000000},
    {"id": 21, "marca": "Volkswagen", "modelo": "Golf", "combustible": "Bencina", "precio": 20000000},
    {"id": 22, "marca": "Volkswagen", "modelo": "Amarok", "combustible": "Diésel", "precio": 30000000},
    {"id": 23, "marca": "Peugeot", "modelo": "208", "combustible": "Bencina", "precio": 14000000},
    {"id": 24, "marca": "Renault", "modelo": "Duster", "combustible": "Diésel", "precio": 17000000},
    {"id": 25, "marca": "Tesla", "modelo": "Model 3", "combustible": "Eléctrico", "precio": 35000000}
]

@app.route('/')
def home():
    return "API de Autos funcionando!!!"

@app.route('/autos')
def obtener_autos():
    return jsonify(autos)

if __name__ == '__main__':
    app.run()