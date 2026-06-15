from database.db import get_db_connection
from flask import request
from models.Animal import Animal

class AnimalService:
    @staticmethod
    def add_animal(animal):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO animais (name, species, breed, age, age_compl, sex, size, status, description, image)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (animal.name, animal.species, animal.breed, animal.age, animal.age_compl, animal.sex, animal.size, animal.status, animal.description, '/static/img/fotos/'+animal.image))

            conn.commit()
        finally:
            conn.close()
    
    @staticmethod
    def edit_animal(id, animal):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                UPDATE animais
                SET name = ?, species = ?, breed = ?, age = ?, age_compl = ?, sex = ?, size = ?, status = ?, description = ?, image = ?
                WHERE id = ?
            ''', (animal.name, animal.species, animal.breed, animal.age, animal.age_compl, animal.sex, animal.size, animal.status, animal.description, animal.image, id))
            
            conn.commit()
        finally:
           conn.close()
    
    @staticmethod
    def list_animals():
        filtro_species = request.args.get('species')
        filtro_status = request.args.get('status')
        filtro_size = request.args.get('size')
        filtro_sex = request.args.get('sex')
        filtro_name = request.args.get('name')

        conn = get_db_connection()
        cursor = conn.cursor()

        query = 'SELECT * FROM animais WHERE 1=1'
        params = []

        if filtro_species:
            query += ' AND species = ?'
            params.append(filtro_species)

        if filtro_status:
            query += ' AND status = ?'
            params.append(filtro_status)

        if filtro_size:
            query += ' AND size = ?'
            params.append(filtro_size)

        if filtro_sex:
            query += ' AND sex = ?'
            params.append(filtro_sex)

        if filtro_name:
            query += ' AND name LIKE ?'
            params.append(f'%{filtro_name}%')

        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        conn.close()
        return rows
    
    @staticmethod
    def remove_registry(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM animais WHERE id = ?', (id,))

            conn.commit()
        finally:
            conn.close()
    