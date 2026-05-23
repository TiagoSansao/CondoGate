
from datetime import date

from entidades.espaco import Espaco
from entidades.morador import Morador


class Reserva:
    def __init__(self, data: date, espaco: Espaco, morador: Morador):
        self.__data = data
        self.__espaco = espaco
        self.__morador = morador

    @property
    def chave(self):
        return f'{self.__espaco.nome}|{self.__data.isoformat()}'

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def espaco(self):
        return self.__espaco

    @espaco.setter
    def espaco(self, espaco: "Espaco"):
        if isinstance(espaco, Espaco):
            self.__espaco = espaco

    @property
    def morador(self):
        return self.__morador

    @morador.setter
    def morador(self, morador: Morador):
        if isinstance(morador, Morador):
            self.__morador = morador

    def get_data(self):
        return self.__data