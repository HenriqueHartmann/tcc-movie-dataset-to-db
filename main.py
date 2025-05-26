import csv
import sqlite3

def criar_banco_de_dados(csv_path='movie-dataset.csv', db_path='movies.db'):
    # Conectar ou criar o banco de dados SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Criar a tabela 'movies'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            overview TEXT
        )
    ''')

    # Ler os dados do CSV e inserir no banco
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            title = row.get('title', '').strip()
            overview = row.get('overview', '').strip()

            if title:  # Apenas insere se tiver título
                cursor.execute('''
                    INSERT INTO movies (title, overview)
                    VALUES (?, ?)
                ''', (title, overview))

    # Salvar e fechar a conexão
    conn.commit()
    conn.close()
    print(f"\n-- Banco de dados criado em '{db_path}' com tabela 'movies' --\n")

# Exemplo de uso
criar_banco_de_dados()
