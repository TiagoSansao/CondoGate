from entidades.bloco import Bloco


class Residencia:

    def __init__(self, numero_apartamento: int, bloco: Bloco):
        self.__numero_apartamento = numero_apartamento
        self.__bloco = bloco

    @property
    def numero_apartamento(self):
        return self.__numero_apartamento

    @numero_apartamento.setter
    def numero_apartamento(self, numero_apartamento: int):
        if isinstance(numero_apartamento, int):
            self.__numero_apartamento = numero_apartamento

    @property
    def bloco(self):
        return self.__bloco

    @bloco.setter
    def bloco(self, bloco: Bloco):
        if isinstance(bloco, Bloco):
            self.__bloco = bloco
