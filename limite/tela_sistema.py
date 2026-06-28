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
            'Gerenciar Reservas': 4,
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
        layout = [[sg.Text('Bem vindo ao CondoGate', font=("Helvetica", 25))],
                  [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
                  [sg.Button('Registrar Entrada/saída')], # 1
                  [sg.Button('Painel de Controle')], # 2
                  [sg.Button('Gerenciamento Geral')], # 3
                  [sg.Button('Gerenciar Reservas')], # 4
                  [sg.Button('Notificar Tempo Excedido')], # 5
                  [sg.Button('Finalizar Sistema')]] # 0

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def init_opcoes_gerenciamento(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('Gerenciamento Geral', font=("Helvetica", 25))],
                  [sg.Text('Selecione o módulo desejado', font=("Helvica", 15))],
                  [sg.Button('Gerenciar Moradores')], # 1
                  [sg.Button('Gerenciar Visitantes')], # 2
                  [sg.Button('Gerenciar Vagas')], # 3
                  [sg.Button('Gerenciar Espaços')], # 4
                  [sg.Button('Voltar')]] # 0

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)
