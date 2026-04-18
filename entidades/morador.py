from entidades.pessoa import Pessoa


class Morador(Pessoa):

    def __init__(self, nome: str, cpf: str, numero_celular: str):
        super().__init__(nome, cpf)
        self.__numero_celular = numero_celular

    @property
    def numero_celular(self):
        return self.__numero_celular

    @numero_celular.setter
    def numero_celular(self, numero_celular: str):
        if isinstance(numero_celular, str):
            self.__numero_celular = numero_celular
