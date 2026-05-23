
from datetime import date

from entidades.espaco import Espaco
from entidades.morador import Morador
from entidades.status import Status


class Reserva:
    def __init__(self, data: date, status: Status, espaco: Espaco, morador: Morador):
        self.__data = data
        self.__status = status
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
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: Status):
        if isinstance(status, Status):
            self.__status = status

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

    def set_status(self, status: Status):
        self.status = status

    def cancelar_reserva(self):
        self.__status = Status.CANCELADA