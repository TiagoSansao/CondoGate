from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaEspaco(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Espaco': 1,
            'Listar Espacos': 2,
            'Remover Espaco': 3,
            'Retornar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('Gerenciamento de espacos', font=("Helvetica", 25))],
                  [sg.Text('Selecione a opcao desejada', font=("Helvica", 15))],
                  [sg.Button('Incluir Espaco')],
                  [sg.Button('Listar Espacos')],
                  [sg.Button('Remover Espaco')],
                  [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_nome(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('SELECIONAR', font=("Helvica", 20), justification='center')],
                  [sg.Text('Digite o nome do espaco', font=("Helvica", 15))],
                  [sg.Text('Nome:', size=(15, 1)),
                   sg.InputText(key='nome', tooltip='Digite o nome do espaco', size=(20, 1))],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.Close()
                return None

            if not self._validar_campos(values, [("obrigatorio", "nome", "Nome")]):
                continue

            window.Close()
            return str(self._extrair_valor(values, 'nome'))

    def pega_dados_espaco(self):
        schema = {
            "title": "DADOS ESPACO",
            "fieldList": [{
                "label": "Nome",
                "key": "nome",
                "tooltip": "Nome do espaco",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "Capacidade Maxima",
                "key": "capacidade_maxima",
                "tooltip": "Capacidade maxima do espaco",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Bloco (A-D)",
                "key": "bloco",
                "tooltip": "Bloco do espaco (A, B, C ou D)",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }]
        }

        return self._pega_dados(schema)

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Nome do espaco: " + str(dados["nome"]) + "\n"
        string_dados += "Capacidade maxima: " + str(dados["capacidade_maxima"]) + "\n"
        string_dados += "Bloco: " + str(dados["bloco"]) + "\n"
        string_dados += '\n'
        return string_dados

    def mostrar_espacos(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Espacos ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def close(self):
        self.__window.Close()
