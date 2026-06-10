from flask import Blueprint, redirect, render_template, request, url_for
from models.Animal import Animal
from services.animal_service import AnimalService

animal_routes = Blueprint('animal_routes', __name__)

@animal_routes.route('/animals/add_animal', methods=['GET','POST'])
def add_animal():
    if request.method == 'POST':
        new = Animal(
            name= request.form.get('name'),
            species=request.form.get('species'),
            breed=request.form.get('breed'),
            age=request.form.get('age'),
            sex=request.form.get('sex'),
            size=request.form.get('size'),
            status=request.form.get('status'),
            description=request.form.get('description'),
            image=request.form.get('image')
        )
        
        AnimalService.add_animal(new)
        return redirect(url_for('animal_routes.add_animal'))

    animals = AnimalService.list_animals()
    return render_template('animals/add_animal.html', animals=animals)

@animal_routes.route('/animals/list_animals', methods=['GET'])
def list_animals():
    animals = AnimalService.list_animals()
    return render_template('animals/list_animals.html', animals=animals)