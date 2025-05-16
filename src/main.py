from estoque import menu_estoque

def main():
    while True:
        print("\nBem-vindo ao sistema da loja!")
        print("Qual função você deseja acessar?")
        print("1 - Bater ponto\n2 - Caixa\n3 - Estoque\n4 - Relatórios\n5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            bater_ponto()
        elif opcao == "2":
            menu_caixa()
        elif opcao == "3":
            menu_estoque()
        elif opcao == "4":
            gerar_relatorios()
        elif opcao == "5":
            print("👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
