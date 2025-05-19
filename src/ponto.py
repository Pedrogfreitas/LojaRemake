from data import conectar, desconectar
import datetime

def registrar_ponto(matricula):
    con, cursor = conectar()

    # Busca funcionário pelo campo matricula
    cursor.execute("SELECT id FROM funcionario WHERE matricula = ?", (matricula,))
    resultado = cursor.fetchone()
    if not resultado:
        print("❌ Matrícula não encontrada.")
        desconectar(con)
        return

    funcionario_id = resultado[0]

    # Busca ponto aberto (entrada sem saida) para esse funcionário
    cursor.execute("""
        SELECT id, entrada FROM ponto
        WHERE funcionario_id = ? AND saida IS NULL
        ORDER BY entrada DESC LIMIT 1
    """, (funcionario_id,))
    ponto_aberto = cursor.fetchone()

    agora = datetime.datetime.now()

    if ponto_aberto is None:
        # Nenhum ponto aberto -> registrar entrada
        cursor.execute("""
            INSERT INTO ponto (funcionario_id, entrada) VALUES (?, ?)
        """, (funcionario_id, agora))
        print(f"✅ Entrada registrada para matrícula {matricula} às {agora.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        # Ponto aberto existe -> registrar saída
        ponto_id = ponto_aberto[0]
        entrada = datetime.datetime.strptime(ponto_aberto[1], '%Y-%m-%d %H:%M:%S')
        # Lógica simples: só permite saída posterior à entrada
        if agora <= entrada:
            print("❌ Horário de saída não pode ser anterior à entrada.")
            desconectar(con)
            return

        cursor.execute("""
            UPDATE ponto SET saida = ? WHERE id = ?
        """, (agora, ponto_id))
        print(f"✅ Saída registrada para matrícula {matricula} às {agora.strftime('%Y-%m-%d %H:%M:%S')}")

    desconectar(con)

def menu_ponto():
    while True:
        print("\n🕒 Sistema de ponto")
        matricula = input("Digite sua matrícula (ou 'sair' para encerrar): ").strip()
        if matricula.lower() == 'sair':
            break
        registrar_ponto(matricula)

if __name__ == '__main__':
    menu_ponto()
