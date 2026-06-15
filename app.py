from flask import Flask, logging, render_template
from routes.animal_routes import animal_routes
from routes.adotante_routes import adotante_routes
from database.db import init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/adocao_animais_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db()

app.register_blueprint(animal_routes)
app.register_blueprint(adotante_routes)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)