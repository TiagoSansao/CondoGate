from datetime import date, time
from entidades.bloco import Bloco

class Espaco:
    def __init__(self, nome: str, capacidade_maxima: int, bloco: Bloco ):
        self.nome = nome 
        self.capacidade_maxima = capacidade_maxima
        self.bloco = bloco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def capacidade_maxima(self):
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima: int):
        self.__capacidade_maxima = capacidade_maxima

    @property
    def bloco(self):
        return self.__bloco
    
    @bloco.setter
    def bloco(self, bloco: Bloco):
        if isinstance(bloco, Bloco):
            self.__bloco = bloco