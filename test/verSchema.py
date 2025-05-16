import sqlite3

def mostrar_schema():
    con = sqlite3.connect('../data/loja.db')  # ajuste o caminho se necessário
    cursor = con.cursor()

    print("📄 Esquema atual do banco de dados:\n")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tabelas = cursor.fetchall()

    for (nome_tabela,) in tabelas:
        print(f"-- Tabela: {nome_tabela}")
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name = ?", (nome_tabela,))
        schema = cursor.fetchone()
        print(schema[0] + ";\n")

    con.close()

if __name__ == "__main__":
    mostrar_schema()
