from tkinter import *
from tkcalendar import Calendar, DateEntry

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

# criando a janela 
janela = Tk()
janela.title('Trabalho de Extensão')
janela.geometry('1043x455')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

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
edt_data = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_data.place(x=15, y=40)

# Finalidade
lbl_nome = Label(frame_baixo, text='Finalidade: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_nome.place(x=10, y=10)
edt_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_nome.place(x=15, y=40)

# Observação
lbl_nome = Label(frame_baixo, text='Observações: ', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
lbl_nome.place(x=10, y=10)
edt_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
edt_nome.place(x=15, y=40)






janela.mainloop()