from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaVisitante(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        pass

    def init_opcoes(self):
        pass

    def pega_dados_visitante(self):
        schema = {
            'title': 'DADOS DO VISITANTE',
            'fieldList': [{
                'label': 'Nome do Visitante',
                'key': 'nome',
                'tooltip': 'Nome completo do visitante',
                'isRequired': True,
                'dataType': InputDataType.TEXTO,
                'parseAs': str
            }, {
                'label': 'CPF do Visitante',
                'key': 'cpf',
                'tooltip': 'Apenas números',
                'isRequired': True,
                'dataType': InputDataType.CPF,
                'parseAs': str
            }, {
                'label': 'CPF do Morador Responsável',
                'key': 'cpf_morador',
                'tooltip': 'CPF do morador que está autorizando o cadastro',
                'isRequired': True,
                'dataType': InputDataType.CPF,
                'parseAs': str
            }]
        }

        return self._pega_dados(schema)

    def close(self):
        if self.__window:
            self.__window.Close()