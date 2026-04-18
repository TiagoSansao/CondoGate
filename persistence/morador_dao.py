from persistence.dao import DAO
from entidades.morador import Morador


class MoradorDAO(DAO):

    def __init__(self):
        super().__init__('morador', 'cpf')

    def add(self, morador: Morador):
        if (morador is not None) and isinstance(morador, Morador) and isinstance(morador.cpf, str):
            super().add(morador)

    def update(self, morador: Morador):
        if (morador is not None) and isinstance(morador, Morador) and isinstance(morador.cpf, str):
            super().update(morador)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
