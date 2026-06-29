from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import FreeSimpleGUI as sg


class TelaVaga(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Vaga': 1,
            'Listar Vagas': 2,
            'Remover Vaga': 3,
            'Retornar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento de Vagas', font=("Helvetica", 22, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione a opção desejada', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Incluir Vaga',  size=(22, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Listar Vagas',  size=(22, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Remover Vaga',  size=(22, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Retornar',      size=(22, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))

    def pega_id(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('SELECIONAR', font=("Helvica", 20), justification='center')],
                  [sg.Text('Digite o ID', font=("Helvica", 15))],
                  [sg.Text('ID:', size=(15, 1)),
                   sg.InputText(key='codigo', tooltip='Digite o ID da vaga', size=(20, 1))],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
        window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.Close()
                return None

            window.Close()
            return int(self._extrair_valor(values, 'codigo'))

    def pega_dados_vagas(self):
        schema = {
            "title": "DADOS VAGAS",
            "fieldList": [{
                "label": "Id",
                "key": "id",
                "tooltip": "Id da vaga",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }]
        }

        return self._pega_dados(schema)

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Id da vaga: " + str(dados["id"]) + "\n"
        string_dados += "Status da vaga: " + ("Ocupada" if dados["status"] else "Disponível") + "\n"
        return string_dados

    def mostrar_vagas(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Vagas ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))
    def close(self):
        self.__window.Close()
