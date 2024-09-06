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
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            ddd TEXT NOT NULL,
            reference TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_contato(nome, telefone, ddd, reference):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, telefone, ddd, reference)
        VALUES (?, ?, ?, ?)
    ''', (nome, telefone, ddd, reference))
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
    ddd = entry_ddd.get()

    if not nome or not telefone:
        messagebox.showwarning("Aviso", "Nome e telefone são obrigatórios!")
        return
    
    adicionar_contato(nome, telefone, ddd, referencia)
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    update_list()

def update_list():
    for i in tree.get_children():
        tree.delete(i)
    contatos = buscar_contatos()
    for contato in contatos:
        tree.insert("", "end", values=contato)

def delete_contact():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um contato para excluir.")
        return

    item_id = tree.item(selected_item[0])['values'][0]

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM contatos WHERE id=?', (item_id,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Contato removido com sucesso!")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao remover o contato: {e}")
    finally:
        conn.close()
        update_list()

def validate_input(char):
    if char.isdigit() or char == "":
        return True
    else:
        return False

def editar_contato():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione um contato para editar.")
        return
    
    item_id = tree.item(selected_item[0])['values'][0]
    nome = tree.item(selected_item[0])['values'][1]
    telefone = tree.item(selected_item[0])['values'][2]
    ddd = tree.item(selected_item[0])['values'][3]
    referencia = tree.item(selected_item[0])['values'][4]
    
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, nome)
    entry_telefone.delete(0, tk.END)
    entry_telefone.insert(0, telefone)
    entry_ddd.delete(0, tk.END)
    entry_ddd.insert(0, ddd)
    entry_referencia.delete(0, tk.END)
    entry_referencia.insert(0, referencia)

    btn_adicionar.config(text="Salvar Alterações", command=lambda: salvar_alteracoes(item_id))

def salvar_alteracoes(contato_id):
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    ddd = entry_ddd.get()
    referencia = entry_referencia.get()

    if not nome or not telefone:
        messagebox.showwarning("Aviso", "Nome e telefone são obrigatórios!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE contatos
            SET nome=?, telefone=?, ddd=?, reference=?
            WHERE id=?
        ''', (nome, telefone, ddd, referencia, contato_id))
        conn.commit()
        messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao atualizar o contato: {e}")
    finally:
        conn.close()
        update_list()

        btn_adicionar.config(text="Adicionar Contato", command=adicionar_contato_gui)

root = tk.Tk()
root.title("Lista Telefônica")

setup_db()

validate_cmd = root.register(validate_input)

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

tk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_input)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="DDD:").grid(row=1, column=0, padx=5, pady=5)
entry_ddd = tk.Entry(frame_input, validate='key', validatecommand=(validate_cmd, "%S"))
entry_ddd.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Telefone:").grid(row=2, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_input, validate='key', validatecommand=(validate_cmd, "%S"))
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Referência:").grid(row=3, column=0, padx=5, pady=5)
entry_referencia = tk.Entry(frame_input)
entry_referencia.grid(row=3, column=1, padx=5, pady=5)

btn_adicionar = tk.Button(frame_input, text="Adicionar Contato", command=adicionar_contato_gui)
btn_adicionar.grid(row=4, columnspan=2, pady=10)

btn_editar = tk.Button(frame_input, text="Editar Contato", command=editar_contato)
btn_editar.grid(row=5, columnspan=2, pady=10)

btn_deletar = tk.Button(frame_input, text="Deletar Contato", command=delete_contact)
btn_deletar.grid(row=6, columnspan=2, pady=10)

frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=10)

colums = ('ID', 'Nome', 'Telefone', 'DDD', 'Referência')
tree = ttk.Treeview(frame_lista, columns=colums, show='headings')
tree.pack()

for col in colums:
    tree.heading(col, text=col)

update_list()
root.mainloop()
