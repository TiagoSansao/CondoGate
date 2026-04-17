from entidades.pessoa import Pessoa


class Morador(Pessoa):
    def __init__(self, cpf: str, nome: str, numero_celular: str): 
        super().__init__(cpf, nome)
        self.__numero_celular = numero_celular

    def get_numero_celular(self):
        return self.__numero_celular
