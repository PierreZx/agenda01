import tkinter as tk
import json
import ttkbootstrap as ttk
from tkcalendar import DateEntry
from tkinter import messagebox


app = ttk.Window(themename="flatly")
app.title("Supermercado")
app.geometry('600x800')

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill="both")

aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)

notebook.add(aba1, text="Contatos")
notebook.add(aba2, text="Adicionar contatos")

def on_entry_click(event):
    if entry1.get() == 'Pesquisar contato':
        entry1.delete(0, "end")
        entry1.config(fg='black')

def on_focusout(event):
    if entry1.get() == '':
        entry1.insert(0, 'Pesquisar contato')
        entry1.config(fg='grey')

entry1 = tk.Entry(aba1, fg='grey')
entry1.insert(0, 'Pesquisar contato')
entry1.bind('<FocusIn>', on_entry_click)
entry1.bind('<FocusOut>', on_focusout)
entry1.place(x= 30, y= 42)










titulo = ttk.Label(aba2, text="Adicionar Contato:", font=("Arial", 12), bootstyle="primary")
titulo.place(x= 10, y= 20)

titulo = ttk.Label(aba1, text="Contatos:", font=("Arial", 12), bootstyle="primary")
titulo.place(x= 10, y= 10)

def on_entry_click1(event):
    if entry2.get() == 'Nome do contato':
        entry2.delete(0, "end")
        entry2.config(fg='black')

def on_focusout1(event):
    if entry2.get() == '':
        entry2.insert(0, 'Nome do contato')
        entry2.config(fg='grey')

entry2 = tk.Entry(aba2, fg='grey')
entry2.insert(0, 'Nome do contato')
entry2.bind('<FocusIn>', on_entry_click1)
entry2.bind('<FocusOut>', on_focusout1)
entry2.place(x= 30, y= 42)









def on_entry_click2(event):
    if entry3.get() == 'Sobrenome/referência':
        entry3.delete(0, "end")
        entry3.config(fg='black')

def on_focusout2(event):
    if entry3.get() == '':
        entry3.insert(0, 'Sobrenome/referência')
        entry3.config(fg='grey')

entry3 = tk.Entry(aba2, fg='grey')
entry3.insert(0, 'Sobrenome/referência')
entry3.bind('<FocusIn>', on_entry_click2)
entry3.bind('<FocusOut>', on_focusout2)
entry3.place(x= 30, y= 70)











def on_entry_click3(event):
    if entry4.get() == 'DDD':
        entry4.delete(0, "end")
        entry4.config(fg='black')

def on_focusout3(event):
    if entry4.get() == '':
        entry4.insert(0, 'DDD')
        entry4.config(fg='grey')

entry4 = tk.Entry(aba2, fg='grey')
entry4.insert(0, 'DDD')
entry4.bind('<FocusIn>', on_entry_click3)
entry4.bind('<FocusOut>', on_focusout3)
entry4.place(x= 30, y= 90)









def on_entry_click4(event):
    if entry5.get() == 'Número':
        entry5.delete(0, "end")
        entry5.config(fg='black')

def on_focusout4(event):
    if entry5.get() == '':
        entry5.insert(0, 'Número')
        entry5.config(fg='grey')

entry5 = tk.Entry(aba2, fg='grey')
entry5.insert(0, 'Número')
entry5.bind('<FocusIn>', on_entry_click4)
entry5.bind('<FocusOut>', on_focusout4)
entry5.place(x= 30, y= 110)

app.mainloop()