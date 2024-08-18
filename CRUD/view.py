'''Operações do Crud'''
import sqlite3 as sql

# criando a conexão
conexao = sql.connect('dados.db')
lista = ['Teste Testando 3', 'teste@email.com', 123456789, "15/08/2024", 'musculacao', 'Academia do bairro']

# Inserindo as informações
def inserir(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'INSERT INTO formulario (nome, email, telefone, data_aula, finalidade, observacao ) VALUES (?,?,?,?,?,?)'
        cursor.execute(query, i)
inserir(lista)

# Acessar as informações
def buscar():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        query = 'SELECT * FROM formulario'
        cursor.execute(query)
        informacao = cursor.fetchall()
        
        for i in informacao:
            lista.append(i)

    return lista

# Alterar as informações
def atualizar_informacao(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'UPDATE formulario SET nome=?, email=?, telefone=?, data_aula=?, finalidade=?, observacao=?  WHERE id=?'
        cursor.execute(query, i)

# Apagar informação
def apagar_informacao(i):
    with conexao:
        cursor = conexao.cursor()
        query = 'DELETE FROM formulario WHERE id=?'
        cursor.execute(query, i)