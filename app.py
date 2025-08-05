from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conexión a MongoDB Atlas
uri = "mongodb+srv://gomeznicolas645:KRBHKGKzqeDQg2Al@cluster0.36stx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["data_bpm"]
coleccion = db["ritmo-cardiaco"]

@app.route("/", methods=["POST"])
def recibir_datos():
    try:
        data = request.get_json()
        print("Datos recibidos:", data)

        data["timestamp"] = datetime.now()
        coleccion.insert_one(data)
        print("Guardado en MongoDB:", data)

        return jsonify({"mensaje": "Guardado correctamente"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def status():
    return jsonify({"mensaje": "Servidor online"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
