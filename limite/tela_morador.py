from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaMorador(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Morador': 1,
            'Alterar Morador': 2,
            'Listar Moradores': 3,
            'Remover Morador': 4,
            'Retornar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento de Moradores', font=("Helvetica", 22, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione a opção desejada', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Incluir Morador',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Alterar Morador',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Listar Moradores', size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Remover Morador',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Retornar',         size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))

    def pega_dados_morador(self):
        schema = {
            "title": "DADOS MORADOR",
            "fieldList": [{
                "label": "Nome",
                "key": "nome",
                "tooltip": "Nome completo",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "CPF",
                "key": "cpf",
                "tooltip": "Apenas números (ex: 12645972900)",
                "isRequired": True,
                "dataType": InputDataType.CPF,
                "parseAs": str
            }, {
                "label": "Celular",
                "key": "numero_celular",
                "tooltip": "Informe o celular (Ex.: 47988303706)",
                "isRequired": True,
                "dataType": InputDataType.TELEFONE,
                "parseAs": str
            }, {
                "label": "Nº Apartamento",
                "key": "numero_apartamento",
                "tooltip": "Número do apartamento (ex: 101)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Bloco (A-D)",
                "key": "bloco",
                "tooltip": "Bloco do apartamento (A, B, C ou D)",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }]
        }

        return self._pega_dados(schema)

    def mostrar_moradores(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Moradores ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Nome do morador: " + str(dados["nome"]) + "\n"
        string_dados += "CPF do morador: " + str(dados["cpf"]) + "\n"
        string_dados += "Celular do morador: " + str(dados["numero_celular"]) + "\n"
        string_dados += "Residência: " + str(dados["residencia"]) + "\n"
        string_dados += '\n'

        return string_dados

    def close(self):
        self.__window.Close()
