# Cadastro de Alunos
![Logo](https://img.icons8.com/ios-filled/50/000000/school.png)
 Formulário de Cadastro de Alunos em Python e SQlite - Trabalho de Extesão - Estacio de Sá
 Este é um projeto de uma aplicação de cadastro de alunos usando `Tkinter` para a interface gráfica e `SQLite` para o gerenciamento de banco de dados. O aplicativo permite inserir, atualizar e excluir registros de alunos, e exibir esses registros em uma tabela.

## Bibliotecas usadas
 Tkinter
 tkcalendar - pip install tkcalendar
 from tkinter import ttk para usar o Treeview (Grid)

## Funcionalidades

- 📋**Cadastro de Alunos**: Adicione novos registros de alunos com informações como nome, email, telefone, data da aula, finalidade e observações.
- ✏️**Atualização de Dados**: Atualize as informações de um aluno selecionado na tabela.
- 🗑️**Exclusão de Dados**: Exclua registros de alunos da tabela.
- 📊**Exibição de Dados**: Exiba os registros de alunos em uma tabela com rolagem vertical e horizontal.

## Requisitos

- 🐍 **Python 3.x**
- 📦 **Bibliotecas**:
  - `tkinter` (para a interface gráfica)
  - `tkcalendar` (para selecionar datas)
  - `sqlite3` (para o banco de dados)
  - `logging` (para registrar erros)

## Estrutura do Projeto

### Arquivo Principal (`main.py`)

Este arquivo contém a interface gráfica e as funcionalidades principais do aplicativo, incluindo:

- **Centralização da Janela**: Função para centralizar a janela principal na tela.
- **Frames**: Estrutura da janela dividida em frames para melhor organização dos componentes.
- **Widgets**: Labels, entradas de texto e botões para interagir com o usuário.
- **Funções CRUD**:
  - ✏️ `Inserir_form()`: Insere novos dados no banco de dados e atualiza a tabela.
  - 🔄 `atualizar()`: Atualiza dados de um aluno selecionado.
  - 🗑️ `deletar()`: Exclui um aluno selecionado do banco de dados.
  - 📋 `mostrar_grid()`: Exibe os dados em uma tabela.

### Arquivo de Operações CRUD (`view.py`)

Este arquivo contém funções para manipulação dos dados no banco de dados SQLite:

- **Inserir**: Adiciona novos registros ao banco de dados.
- **Buscar**: Recupera todos os registros do banco de dados.
- **Atualizar**: Atualiza registros existentes no banco de dados.
- **Apagar**: Exclui registros do banco de dados.

## Uso

1. **Executar o Projeto**: 
   - Execute o arquivo `main.py` para iniciar a aplicação.

2. **Inserir Dados**:
   - Preencha os campos de nome, email, telefone, data da aula, finalidade e observações e clique em "Inserir".

3. **Atualizar Dados**:
   - Selecione um registro na tabela, edite os campos necessários e clique em "Atualizar".

4. **Excluir Dados**:
   - Selecione um registro na tabela e clique em "Deletar".

