import sqlite3

con = sqlite3.connect('../data/loja.db')
cursor = con.cursor()

# Lista de produtos: (nome, preco, estoque)
produtos = [
    ("Camisa Social", 59.90, 10),
    ("Camisa Polo", 39.90, 10),
    ("Regata", 39.90, 10),
    ("Camisa Estampada", 179.90, 10),
    ("Camisa Agostinho Carrara", 79.90, 10),
    ("Bermuda Jeans", 199.90, 10),
    ("Bermuda Treino", 69.90, 10),
    ("Shorts de Praia", 106.90, 10),
    ("Calça Jeans", 189.90, 10),
    ("Calça de Moletom", 129.90, 10),
    ("Calça Social", 129.90, 10),
    ("Cueca Box", 19.90, 10),
    ("Cueca Copinho", 14.90, 10),
    ("Cueca CK", 29.90, 10),
    ("Sapato Social", 269.90, 10),
    ("Tênis", 219.90, 10),
    ("Sapato Cano Longo", 149.90, 10),
    ("Bota", 119.90, 10),
    ("Havaianas", 19.90, 10),
    ("Kenner", 129.90, 10),
    ("Vestido", 140.90, 10),
    ("Camisa Feminina", 228.90, 10),
    ("Camisa Jeans Feminina", 294.90, 10),
    ("Top", 89.90, 10),
    ("Calça Feminina", 79.90, 10),
    ("Saia", 22.90, 10),
    ("Minissaia", 26.70, 10),
    ("Biquíni Parte de Cima", 49.90, 10),
    ("Biquíni Parte de Baixo", 39.90, 10),
    ("Biquíni Conjunto", 84.90, 10),
    ("Calcinha", 19.90, 10),
    ("Calcinha Fio Dental", 39.90, 10),
    ("Salto", 89.90, 10),
    ("Rasteirinha", 39.90, 10),
    ("Bota Feminina", 99.90, 10),
    ("Sapato Feminino", 199.90, 10)
]

# Inserindo produtos
cursor.executemany("INSERT INTO produto (nome, preco, estoque) VALUES (?, ?, ?)", produtos)

# Salvando e fechando conexão
con.commit()
con.close()

print("Produtos inseridos com sucesso!")