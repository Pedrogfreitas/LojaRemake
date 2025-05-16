import sqlite3

con = sqlite3.connect('../data/loja.db')
cursor = con.cursor()

# Tenta adicionar as colunas (se já existirem, ignora o erro)
try:
    cursor.execute("ALTER TABLE produto ADD COLUMN descricao TEXT")
except sqlite3.OperationalError:
    pass  # coluna já existe

try:
    cursor.execute("ALTER TABLE produto ADD COLUMN imagem TEXT")
except sqlite3.OperationalError:
    pass  # coluna já existe

# Exemplo de update: atualizar um produto pelo ID
id_produto = 1  
nova_descricao = "Camisa social de algodão com acabamento fino. Ideal para ocasiões formais."
nova_imagem = "camisa_social.jpg"  # nome do arquivo ou URL, dependendo do seu sistema

cursor.execute("""
    UPDATE produto 
    SET descricao = ?, imagem = ?
    WHERE id = ?
""", (nova_descricao, nova_imagem, id_produto))

con.commit()
con.close()

print("Produto atualizado com sucesso!")
