class Animal:
    
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
