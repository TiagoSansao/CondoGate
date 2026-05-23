from persistence.dao import DAO
from entidades.reserva import Reserva


class ReservaDAO(DAO):

    def __init__(self):
        super().__init__('reserva', 'chave')

    def add(self, reserva: Reserva):
        if (reserva is not None) and isinstance(reserva, Reserva):
            super().add(reserva)

    def update(self, reserva: Reserva):
        if (reserva is not None) and isinstance(reserva, Reserva):
            super().update(reserva)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()