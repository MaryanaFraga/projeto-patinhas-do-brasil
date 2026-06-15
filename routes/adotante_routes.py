from flask import Blueprint, redirect, render_template, request, url_for
from models.Adotante import Adotante
from services.adotante_service import AdotanteService

adotante_routes = Blueprint('adotante_routes', __name__)

@adotante_routes.route('/adotante_cadastro', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        new = Adotante(
            nome_completo=request.form.get('nome_completo'),
            tel=request.form.get('tel'),
            rua=request.form.get('rua'),
            num=request.form.get('num'),
            bairro=request.form.get('bairro'),
            cidade=request.form.get('cidade'),
            estado_sigla=request.form.get('estado_sigla'),
            obs=request.form.get('obs')
        )
    
        AdotanteService.add_adotante(new)
        return redirect(url_for('adotante_routes.listar'))
    
    return render_template('adotante_cadastro.html')

@adotante_routes.route('/adotante_lista', methods=['GET'])
def listar():
    adotantes = AdotanteService.list_adotantes()
    return render_template('adotante_lista.html', adotantes=adotantes)

@adotante_routes.route('/remover/<int:id>', methods=['POST'])
def remover(id):
    AdotanteService.remove_registry(id)
    return redirect(request.referrer or url_for('index'))

@adotante_routes.route('/editar/<int:id>', methods=['POST', 'GET'])
def editar(id):
    if request.method == 'GET':
        conn = AdotanteService.list_adotantes()
        adotante = next((a for a in conn if a['id'] == id), None)
        if adotante is None:
            return "Adotante não encontrado", 404
        return render_template('editar.html', adotante=adotante)
    
    if request.method == 'POST':
        updated_adotante = Adotante(
            nome_completo=request.form.get('nome_completo'),
            tel=request.form.get('tel'),
            rua=request.form.get('rua'),
            num=request.form.get('num'),
            bairro=request.form.get('bairro'),
            cidade=request.form.get('cidade'),
            estado_sigla=request.form.get('estado_sigla'),
            obs=request.form.get('obs')
        )
    
        AdotanteService.edit_adotante(id, updated_adotante)
        return redirect(url_for('adotante_routes.listar', id_editado=id))