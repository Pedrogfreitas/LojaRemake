import sqlite3
import os

# Caminho relativo ao diretório do script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'loja.db')

conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()