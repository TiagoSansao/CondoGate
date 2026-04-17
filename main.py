from dados import carregar_moradores, carregar_visitantes, carregar_visitas
from relatorios import (
    relatorio_por_morador,
    relatorio_por_periodo,
    relatorio_por_visitante,
)


def main():
    moradores = carregar_moradores()
    visitantes = carregar_visitantes()
    visitas = carregar_visitas()

    while True:
        print("\n=== Relatorios de visitas ===")
        print("1 - Por periodo")
        print("2 - Por morador")
        print("3 - Por visitante")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            relatorio_por_periodo(visitas, moradores, visitantes)
        elif opcao == "2":
            relatorio_por_morador(visitas, moradores, visitantes)
        elif opcao == "3":
            relatorio_por_visitante(visitas, moradores, visitantes)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
