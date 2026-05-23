from persistence.dao import DAO
from entidades.espaco import Espaco


class EspacoDAO(DAO):
    def __init__(self):
        super().__init__('espaco', 'nome')

    def add(self, espaco: Espaco):
        if (espaco is not None) and isinstance(espaco, Espaco) and isinstance(espaco.nome, str):
            super().add(espaco)

    def update(self, espaco: Espaco):
        if (espaco is not None) and isinstance(espaco, Espaco) and isinstance(espaco.nome, str):
            super().update(espaco)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()