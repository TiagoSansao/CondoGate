from enum import Enum
from datetime import datetime
from entidades.visitante import Visitante
from entidades.vaga import Vaga


class StatusVisita(Enum):
    ATIVA = 1
    FINALIZADA = 2

class Visita:
    def __init__(self, visitante, entrada, vaga=None):
        self.__visitante = visitante
        self.__entrada = entrada 
        self.__saida = None
        self.__vaga = vaga
        self.__status = StatusVisita.ATIVA

    @property
    def chave(self):
        return f'{self.__visitante.cpf}|{self.__entrada.isoformat()}'

    @property
    def visitante(self):
        return self.__visitante

    @visitante.setter
    def visitante(self, visitante: Visitante):
        if isinstance(visitante, Visitante):
            self.__visitante = visitante

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada: datetime):
        if isinstance(entrada, datetime):
            self.__entrada = entrada

    @property
    def saida(self):
        return self.__saida

    @property
    def vaga(self):
        return self.__vaga

    @vaga.setter
    def vaga(self, vaga: Vaga):
        if isinstance(vaga, Vaga) or vaga is None:
            self.__vaga = vaga
            
    @property
    def status(self):
        return self.__status

    def registrar_saida(self):
        self.__saida = datetime.now()
        self.__status = StatusVisita.FINALIZADA
        if self.__vaga:
            self.__vaga.status = False