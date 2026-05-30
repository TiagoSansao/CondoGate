from entidades.pessoa import Pessoa
from entidades.morador import Morador

class Visitante(Pessoa):
    def __init__(self, nome: str, cpf: str, morador_responsavel: Morador):
        super().__init__(nome, cpf)
        self.__morador_responsavel = morador_responsavel

    @property
    def morador_responsavel(self):
        return self.__morador_responsavel

    @morador_responsavel.setter
    def morador_responsavel(self, morador: Morador):
        if isinstance(morador, Morador):
            self.__morador_responsavel = morador