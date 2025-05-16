import sqlite3

def listar_colunas(cursor):
    cursor.execute("PRAGMA table_info(produto)")
    colunas = cursor.fetchall()
    return [col[1] for col in colunas if col[1] != "id"]

def obter_valor_atual(cursor, id_produto, coluna):
    cursor.execute(f"SELECT {coluna} FROM produto WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

def atualizar_produto():
    con = sqlite3.connect('../data/loja.db')
    cursor = con.cursor()

    # Listar colunas disponíveis
    colunas = listar_colunas(cursor)
    print("Colunas disponíveis para edição:")
    for c in colunas:
        print(f"- {c}")

    try:
        id_input = input("\nDigite o ID do produto que deseja atualizar: ").strip()
        if not id_input:
            print("Operação cancelada.")
            return

        id_produto = int(id_input)

        coluna = input("Digite o nome da coluna que deseja atualizar: ").strip()
        if not coluna:
            print("Operação cancelada.")
            return

        if coluna not in colunas:
            print(f"Coluna '{coluna}' não existe na tabela 'produto'.")
            return

        # Obter valor atual
        valor_atual = obter_valor_atual(cursor, id_produto, coluna)
        if valor_atual is None:
            print("Produto não encontrado.")
            return

        print(f"Valor atual de '{coluna}': {valor_atual}")

        novo_valor = input(f"Digite o novo valor para '{coluna}' (pressione Enter para cancelar): ").strip()
        if novo_valor == "":
            print("Operação cancelada.")
            return

        # Atualiza o valor
        query = f"UPDATE produto SET {coluna} = ? WHERE id = ?"
        cursor.execute(query, (novo_valor, id_produto))
        con.commit()

        print("\n✅ Produto atualizado com sucesso!")

    except ValueError:
        print("Erro: ID inválido.")

    finally:
        con.close()

if __name__ == "__main__":
    atualizar_produto()
