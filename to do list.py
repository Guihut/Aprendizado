import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        lista_tarefas.delete(selecao)
    except:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

# Configuração da interface gráfica
app = tk.Tk()
app.title("To-Do List")

# Entrada para adicionar tarefas
entry_tarefa = tk.Entry(app, width=40)
entry_tarefa.pack(pady=10)

# Botão para adicionar tarefas
btn_adicionar = tk.Button(app, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

# Lista para exibir tarefas
lista_tarefas = tk.Listbox(app, selectmode=tk.SINGLE, width=40, height=10)
lista_tarefas.pack(pady=10)

# Botão para remover tarefas
btn_remover = tk.Button(app, text="Remover Tarefa Selecionada", command=remover_tarefa)
btn_remover.pack(pady=5)

# Iniciar a interface gráfica
app.mainloop()
