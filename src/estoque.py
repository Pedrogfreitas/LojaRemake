import sqlite3

con = sqlite3.connect('../data/loja.db')
cursor = con.cursor()

def menu_estoque():
    print("\n📦 Bem-vindo ao menu de estoque.")
    input("Escolha qual função você deseja!\n \n1 - Listar produtos\n2 - Adicionar produto\n3 - Atualizar produto\n4 - Remover produto\n5 - Sair\n\nDigite a opção desejada: ")

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
        print("👋 Encerrando o sistema. Até logo!")
    else:
        print("❌ Opção inválida. Tente novamente.")

def listar_produtos():
    cursor.execute("SELECT id, nome, preco, estoque FROM produto")
    produtos = cursor.fetchall()

    print("Produtos cadastrados:")
    print("--------------------")
    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f} | Estoque: {produto[3]}")

    con.close()

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    cursor.execute("INSERT INTO produto (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
    con.commit()

    print("Produto adicionado com sucesso!")

    con.close()

def atualizar_produto():
    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
    coluna = input("Digite o nome da coluna que deseja atualizar: ")
    novo_valor = input(f"Digite o novo valor para {coluna}: ")

    cursor.execute(f"UPDATE produto SET {coluna} = ? WHERE id = ?", (novo_valor, id_produto))
    con.commit()

    print("Produto atualizado com sucesso!")

    con.close()

def remover_produto():
    id_produto = int(input("Digite o ID do produto que deseja remover: "))

    cursor.execute("DELETE FROM produto WHERE id = ?", (id_produto,))
    con.commit()

    print("Produto removido com sucesso!")

    con.close()