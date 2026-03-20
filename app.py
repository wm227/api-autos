import os
from flask import Flask, jsonify, request

app = Flask(__name__)

autos = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "anio": 2022, "combustible": "Bencina", "precio": 15000000},
    {"id": 2, "marca": "Tesla", "modelo": "Model 3", "anio": 2023, "combustible": "Eléctrico", "precio": 35000000},
    {"id": 3, "marca": "Chevrolet", "modelo": "Spark", "anio": 2020, "combustible": "Bencina", "precio": 9000000}
]

next_id = 4

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensaje": "Bienvenido a la API de Autos Completa",
        "endpoints": {
            "GET /autos": "Obtener todos los autos",
            "GET /autos/<id>": "Obtener auto por ID",
            "POST /autos": "Crear un nuevo auto",
            "PUT /autos/<id>": "Actualizar un auto existente",
            "DELETE /autos/<id>": "Eliminar un auto"
        }
    })

@app.route('/autos', methods=['GET'])
def get_autos():
    return jsonify(autos)

@app.route('/autos/<int:id>', methods=['GET'])
def get_auto(id):
    auto = next((a for a in autos if a["id"] == id), None)
    if auto:
        return jsonify(auto)
    return jsonify({"error": f"El auto con ID {id} no fue encontrado"}), 404

@app.route('/autos', methods=['POST'])
def create_auto():
    global next_id
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
        
    campos_requeridos = ["marca", "modelo", "anio", "combustible", "precio"]
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({"error": f"Faltan campos. Requeridos: {campos_requeridos}"}), 400
        
    nuevo_auto = {
        "id": next_id,
        "marca": data["marca"],
        "modelo": data["modelo"],
        "anio": data["anio"],
        "combustible": data["combustible"],
        "precio": data["precio"]
    }
    
    autos.append(nuevo_auto)
    next_id += 1
    
    return jsonify(nuevo_auto), 201

@app.route('/autos/<int:id>', methods=['PUT'])
def update_auto(id):
    data = request.get_json()
    auto = next((a for a in autos if a["id"] == id), None)
    
    if auto:
        auto["marca"] = data.get("marca", auto["marca"])
        auto["modelo"] = data.get("modelo", auto["modelo"])
        auto["anio"] = data.get("anio", auto["anio"])
        auto["combustible"] = data.get("combustible", auto["combustible"])
        auto["precio"] = data.get("precio", auto["precio"])
        
        return jsonify({"mensaje": "Auto actualizado correctamente", "auto": auto})
        
    return jsonify({"error": "Auto no encontrado para actualizar"}), 404

@app.route('/autos/<int:id>', methods=['DELETE'])
def delete_auto(id):
    global autos
    auto = next((a for a in autos if a["id"] == id), None)
    
    if auto:
        autos = [a for a in autos if a["id"] != id]
        return jsonify({"mensaje": f"Auto con ID {id} eliminado exitosamente"})
        
    return jsonify({"error": "Auto no encontrado para eliminar"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)