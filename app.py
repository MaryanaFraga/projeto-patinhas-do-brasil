from flask import Flask
from database import db
from routes.animal_routes import animal_routes
from database.db import init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/adocao_animais_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db()

# Register the animal routes
app.register_blueprint(animal_routes)

if __name__ == '__main__':
    app.run(debug=True)