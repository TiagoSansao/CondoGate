from limite.abstract_tela import AbstractTela
import FreeSimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None

    def tela_opcoes(self, on_idle=None):
        self.init_opcoes()

        opcoes = {
            'Registrar Entrada/saída': 1,
            'Painel de Controle': 2,
            'Gerenciamento Geral': 3,
            'Sistema de Reservas': 4,
            'Notificar Tempo Excedido': 5,
            'Finalizar Sistema': 0,
            None: 0,
            'Cancelar': 0,
        }

        while True:
            if on_idle:
                button, _ = self.__window.read(timeout=500)
                if button == sg.TIMEOUT_KEY:
                    on_idle()
                    continue
            else:
                button, _ = self.__window.read()

            opcao = opcoes.get(button, 0)
            self.close()
            return opcao

    def tela_opcoes_gerenciamento(self, on_idle=None):
        self.init_opcoes_gerenciamento()

        opcoes = {
            'Gerenciar Moradores': 1,
            'Gerenciar Visitantes': 2,
            'Gerenciar Vagas': 3,
            'Gerenciar Espaços': 4,
            'Voltar': 0,
            None: 0,
            'Cancelar': 0,
        }

        while True:
            if on_idle:
                button, _ = self.__window.read(timeout=500)
                if button == sg.TIMEOUT_KEY:
                    on_idle()
                    continue
            else:
                button, _ = self.__window.read()

            opcao = opcoes.get(button, 0)
            self.close()
            return opcao

    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('🏢 CondoGate', font=("Helvetica", 28, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione a opção desejada', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Registrar Entrada/saída', size=(28, 2), font=("Helvetica", 13, 'bold'),
                       button_color=('#ffffff', '#1a6fc4'), pad=(5, 6))],
            [sg.Button('Painel de Controle',      size=(28, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Gerenciamento Geral',      size=(28, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Sistema de Reservas',      size=(28, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Notificar Tempo Excedido', size=(28, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Finalizar Sistema',        size=(28, 1), font=("Helvetica", 11),
                       button_color=('#ffffff', '#8b0000'), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))

    def init_opcoes_gerenciamento(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento Geral', font=("Helvetica", 24, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Selecione o módulo desejado', font=("Helvetica", 12), justification='center', expand_x=True, text_color='#aaaaaa', pad=(0, 5))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Gerenciar Moradores',  size=(26, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Gerenciar Visitantes', size=(26, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Gerenciar Vagas',      size=(26, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.Button('Gerenciar Espaços',    size=(26, 1), font=("Helvetica", 11), pad=(5, 3))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('Voltar',               size=(26, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window(self.TITULO_BASE, layout, element_justification='center', margins=(30, 20))
