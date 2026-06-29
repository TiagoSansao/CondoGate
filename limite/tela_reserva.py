from datetime import datetime

from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaReserva(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Reserva': 1,
            'Listar Reservas': 2,
            'Cancelar Reserva': 3,
            'Retornar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Sistema de Reservas', font=("Helvetica", 22, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione a opção desejada', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Incluir Reserva',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Listar Reservas',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Cancelar Reserva', size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Retornar',         size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))

    def pega_dados_reserva(self):
        schema = {
            'title': 'DADOS RESERVA',
            'fieldList': [{
                'label': 'CPF do Morador',
                'key': 'cpf',
                'tooltip': 'CPF do morador que fará a reserva',
                'isRequired': True,
                'dataType': InputDataType.CPF,
                'parseAs': str
            }, {
                'label': 'Espaco',
                'key': 'espaco',
                'tooltip': 'Nome do espaco',
                'isRequired': True,
                'dataType': InputDataType.TEXTO,
                'parseAs': str
            }, {
                'label': 'Data',
                'key': 'data',
                'tooltip': 'Data da reserva no formato DD-MM-YYYY',
                'isRequired': True,
                'dataType': InputDataType.DATA,
                'parseAs': lambda valor: datetime.strptime(valor, '%d-%m-%Y').date()
            }]
        }

        return self._pega_dados(schema)

    def pega_identificacao_reserva(self):
        schema = {
            'title': 'CANCELAR RESERVA',
            'fieldList': [{
                'label': 'Espaco',
                'key': 'espaco',
                'tooltip': 'Nome do espaco',
                'isRequired': True,
                'dataType': InputDataType.TEXTO,
                'parseAs': str
            }, {
                'label': 'Data',
                'key': 'data',
                'tooltip': 'Data da reserva no formato DD-MM-YYYY',
                'isRequired': True,
                'dataType': InputDataType.DATA,
                'parseAs': lambda valor: datetime.strptime(valor, '%d-%m-%Y').date()
            }]
        }

        return self._pega_dados(schema)

    def mostrar(self, dados):
        string_dados = ''
        string_dados += 'Data da reserva: ' + str(dados['data']) + '\n'
        string_dados += 'Espaco: ' + str(dados['espaco']) + '\n'
        string_dados += 'Morador: ' + str(dados['morador']) + ' - CPF ' + str(dados['cpf']) + '\n'
        string_dados += '\n'
        return string_dados

    def mostrar_reservas(self, lista_dados):
        string_lista = ''
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Reservas ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def close(self):
        self.__window.Close()