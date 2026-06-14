class Animal:
    
    STATUS_AVAILABLE = 'disponivel'
    STATUS_ADOPTED = 'adotado'
    STATUS_PROCESSING = 'em processo'
    
    def __init__(self, name, species, breed, age, age_compl, sex, size, status, image, description='', id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.age_compl = age_compl
        self.sex = sex
        self.size = size
        self.status = status
        self.description = description
        self.image = image

    def __str__(self):
        return f'{self.name} is a {self.age}-year-old {self.sex} {self.breed} ({self.species}) currently located at {self.size}. Status: {self.status}. Description: {self.description}. Imagem: {self.image}'

    def is_available(self):
        return self.status == self.STATUS_AVAILABLE
    
    def mark_as_processing(self):
        if not self.is_available():
            raise Exception('Animal não disponível para adoção')
        else:
            self.status = self.STATUS_PROCESSING

    def mark_as_adopted(self):
        self.status = self.STATUS_ADOPTED