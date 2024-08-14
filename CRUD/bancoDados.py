# Criando conexão com o Banco de Dados SQlite
import sqlite3 as sql

# Criando a conexão
con = sql.connect('dados.db')

# Criando a tabela
with con:
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE formulario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        data_aula DATE,
                        finalidade TEXT,
                        observacao TEXT
                   )''')