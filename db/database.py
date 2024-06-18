import sqlite3

# Função para criar a tabela do jogador (se ainda não existir)
def create_player_table():
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()

    # SQL para criar a tabela do jogador com a restrição UNIQUE na coluna name
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        pos_x INTEGER,
        pos_y INTEGER,
        health FLOAT
    );
    '''

    # Executar o comando SQL
    cursor.execute(create_table_query)

    # Commit e fechar a conexão
    connection.commit()
    connection.close()

# Função para inserir os dados do jogador no banco de dados
def insert_player_data(name, pos_x, pos_y, health):
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()

    # SQL para inserir os dados do jogador
    insert_query = '''
    INSERT INTO player (name, pos_x, pos_y, health)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(name) DO UPDATE SET
    pos_x = excluded.pos_x,
    pos_y = excluded.pos_y,
    health = excluded.health;
    '''

    # Executar o comando SQL com os valores
    cursor.execute(insert_query, (name, pos_x, pos_y, health))

    # Commit e fechar a conexão
    connection.commit()
    connection.close()


# Função para buscar os dados do jogador no banco de dados
def get_player_data(name):
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()

    # SQL para buscar os dados do jogador
    select_query = '''
    SELECT pos_x, pos_y, health
    FROM player
    WHERE name = ?;
    '''

    # Executar o comando SQL com o nome do jogador
    cursor.execute(select_query, (name,))
    player_data = cursor.fetchone()  # Recuperar o primeiro resultado
    print(player_data)
    # Fechar a conexão
    connection.close()

    return player_data
