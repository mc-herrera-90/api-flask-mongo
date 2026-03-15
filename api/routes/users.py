from flask import Blueprint, request, jsonify
from api.db import users_collection
from bson import ObjectId

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def create_users():
    data = request.json

    user = {
        "name": data["name"],
        "email": data["email"]
    }
    result = users_collection.insert_one(user)

    return jsonify({
        "id": str(result.inserted_id),
        "mensaje": "Usuario creado con éxito"
    })
