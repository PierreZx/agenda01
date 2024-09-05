import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def connect_db():
    conn = sqlite3.connect_db('brooklin.db')
    return conn

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone INTEGER
            reference TEXT 
        )
    ''')
    
def adicionar_contato(nome, telefone, reference):
        global cursor, conn
        cursor.execute(f'''
            INSERT INTO contatos (nome, telefone, reference)
            VALUES (?, ?, ?)
        ''', (nome, telefone, reference))
        conn.commit()
        conn.close()

def buscar_contatos(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos')
    return cursor.fetchall()

def adicionar_contato_gui():
     nome = entry_nome.get()
     telefone = entry_telefone.get()
     referencia = entry_referencia.get()

     if not nome or not telefone:
          messagebox.showwarning("Aviso", "Nome e telefone são obrigatórios!")
          return
     
adicionar_contato(conn, nome, telefone, endereco)
messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
atualizar_lista()

def atualizar_lista():
    for i in tree.get_children():
        tree.delete(i)
    contatos = buscar_contatos(conn)
    for contato in contatos:
        tree.insert("", "end", values=contato)

root = tk.Tk()
root.title("Lista Telefônica")

nome_banco = 'brooklin.db'
conn = connect_db(nome_banco)
setup_db(conn, 'contatos')

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

tk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_input)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Telefone:").grid(row=1, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_input)
entry_telefone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Endereço:").grid(row=2, column=0, padx=5, pady=5)
entry_endereco = tk.Entry(frame_input)
entry_endereco.grid(row=2, column=1, padx=5, pady=5)

btn_adicionar = tk.Button(frame_input, text="Adicionar Contato", command=adicionar_contato_gui)
btn_adicionar.grid(row=3, columnspan=2, pady=10)

frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=10)

cols = ('ID', 'Nome', 'Telefone', 'Endereço')
tree = ttk.Treeview(frame_lista, columns=cols, show='headings')
tree.pack()

for col in cols:
    tree.heading(col, text=col)

atualizar_lista()
root.mainloop()
conn.close()


class ContactList():
    def __init__(self, root):
        self.root = root
        self.root.title('Lista de contatos')
        setup_db()
        self.setup_iu()

    def setup_iu(self):
        self.button1 = ttk.Frame(self.root)
        self.button1.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.button1, text="Criar contato")
        self.add_button.pack(padx=5, pady=5)

        self.tree = ttk.Treeview(self.root, columns=("Nome", "Telefone", "Referência"))