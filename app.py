from flask import Flask, render_template
from routes.animal_routes import animal_routes
from database.db import init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/adocao_animais_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db()

# Register the animal routes
app.register_blueprint(animal_routes)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/animals/add_animal')
def register_animal():
    return render_template('animals/add_animal.html')

@app.route('/animals/list_animals')
def view_animals():
    return render_template('animals/list_animals.html')

if __name__ == '__main__':
    app.run(debug=True)