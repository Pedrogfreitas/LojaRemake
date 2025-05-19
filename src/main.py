from estoque import menu_estoque
from gerente import menu_gerente
from ponto import menu_ponto

def main():
    while True:
        print("\nBem-vindo ao sistema da loja!")
        print("Qual função você deseja acessar?")
        print("1 - Bater ponto\n2 - Caixa\n3 - Estoque\n4 - Menu gerente\n5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            menu_ponto()
        elif opcao == "2":
            menu_caixa()
        elif opcao == "3":
            menu_estoque()
        elif opcao == "4":
            menu_gerente()
        elif opcao == "5":
            print("👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
