import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def connect_db():
    conn = sqlite3.connect('brooklin.db')
    return conn

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            telefone TEXT NOT NULL,
            reference TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_contato(nome, telefone, reference):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, telefone, reference)
        VALUES (?, ?, ?)
    ''', (nome, telefone, reference))
    conn.commit()
    conn.close()

def buscar_contatos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    conn.close()
    return contatos

def adicionar_contato_gui():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    referencia = entry_referencia.get()

    if not nome or not telefone:
        messagebox.showwarning("Aviso", "Nome e telefone são obrigatórios!")
        return
    
    adicionar_contato(nome, telefone, referencia)
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    update_list()

def update_list():
    for i in tree.get_children():
        tree.delete(i)
    contatos = buscar_contatos()
    for contato in contatos:
        tree.insert("", "end", values=contato)

def delete_contact():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contatos WHERE id=?', (id,))
    try:
        conn.commit()
        if cursor.rowcount > 0:
            return True, "Contato removido com sucesso!"
        else:
            return False, "Contato não encontrado."
    except sqlite3.Error as e:
        return False, f"Erro ao remover produto: {e}"
    finally:
        conn.close()

root = tk.Tk()
root.title("Lista Telefônica")

setup_db()

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

tk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_input)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Telefone:").grid(row=1, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_input)
entry_telefone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Referência:").grid(row=2, column=0, padx=5, pady=5)
entry_referencia = tk.Entry(frame_input)
entry_referencia.grid(row=2, column=1, padx=5, pady=5)

btn_adicionar = tk.Button(frame_input, text="Adicionar Contato", command=adicionar_contato_gui)
btn_adicionar.grid(row=3, columnspan=2, pady=10)

btn_deletar = tk.Button(frame_input, text="Deletar contato", command=delete_contact)
btn_deletar.grid(row=4, columnspan=3, pady=10)

frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=10)

colums = ('ID', 'Nome', 'Telefone', 'Referência')
tree = ttk.Treeview(frame_lista, columns=colums, show='headings')
tree.pack()

for col in colums:
    tree.heading(col, text=col)

update_list()
root.mainloop()
