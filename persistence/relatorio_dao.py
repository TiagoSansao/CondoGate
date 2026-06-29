from persistence.dao import DAO
from entidades.visita import Visita


class RelatorioDAO(DAO):

    def __init__(self):
        super().__init__('relatorio_visitas', 'chave')

    def add(self, visita: Visita):
        if (visita is not None) and isinstance(visita, Visita):
            super().add(visita)

    def update(self, visita: Visita):
        if (visita is not None) and isinstance(visita, Visita):
            super().update(visita)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
