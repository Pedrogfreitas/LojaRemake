import sqlite3

con = sqlite3.connect('../data/loja.db')
cursor = con.cursor()

cursor.execute("SELECT id, nome, preco, estoque FROM produto")
produtos = cursor.fetchall()

print("Produtos cadastrados:")
print("--------------------")
for produto in produtos:
    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f} | Estoque: {produto[3]}")

con.close()
