from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
# importando a view
from view import *

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Função para centralizar a janela
def centralizar_janela(janela):
    janela.update_idletasks()  # Atualiza as informações da janela
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)
    
    janela.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

# criando a janela 
janela = Tk()
janela.title('Trabalho de Extensão')
janela.configure(background=co9)
janela.resizable(width=False, height=False)
janela.geometry('1100x455')

centralizar_janela(janela)

# dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

# criando Label com titulo da tela
app_nome = Label(frame_cima, text='Cadastro de Alunos', anchor=NW, font=('Ivy 13 bold'), fg=co1, bg=co2, relief='flat')
app_nome.place(x=10, y=20)

global grid

# Função para limpar os campos
def limpar_campos():
    edt_nome.delete(0, 'end')
    edt_email.delete(0, 'end')
    edt_telefone.delete(0, 'end')
    edt_data.delete(0, 'end')
    edt_finalidade.delete(0, 'end')
    edt_obs.delete(0, 'end')

#Função Inserir
def Inserir_form():
    nome = edt_nome.get()
    email = edt_email.get()
    telefone = edt_telefone.get()
    data = edt_data.get()
    finalidade = edt_finalidade.get()
    observacao = edt_obs.get()

    lista = [nome, email, telefone, data, finalidade, observacao]

    if nome == '':
        messagebox.showinfo('Informação', 'Por favor, insira o nome do aluno(a)')
    else:
        inserir(lista) # função da view
        messagebox.showinfo('Atenção', 'Dados inseridos com sucesso!')
        limpar_campos()

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar_grid()

# função para atualizar informação
def atualizar():
    try:
        grid_dados = grid.focus()
        grid_dicionario = grid.item(grid_dados)
        grid_lista = grid_dicionario['values']
        
        valor_id = grid_lista[0]
        limpar_campos()

        edt_nome.insert(0, grid_lista[1])
        edt_email.insert(0, grid_lista[2])
        edt_telefone.insert(0, grid_lista[3])
        edt_data.insert(0, grid_lista[4])
        edt_finalidade.insert(0, grid_lista[5])
        edt_obs.insert(0, grid_lista[6])

        def editar():
            nome = edt_nome.get()
            email = edt_email.get()
            telefone = edt_telefone.get()
            data = edt_data.get()
            finalidade = edt_finalidade.get()
            observacao = edt_obs.get()

            lista = [nome, email, telefone, data, finalidade, observacao, valor_id]

            if nome == '':
                messagebox.showinfo('Informação', 'Por favor, insira o nome do aluno(a)')
            else:
                atualizar_informacao(lista) # função da view
                messagebox.showinfo('Atenção', 'Dados atualizados com sucesso!')
                limpar_campos()

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar_grid()

        btn_confirmar = Button(frame_baixo, text='Confirmar', command=editar, width=10, font=('Ivy 9 bold'), fg=co1, bg=co2, relief='raised', overrelief='ridge', cursor='hand2')
        btn_confirmar.place(x=112, y=370)

    except IndexError:
        messagebox.showerror('Atenção', 'Selecione um dos dados da tabela para atualizar!')

def deletar():
    try:
        grid_dados = grid.focus()
        grid_dicionario = grid.item(grid_dados)
        grid_lista = grid_dicionario['values']
        
        valor_id = [grid_lista[0]]

        apagar_informacao(valor_id)
        messagebox.showinfo('Atenção', 'Os dados foram apagados do Banco de Dados!')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar_grid()
    except:
        messagebox.showerror('Atenção', 'Selecione um dos dados da tabela para excluir!')

#configurando frame baixo - Campos edits e labels

# Nome do Aluno
lbl_nome = Label(frame_baixo, text='Nome do aluno(a): ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_nome.place(x=10, y=10)
edt_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_nome.place(x=15, y=40)

# Email
lbl_email = Label(frame_baixo, text='Email: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_email.place(x=10, y=70)
edt_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_email.place(x=15, y=100)

# Telefone
lbl_telefone = Label(frame_baixo, text='Telefone ou celular: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_telefone.place(x=10, y=130)
edt_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_telefone.place(x=15, y=160)

# Data da aula
lbl_data = Label(frame_baixo, text='Data da Aula: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_data.place(x=10, y=190)
edt_data = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024, locale='pt_BR', date_pattern='dd/MM/yyyy')
edt_data.place(x=15, y=220)

# Finalidade
lbl_finalidade = Label(frame_baixo, text='Finalidade: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_finalidade.place(x=160, y=190)
edt_finalidade = Entry(frame_baixo, width=21, justify='left', relief='solid')
edt_finalidade.place(x=160, y=220)

# Observação
lbl_obs = Label(frame_baixo, text='Observações: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_obs.place(x=15, y=260)
edt_obs = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_obs.place(x=15, y=290)


'''Botões do CRUD'''
# Inserir
btn_inserir = Button(frame_baixo, text='Inserir', command=Inserir_form, width=10, font=('Ivy 9 bold'), fg=co1, bg=co6, relief='raised', overrelief='ridge', cursor='hand2')
btn_inserir.place(x=15, y=340)

# Atualizar
btn_atualizar = Button(frame_baixo, text='Atualizar', command=atualizar, width=10, font=('Ivy 9 bold'), fg=co1, bg=co2, relief='raised', overrelief='ridge', cursor='hand2')
btn_atualizar.place(x=112, y=340)

# Deletar
btn_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), fg=co1, bg=co7, relief='raised', overrelief='ridge', cursor='hand2')
btn_deletar.place(x=210, y=340)

'''  Frame da Grid '''
# função para mostrar a grid
def mostrar_grid():
    global grid

    # Estilo
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Ivy', 9, 'bold'))
    style.configure("Treeview", background="#F0F0F0", foreground="black", rowheight=25, fieldbackground="#F0F0F0")

    lista = buscar()

    cabecalho_grid = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Finalidade', 'Observações']

    # criando a tabela
    grid = ttk.Treeview(frame_direita, selectmode='extended', columns=cabecalho_grid, show='headings')

    # scroll vertical
    scroll_vert = ttk.Scrollbar(frame_direita, orient='vertical', command=grid.yview)

    # scroll horizontal
    scroll_hori = ttk.Scrollbar(frame_direita, orient='horizontal', command=grid.xview)

    grid.configure(yscrollcommand=scroll_vert.set, xscrollcommand=scroll_hori.set) # aplicando o scroll na configuração
    grid.grid(column=0, row=0, sticky='nsew')
    scroll_vert.grid(column=1, row=0, sticky='ns')
    scroll_hori.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=['center','center','center','center','center','center','center'] #hd heder - sw = alinhados a esquerda
    h=[30,170,140,100,100,100,122] # representa o tamanho da tabelas
    n=0

    for coluna in cabecalho_grid:
        grid.heading(coluna, text=coluna.title(), anchor=CENTER)

        grid.column(coluna, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        grid.insert('', 'end', values=item) 


# chamar a função para mostrar a Grid

mostrar_grid()
janela.mainloop()