import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tarefas = []
def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        tarefas.append({"tarefa": tarefa, "data": datetime.now()})
        listbox_tarefas.insert(tk.END, f"{tarefa} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite tarefa")

def concluir_tarefa():
    indice_selecionado = listbox_tarefas.curselection()
    if indice_selecionado:
        tarefa_concluida = tarefas.pop(indice_selecionado[0])
        listbox_tarefas.delete(indice_selecionado)
        messagebox.showinfo("Concluido", f"{tarefa_concluida['tarefa']} foi concluida")

root = tk.Tk()
root.title("Gerenciador de tarefas")
label = tk.Label(root, text="Tarefa", width=40)
label.pack(pady=5)

entry_tarefa = tk.Entry(root, width=40)
entry_tarefa.pack()
botao_adicionar = tk.Button(root, text="Adicionar tarefa", command=adicionar_tarefa)
botao_adicionar.pack()
listbox_tarefas = tk.Listbox(root, width=40, height=10)
listbox_tarefas.pack()
botao_concluir = tk.Button(root, text="Concluir Tarefa", command=concluir_tarefa)
botao_concluir.pack(pady=5)
root.mainloop()