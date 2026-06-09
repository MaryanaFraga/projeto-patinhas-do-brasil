import sqlite3

# connect to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # save as a dictionary
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL,
            sex TEXT NOT NULL,
            size TEXT NOT NULL,
            status TEXT NOT NULL,
            description TEXT NOT NULL,
            image TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adotantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cellphone TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            observations TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adocoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            data_adocao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            animal_id INTEGER NOT NULL,
            adotante_id INTEGER NOT NULL,         
            FOREIGN KEY(animal_id) REFERENCES animais(id),
            FOREIGN KEY(adotante_id) REFERENCES adotantes(id)
        )
    ''')

    conn.commit()
    conn.close()