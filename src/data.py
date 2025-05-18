import sqlite3
import os

# Caminho absoluto para o arquivo do banco de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'loja.db')

def conectar():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    return con, cursor

def desconectar(con):
    con.commit()
    con.close()
