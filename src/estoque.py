from data import conectar, desconectar

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

def listar_produtos():
    con, cursor = conectar()

    cursor.execute("SELECT id, nome, preco, estoque, descricao, imagem FROM produto ORDER BY id")
    produtos = cursor.fetchall()

    print("\nProdutos cadastrados:")
    print("-" * 50)
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f} | Estoque: {p[3]}")
        if p[4]:
            descricao = (p[4][:60] + '...') if len(p[4]) > 60 else p[4]
            print(f"Descrição: {descricao}")
        if p[5]:
            print(f"Imagem: {p[5]}")
        print("-" * 50)

    desconectar(con)

def adicionar_produto():
    con, cursor = conectar()

    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("❌ Nome do produto não pode ser vazio.")
        desconectar(con)
        return

    try:
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        estoque = int(input("Digite a quantidade em estoque: "))
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
    except ValueError as e:
        print(f"❌ {e}")
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
            if novo_valor < 0:
                raise ValueError("Preço não pode ser negativo.")
        elif coluna == "estoque":
            novo_valor = int(novo_valor)
            if novo_valor < 0:
                raise ValueError("Estoque não pode ser negativo.")
        elif coluna == "nome" and not novo_valor.strip():
            raise ValueError("Nome do produto não pode ser vazio.")
    except ValueError as e:
        print(f"❌ {e}")
        desconectar(con)
        return

    cursor.execute(f"UPDATE produto SET {coluna} = ? WHERE id = ?", (novo_valor, id_produto))
    desconectar(con)
    print("✅ Produto atualizado com sucesso!")

def remover_produto():
    con, cursor = conectar()

    try:
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
        cursor.execute("SELECT 1 FROM produto WHERE id = ?", (id_produto,))
        if not cursor.fetchone():
            print("❌ Produto não encontrado.")
            desconectar(con)
            return
    except ValueError:
        print("❌ ID inválido.")
        desconectar(con)
        return

    print(f"Tem certeza que deseja remover o produto com ID {id_produto}? (S/N)")
    confirmacao = input().strip().lower()
    if confirmacao != "s":
        print("❎ Operação cancelada.")
        desconectar(con)
        return

    cursor.execute("DELETE FROM produto WHERE id = ?", (id_produto,))
    desconectar(con)
    print("🗑️ Produto removido com sucesso!")
