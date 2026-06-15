import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
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
            age NUMERIC NOT NULL,
            age_compl TEXT NOT NULL,
            sex TEXT NOT NULL,
            size TEXT NOT NULL,
            status TEXT NOT NULL,
            description TEXT,
            image TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adotantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_completo TEXT NOT NULL,
            tel TEXT NOT NULL,
            rua TEXT NOT NULL,
            num NUMERIC,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado_sigla TEXT NOT NULL,
            obs TEXT
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