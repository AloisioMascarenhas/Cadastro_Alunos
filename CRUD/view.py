'''Operações do Crud'''
import sqlite3 as sql
import logging # registrar erros em um arquivo .txt

# configurando o log para registrar as mensagens de erro
logging.basicConfig(filename='log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# criando a conexão
conexao = sql.connect('dados.db')


# Inserindo as informações
def inserir(i):
    try:
        with conexao:
            cursor = conexao.cursor()
            query = 'INSERT INTO formulario (nome, email, telefone, data_aula, finalidade, observacao ) VALUES (?,?,?,?,?,?)'
            cursor.execute(query, i)
    except Exception as erro:
        logging.error(f'Erro ao inserir dados no Banco: {erro}')

# Acessar as informações
def buscar():
    lista = []
    try:
        with conexao:
            cursor = conexao.cursor()
            query = 'SELECT * FROM formulario'
            cursor.execute(query)
            informacao = cursor.fetchall()
            
            for i in informacao:
                lista.append(i)

    except Exception as erro:
        logging.error(f'Erro ao buscar dados: {erro}')

    return lista


# Alterar as informações
def atualizar_informacao(i):
    try:
        with conexao:
            cursor = conexao.cursor()
            query = 'UPDATE formulario SET nome=?, email=?, telefone=?, data_aula=?, finalidade=?, observacao=?  WHERE id=?'
            cursor.execute(query, i)
    except Exception as erro:
        logging.error(f'Erro ao editar dados no Banco: {erro}')


# Apagar informação
def apagar_informacao(i):
    try:
        with conexao:
            cursor = conexao.cursor()
            query = 'DELETE FROM formulario WHERE id=?'
            cursor.execute(query, i)
    except Exception as erro:
        logging.error(f'Erro ao tentar excluir dados no Banco: {erro}')