import tkinter as tk
from tkinter import ttk
import sqlite3

def connect_db():
    conn = sqlite3.connect_db()
    cursor = cursor.execute