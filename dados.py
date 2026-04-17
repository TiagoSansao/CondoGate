import json


def carregar_moradores():
    with open("data/moradores.json", "r", encoding="utf-8") as moradores:
        return json.load(moradores)


def carregar_visitantes():
    with open("data/visitantes.json", "r", encoding="utf-8") as visitantes:
        return json.load(visitantes)


def carregar_visitas():
    with open("data/visitas.json", "r", encoding="utf-8") as visitas:
        return json.load(visitas)
