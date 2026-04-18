from persistence.dao import DAO
from entidades.vaga import Vaga


class VagaDAO(DAO):

    def __init__(self):
        super().__init__('vaga', 'id')

    def add(self, vaga: Vaga):
        if (vaga is not None) and isinstance(vaga, Vaga):
            super().add(vaga)

    def update(self, vaga: Vaga):
        if (vaga is not None) and isinstance(vaga, Vaga):
            super().update(vaga)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
