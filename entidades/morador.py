from entidades.pessoa import Pessoa
from entidades.residencia import Residencia
from entidades.bloco import Bloco


class Morador(Pessoa):

    def __init__(self, nome: str, cpf: str, numero_celular: str, numero_apartamento: int, bloco_str: str):
        super().__init__(nome, cpf)
        self.__numero_celular = numero_celular
        self.__residencia = Residencia(numero_apartamento, Bloco(bloco_str))

    @property
    def numero_celular(self):
        return self.__numero_celular

    @numero_celular.setter
    def numero_celular(self, numero_celular: str):
        if isinstance(numero_celular, str):
            self.__numero_celular = numero_celular

    def pegar_residencia(self):
        return f"Apto {self.__residencia.numero_apartamento} - Bloco {self.__residencia.bloco.value}"

    def mudar_residencia(self, numero_apartamento: int, bloco_str: str):
        self.__residencia = Residencia(numero_apartamento, Bloco(bloco_str))
