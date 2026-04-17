from entidades.pessoa import Pessoa


class Visitante(Pessoa):
    def __init__(self, cpf: str, nome: str):
        super().__init__(cpf, nome)
