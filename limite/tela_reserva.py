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
        layout = [[sg.Text('Gerenciamento de reservas', font=("Helvetica", 25))],
                  [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
                  [sg.Button('Incluir Reserva')],
                  [sg.Button('Listar Reservas')],
                  [sg.Button('Cancelar Reserva')],
                  [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

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
        string_dados += 'Status da reserva: ' + str(dados['status']) + '\n'
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