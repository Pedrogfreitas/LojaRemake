from data import conectar, desconectar
import random
import string

def gerar_matricula(tamanho=6):
    # Gera uma matrícula aleatória de letras e números (exemplo: A1B2C3)
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))

def menu_gerente():
    while True:
        print("\n👔 Menu Gerente - Gestão de Funcionários")
        print("1 - Listar funcionários")
        print("2 - Adicionar funcionário")
        print("3 - Atualizar funcionário")
        print("4 - Remover funcionário")
        print("5 - Voltar")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            listar_funcionarios()
        elif opcao == "2":
            adicionar_funcionario()
        elif opcao == "3":
            atualizar_funcionario()
        elif opcao == "4":
            remover_funcionario()
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

def listar_funcionarios():
    con, cursor = conectar()
    cursor.execute("SELECT id, nome, matricula, cargo, isAdmin FROM funcionario ORDER BY id")
    funcionarios = cursor.fetchall()
    print("\nFuncionários cadastrados:")
    print("-" * 80)
    for f in funcionarios:
        admin_status = "Sim" if f[4] == 1 else "Não"
        print(f"ID: {f[0]} | Nome: {f[1]} | Matrícula: {f[2]} | Cargo: {f[3]} | Admin: {admin_status}")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    print("-" * 80)
    desconectar(con)

def adicionar_funcionario():
    con, cursor = conectar()
    nome = input("Digite o nome do funcionário: ").strip()
    cargo = input("Digite o cargo do funcionário: ").strip()
    
    while True:
        is_admin_input = input("Este funcionário é admin? (S/N): ").strip().lower()
        if is_admin_input in {"s", "n"}:
            isAdmin = 1 if is_admin_input == "s" else 0
            break
        print("Por favor, digite 'S' para Sim ou 'N' para Não.")

    matricula = gerar_matricula()
    # Verificar se matrícula já existe para evitar duplicidade
    cursor.execute("SELECT 1 FROM funcionario WHERE matricula = ?", (matricula,))
    while cursor.fetchone():
        matricula = gerar_matricula()
        cursor.execute("SELECT 1 FROM funcionario WHERE matricula = ?", (matricula,))

    cursor.execute(
        "INSERT INTO funcionario (nome, matricula, cargo, isAdmin) VALUES (?, ?, ?, ?)",
        (nome, matricula, cargo, isAdmin)
    )
    desconectar(con)
    print(f"✅ Funcionário adicionado com matrícula: {matricula}")

def atualizar_funcionario():
    con, cursor = conectar()
    matricula = input("Digite a matrícula do funcionário que deseja atualizar: ").strip()

    cursor.execute("SELECT id, nome, cargo, isAdmin FROM funcionario WHERE matricula = ?", (matricula,))
    func = cursor.fetchone()
    if not func:
        print("❌ Funcionário não encontrado.")
        desconectar(con)
        return

    print(f"Funcionário encontrado: ID {func[0]}, Nome: {func[1]}, Cargo: {func[2]}, Admin: {'Sim' if func[3] == 1 else 'Não'}")

    colunas_validas = {
        "nome": "nome",
        "cargo": "cargo",
        "admin": "isAdmin"
    }

    coluna_input = input("Digite o campo que deseja atualizar (nome, cargo, Admin): ").strip().lower()
    if coluna_input not in colunas_validas:
        print("❌ Campo inválido.")
        desconectar(con)
        return

    coluna = colunas_validas[coluna_input]

    if coluna == "isAdmin":
        while True:
            novo_valor = input("Atualizar admin para (S/N): ").strip().lower()
            if novo_valor in {"s", "n"}:
                novo_valor = 1 if novo_valor == "s" else 0
                break
            print("Por favor, digite 'S' para Sim ou 'N' para Não.")
    else:
        novo_valor = input(f"Digite o novo valor para {coluna_input}: ").strip()
        if not novo_valor:
            print("❎ Operação cancelada.")
            desconectar(con)
            return

    cursor.execute(f"UPDATE funcionario SET {coluna} = ? WHERE matricula = ?", (novo_valor, matricula))
    desconectar(con)
    print("✅ Funcionário atualizado com sucesso!")

def remover_funcionario():
    con, cursor = conectar()
    matricula = input("Digite a matrícula do funcionário que deseja remover: ").strip()

    cursor.execute("SELECT nome FROM funcionario WHERE matricula = ?", (matricula,))
    func = cursor.fetchone()
    if not func:
        print("❌ Funcionário não encontrado.")
        desconectar(con)
        return

    confirmacao = input(f"Tem certeza que deseja remover o funcionário '{func[0]}'? (S/N): ").strip().lower()
    if confirmacao != "s":
        print("❎ Operação cancelada.")
        desconectar(con)
        return

    cursor.execute("DELETE FROM funcionario WHERE matricula = ?", (matricula,))
    desconectar(con)
    print("🗑️ Funcionário removido com sucesso!")