from flask import Blueprint, redirect, render_template, request, url_for
from models.Animal import Animal
from services.animal_service import AnimalService

animal_routes = Blueprint('animal_routes', __name__)

@animal_routes.route('/animais/menu')
def show_menu():
    return render_template('animais/menu.html')

@animal_routes.route('/animais/cadastrar', methods=['POST', 'GET'])
def cadastrar():
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
        return redirect(url_for('animal_routes.listar_simples'))
    
    return render_template('animais/cadastrar.html')

@animal_routes.route('/animais/listar_simples', methods=['GET'])
def listar_simples():
    animals = AnimalService.list_animals()
    return render_template('animais/listar_simples.html', animals=animals)

@animal_routes.route('/animais/listar_em_grid', methods=['GET'])
def list_animals_grid():
    animals = AnimalService.list_animals()
    return render_template('animais/listar_em_grid.html', animals=animals)

@animal_routes.route('/animais/remover_registro/<int:id>', methods=['POST'])
def remover_registro(id):
    AnimalService.remove_registry(id)
    return redirect(url_for('animal_routes.listar_simples'))
