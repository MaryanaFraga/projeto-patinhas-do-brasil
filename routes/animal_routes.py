from flask import Blueprint, request, jsonify
from models import Animal
from services.animal_service import AnimalService

animal_routes = Blueprint('animal_routes', __name__)

@animal_routes.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    
    new = AnimalService.add_animal(Animal(
        name=data['name'],
        species=data['species'],
        breed=data['breed'],
        age=data['age'],
        sex=data['sex'],
        size=data['size'],
        status=data['status'],
        description=data['description'],
        image=data['image']
    ))
    return jsonify({"Message": "Animal added successfully", "Animal": new.__dict__}), 201

@animal_routes.route('/animals', methods=['GET'])
def view_animals():
    animals = AnimalService.view_animals()
    return jsonify({"Message": "Animals retrieved successfully", "Animals": [animal.__dict__ for animal in animals]}), 200