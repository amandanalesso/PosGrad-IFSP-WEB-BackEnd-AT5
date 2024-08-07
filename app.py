from flask import Flask, request, jsonify
from collections import OrderedDict


app = Flask(__name__)


# Array com dados dos dragões
dragons =  [
    {"id": 1, "name": "Balerion", "rider": "Aegon the Conqueror", "origin": "Valyria", "rider_count": 1, "color": "test"},
    {"id": 2, "name": "Vhagar", "rider": "Visenya Targaryen", "origin": "Valyria", "rider_count": 3, "color": "test"},
    {"id": 3, "name": "Meraxes", "rider": "Rhaenys Targaryen", "origin": "Valyria", "rider_count": 1, "color": "test"},
    {"id": 4, "name": "Drogon", "rider": "Daenerys Targaryen", "origin": "Essos", "rider_count": 1, "color": "test"},
    {"id": 5, "name": "Rhaegal", "rider": "Daenerys Targaryen", "origin": "Essos", "rider_count": 0, "color": "test"},
    {"id": 6, "name": "Viserion", "rider": "Daenerys Targaryen", "origin": "Essos", "rider_count": 0, "color": "test"},
    {"id": 7, "name": "Syrax", "rider": "Rhaenyra Targaryen", "origin": "Dragonstone", "rider_count": 1, "color": "test"},
    {"id": 8, "name": "Caraxes", "rider": "Daemon Targaryen", "origin": "Dragonstone", "rider_count": 1,"color": "test"},
    {"id": 9, "name": "Meleys", "rider": "Rhaenys Targaryen", "origin": "Dragonstone", "rider_count": 1,"color": "test"}
]

# Rota padrão
@app.route('/')
def index():
    return "Dragões API"

# Rota para obter dados de todos os dragões
@app.route('/dragons', methods=['GET'])
def get_dragons():
    return jsonify(dragons)

# Rota para obter dados de um dragão pelo id
@app.route('/dragons/<int:dragon_id>', methods=['GET'])
def get_dragon(dragon_id):
    dragon = next((d for d in dragons if d['id'] == dragon_id), None)
    if dragon is None:
        return jsonify({"error": "Dragon not found"}), 404
    return jsonify(dragon)

# Rota para adicionar um dragão
@app.route('/dragons', methods=['POST'])
def add_dragon(): 
    data = request.json 
    new_id = max(d['id'] for d in dragons) + 1 
    new_dragon = { 
        "id": new_id, 
        "name": data.get("name"), 
        "rider": data.get("rider"), 
        "origin": data.get("origin"), 
        "color": data.get("color"), 
        "rider_count": data.get("rider_count") 
    } 
    dragons.append(new_dragon) 
    print(f"Added dragon: {new_dragon}")
    return jsonify(new_dragon), 201

# Rota para atualizar dados de um dragão específico
@app.route('/dragons/<int:dragon_id>', methods=['PUT'])
def update_dragon(dragon_id): 
    dragon = next((d for d in dragons if d['id'] == dragon_id), None) 
    if dragon is None: 
        return jsonify({"error": "Dragon not found"}), 404 
    data = request.json 
    dragon.update({ 
            "name": data.get("name", dragon["name"]), 
            "rider": data.get("rider", dragon["rider"]), 
            "origin": data.get("origin", dragon["origin"]), 
            "color": data.get("color", dragon["color"]), 
            "rider_count": data.get("rider_count", dragon["rider_count"]) 
    }) 
    return jsonify(dragon)


#Rota para deletar um dragão específico
@app.route('/dragons/<int:dragon_id>', methods=['DELETE'])
def delete_dragon(dragon_id): 
    global dragons 
    dragons[:] = [d for d in dragons if d['id'] != dragon_id] 
    return jsonify({"message": "Dragon deleted"}), 200 
    

if __name__ == '__main__':
    app.run(debug=True)










