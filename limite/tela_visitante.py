from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaVisitante(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Visitante': 1,
            'Listar Visitantes': 2,
            'Alterar Visitante': 3,
            'Remover Visitante': 4,
            'Retornar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento de Visitantes', font=("Helvetica", 22, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione a opção desejada', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Incluir Visitante',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Listar Visitantes',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Alterar Visitante',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Remover Visitante',  size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Retornar',           size=(24, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))


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

    def mostrar_visitantes(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Visitantes ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Nome do visitante: " + str(dados["nome"]) + "\n"
        string_dados += "CPF do visitante: " + str(dados["cpf"]) + "\n"
        string_dados += "Nome do morador responsavel: " + str(dados["nome_morador"]) + "\n"
        string_dados += "CPF do morador responsavel: " + str(dados["cpf_morador"]) + "\n"
        string_dados += '\n'

        return string_dados

    def close(self):
        if self.__window:
            self.__window.Close()