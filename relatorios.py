from datetime import datetime


FORMATO_DATA_HORA = "%Y-%m-%d %H:%M"


def limpar_cpf(cpf):
    return cpf.replace(".", "").replace("-", "").strip()


def buscar_por_cpf(pessoas, cpf):
    for pessoa in pessoas:
        if pessoa["cpf"] == cpf:
            return pessoa
    return None


def imprimir_visitas(visitas, moradores, visitantes):
    if not visitas:
        print("Nenhuma visita encontrada.")
        return

    for visita in visitas:
        morador = buscar_por_cpf(moradores, visita["morador_cpf"])
        visitante = buscar_por_cpf(visitantes, visita["visitante_cpf"])

        nome_morador = morador["nome"] if morador else "Morador nao encontrado"
        nome_visitante = visitante["nome"] if visitante else "Visitante nao encontrado"

        print("-" * 50)
        print(f"Morador: {nome_morador} | CPF: {visita['morador_cpf']}")
        print(f"Visitante: {nome_visitante} | CPF: {visita['visitante_cpf']}")
        print(f"Entrada: {visita['data_hora_entrada']}")
        print(f"Saida: {visita['data_hora_saida']}")


def relatorio_por_periodo(visitas, moradores, visitantes):
    data_inicio = input("Data inicial (AAAA-MM-DD): ")
    data_fim = input("Data final (AAAA-MM-DD): ")

    try:
        inicio = datetime.strptime(data_inicio + " 00:00", FORMATO_DATA_HORA)
        fim = datetime.strptime(data_fim + " 23:59", FORMATO_DATA_HORA)
    except ValueError:
        print("Data invalida. Use o formato AAAA-MM-DD.")
        return

    visitas_filtradas = []

    for visita in visitas:
        entrada = datetime.strptime(visita["data_hora_entrada"], FORMATO_DATA_HORA)

        if inicio <= entrada <= fim:
            visitas_filtradas.append(visita)

    print("\nRelatorio de visitas por periodo")
    imprimir_visitas(visitas_filtradas, moradores, visitantes)


def relatorio_por_morador(visitas, moradores, visitantes):
    cpf = limpar_cpf(input("CPF do morador: "))
    visitas_filtradas = []

    for visita in visitas:
        if visita["morador_cpf"] == cpf:
            visitas_filtradas.append(visita)

    print("\nRelatorio de visitas por morador")
    imprimir_visitas(visitas_filtradas, moradores, visitantes)


def relatorio_por_visitante(visitas, moradores, visitantes):
    cpf = limpar_cpf(input("CPF do visitante: "))
    visitas_filtradas = []

    for visita in visitas:
        if visita["visitante_cpf"] == cpf:
            visitas_filtradas.append(visita)

    print("\nRelatorio de visitas por visitante")
    imprimir_visitas(visitas_filtradas, moradores, visitantes)
