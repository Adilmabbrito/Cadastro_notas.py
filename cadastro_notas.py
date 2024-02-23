import tkinter as tk
from tkinter import ttk

# Lista para armazenar as médias calculadas
medias = []

def calcular_media():
    # Obter os valores dos campos de entrada
    nome = entry_nome.get()
    materia = entry_materia.get()
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    nota3 = float(entry_nota3.get())

    # Calcular a média
    media = (nota1 + nota2 + nota3) / 3

    # Adicionar a média à lista
    medias.append((nome, materia, media))

    # Atualizar a tabela de médias
    update_table()

def update_table():
    # Limpar a tabela
    for i in treeview.get_children():
        treeview.delete(i)

    # Preencher a tabela com as médias calculadas
    for media in medias:
        treeview.insert('', 'end', values=media)

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Notas")

# Criar os widgets
label_nome = tk.Label(root, text="Nome do Aluno:")
entry_nome = tk.Entry(root)

label_materia = tk.Label(root, text="Matéria:")
entry_materia = tk.Entry(root)

label_nota1 = tk.Label(root, text="Nota 1:")
entry_nota1 = tk.Entry(root)

label_nota2 = tk.Label(root, text="Nota 2:")
entry_nota2 = tk.Entry(root)

label_nota3 = tk.Label(root, text="Nota 3:")
entry_nota3 = tk.Entry(root)

button_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)

# Criar a tabela de médias
columns = ('Nome', 'Matéria', 'Média')
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)

# Posicionar os widgets na janela
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_materia.grid(row=1, column=0, padx=10, pady=5)
entry_materia.grid(row=1, column=1, padx=10, pady=5)

label_nota1.grid(row=2, column=0, padx=10, pady=5)
entry_nota1.grid(row=2, column=1, padx=10, pady=5)

label_nota2.grid(row=3, column=0, padx=10, pady=5)
entry_nota2.grid(row=3, column=1, padx=10, pady=5)

label_nota3.grid(row=4, column=0, padx=10, pady=5)
entry_nota3.grid(row=4, column=1, padx=10, pady=5)

button_calcular.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

treeview.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Iniciar o loop de eventos
root.mainloop()
