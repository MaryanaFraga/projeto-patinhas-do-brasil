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
        ''', (animal.name, animal.species, animal.breed, animal.age, animal.sex, animal.size, 'disponivel', animal.description, animal.image))

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
    def remove_animal(animal_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM animais WHERE id = ?', (animal_id,))

        conn.commit()
        conn.close()
    
    @staticmethod
    def view_animals():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM animais')
        rows = cursor.fetchall()

        animals = []
        for row in rows:
            animal = Animal(
                id=row['id'],
                name=row['name'],
                species=row['species'],
                breed=row['breed'],
                age=row['age'],
                sex=row['sex'],
                size=row['size'],
                status=row['status'],
                description=row['description'],
                image=row['image']
            )
            animals.append(animal)

        conn.close()
        return animals