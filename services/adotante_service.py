from database.db import get_db_connection
from flask import request

class AdotanteService:
    @staticmethod
    def add_adotante(adotante):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO adotantes (nome_completo, tel, rua, num, bairro, cidade, estado_sigla, obs)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (adotante.nome_completo, adotante.tel, adotante.rua, adotante.num, adotante.bairro, adotante.cidade, adotante.estado_sigla, adotante.obs))

            conn.commit()
        finally:
            conn.close()
    
    @staticmethod
    def edit_adotante(id, adotante):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                UPDATE adotantes
                SET nome_completo = ?, tel = ?, rua = ?, num = ?, bairro = ?, cidade = ?, estado_sigla = ?, obs = ?
                WHERE id = ?
            ''', (adotante.nome_completo, adotante.tel, adotante.rua, adotante.num, adotante.bairro, adotante.cidade, adotante.estado_sigla, adotante.obs, id))
            
            conn.commit()
        finally:
           conn.close()
    
    @staticmethod
    def list_adotantes():
        conn = get_db_connection()
        cursor = conn.cursor()
        
        id_editado = request.args.get('id_editado')

        if id_editado:
            query = 'SELECT * FROM adotantes WHERE id = ?'
            cursor.execute(query, [id_editado])
            rows = cursor.fetchall()
            conn.close()
            return rows
        
        filtro_estado_sigla = request.args.get('estado_sigla')
        filtro_cidade = request.args.get('cidade')
        filtro_bairro = request.args.get('bairro')
        filtro_nome = request.args.get('name') 

        query = 'SELECT * FROM adotantes WHERE 1=1'
        params = []

        if filtro_estado_sigla:
            query += ' AND estado_sigla = ?'
            params.append(filtro_estado_sigla)

        if filtro_cidade:
            query += ' AND cidade = ?'
            params.append(filtro_cidade)

        if filtro_bairro:
            query += ' AND bairro = ?'
            params.append(filtro_bairro)

        if filtro_nome:
            query += ' AND nome_completo LIKE ?'
            params.append(f'%{filtro_nome}%')

        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        conn.close()
        return rows
    
    @staticmethod
    def remove_registry(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM adotantes WHERE id = ?', (id,))
            conn.commit()
        finally:
            conn.close()