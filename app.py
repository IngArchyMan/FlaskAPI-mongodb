from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Permite que otros dominios puedan acceder a esta API

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["nombre_base_datos"]
collection = db["nombre_coleccion"]

@app.route('/', methods=['GET'])
def home_view():
    """Endpoint para consultar todos los datos en la colección."""
    #datos = list(collection.find({}, {"_id": 0}))  # Excluye el campo _id de los resultados
    return render_template('pages/index.html') #jsonify(datos)
@app.route('/consultar', methods=['GET'])
def consultar_datos():
    """Endpoint para consultar todos los datos en la colección."""
    #datos = list(collection.find({}, {"_id": 0}))  # Excluye el campo _id de los resultados
    return "Consultar" #jsonify(datos)

@app.route('/agregar', methods=['POST'])
def agregar_datos():
    """Endpoint para agregar datos a la colección."""
    #nuevo_dato = request.json
    #collection.insert_one(nuevo_dato)
    return "Agregar" #jsonify({"mensaje": "Dato agregado exitosamente"}), 201

@app.route('/eliminar', methods=['DELETE'])
def eliminar_datos():
    """Endpoint para eliminar un dato de la colección basado en un criterio."""
    #criterio = request.json  # Debe contener el criterio de búsqueda para eliminar
    #resultado = collection.delete_one(criterio)
    #if resultado.deleted_count:
    #    return jsonify({"mensaje": "Dato eliminado exitosamente"})
    #else:
    #    return jsonify({"mensaje": "Dato no encontrado"}), 404
    return "Eliminar"

if __name__ == '__main__':
    app.run(debug=True)
