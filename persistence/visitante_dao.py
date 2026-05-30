from persistence.dao import DAO
from entidades.visitante import Visitante


class VisitanteDAO(DAO):
    def __init__(self):
        super().__init__('visitantes', 'cpf')

    def add(self, visitante: Visitante):
        if isinstance(visitante, Visitante):
            super().add(visitante)