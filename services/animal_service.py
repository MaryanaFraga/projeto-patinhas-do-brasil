from database.db import get_db_connection
from models.Animal import Animal

class AnimalService:
    @staticmethod
    def add_animal(animal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO animais (name, species, breed, age, sex, size, status, description, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (animal.name, animal.species, animal.breed, animal.age, animal.sex, animal.size, animal.status, animal.description, '/static/'+animal.image))

        conn.commit()
        conn.close()
    
    @staticmethod
    def edit_animal(animal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE animais
            SET name = ?, species = ?, breed = ?, age = ?, sex = ?, size = ?, status = ?, description = ?, image = ?
            WHERE id = ?
        ''', (animal.name, animal.species, animal.breed, animal.age, animal.sex, animal.size, animal.status, animal.description, animal.image, animal.id))

        conn.commit()
        conn.close()
    
    @staticmethod
    def list_animals():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM animais')
        rows = cursor.fetchall()
        
        conn.close()
        return rows
    
    @staticmethod
    def remove_registry(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM animais WHERE id = ?', (id,))

        conn.commit()
        conn.close()
    