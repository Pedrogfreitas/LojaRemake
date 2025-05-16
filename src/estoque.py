import sqlite3

DB_PATH = '../data/loja.db'

def menu_estoque():
    while True:
        print("\n📦 Bem-vindo ao menu de estoque.")
        print("1 - Listar produtos\n2 - Adicionar produto\n3 - Atualizar produto\n4 - Remover produto\n5 - Voltar")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

def conectar():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    return con, cursor

def desconectar(con):
    con.commit()
    con.close()

def listar_produtos():
    con, cursor = conectar()

    cursor.execute("SELECT id, nome, preco, estoque, descricao, imagem FROM produto")
    produtos = cursor.fetchall()

    print("\nProdutos cadastrados:")
    print("-" * 50)
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f} | Estoque: {p[3]}")
        if p[4]:
            print(f"Descrição: {p[4]}")
        if p[5]:
            print(f"Imagem: {p[5]}")
        print("-" * 50)

    desconectar(con)

def adicionar_produto():
    con, cursor = conectar()

    nome = input("Digite o nome do produto: ")

    try:
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
    except ValueError:
        print("❌ Valor numérico inválido.")
        desconectar(con)
        return

    descricao = input("Digite a descrição do produto (opcional): ")
    imagem = input("Digite o link ou caminho da imagem (opcional): ")

    cursor.execute("""
        INSERT INTO produto (nome, preco, estoque, descricao, imagem)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, preco, estoque, descricao or None, imagem or None))

    desconectar(con)
    print("✅ Produto adicionado com sucesso!")

def atualizar_produto():
    con, cursor = conectar()

    try:
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
    except ValueError:
        print("❌ ID inválido.")
        desconectar(con)
        return

    coluna = input("Digite o nome da coluna que deseja atualizar (nome, preco, estoque, descricao, imagem): ").strip().lower()

    colunas_validas = {"nome", "preco", "estoque", "descricao", "imagem"}
    if coluna not in colunas_validas:
        print("❌ Coluna inválida.")
        desconectar(con)
        return

    cursor.execute(f"SELECT {coluna} FROM produto WHERE id = ?", (id_produto,))
    atual = cursor.fetchone()
    if not atual:
        print("❌ Produto não encontrado.")
        desconectar(con)
        return

    print(f"Valor atual de '{coluna}': {atual[0]}")
    novo_valor = input(f"Digite o novo valor (ou pressione ENTER para cancelar): ")
    if novo_valor == "":
        print("❎ Operação cancelada.")
        desconectar(con)
        return

    try:
        if coluna == "preco":
            novo_valor = float(novo_valor)
        elif coluna == "estoque":
            novo_valor = int(novo_valor)
    except ValueError:
        print("❌ Valor inválido para o tipo da coluna.")
        desconectar(con)
        return

    cursor.execute(f"UPDATE produto SET {coluna} = ? WHERE id = ?", (novo_valor, id_produto))
    desconectar(con)
    print("✅ Produto atualizado com sucesso!")

def remover_produto():
    con, cursor = conectar()

    try:
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("❌ ID inválido.")
        desconectar(con)
        return

    cursor.execute("DELETE FROM produto WHERE id = ?", (id_produto,))
    desconectar(con)
    print("🗑️ Produto removido com sucesso!")
