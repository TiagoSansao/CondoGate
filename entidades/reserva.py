
from datetime import date, time

from entidades.status import Status
from entidade.espaco import Espaco


class Reserva:
    def __init__(self, data: date, hora_inicio: time, hora_fim: time, status: Status, espaco: Espaco):
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__status = status
        self.__espaco = espaco

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: time):
        if isinstance(hora_inicio, time):
            self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self):
        return self.__hora_fim

    @hora_fim.setter
    def hora_fim(self, hora_fim: time):
        if isinstance(hora_fim, time):
            self.__hora_fim = hora_fim

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
        self.__espaco = espaco

    def get_data(self):
        return self.__data

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_fim(self):
        return self.__hora_fim

    def set_status(self, status: Status):
        self.status = status

    def cancelar_reserva(self):
        self.__status = Status.CANCELADA