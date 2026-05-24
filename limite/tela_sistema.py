from limite.abstract_tela import AbstractTela
import FreeSimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None

    def tela_opcoes(self, on_idle=None):
        self.init_opcoes()

        opcoes = {
            'Registrar Entrada/saída': 1,
            'Gerenciar Moradores': 2,
            'Gerenciar Vagas': 3,
            'Gerenciar Espaços': 4,
            'Gerenciar Reservas': 5,
            'Notificar Tempo Excedido': 6,
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

    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('Bem vindo ao CondoGate', font=("Helvetica", 25))],
                  [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
                  [sg.Button('Registrar Entrada/saída')],
                  [sg.Button('Gerenciar Moradores')],
                  [sg.Button('Gerenciar Vagas')],
                  [sg.Button('Gerenciar Espaços')],
                  [sg.Button('Gerenciar Reservas')],
                  [sg.Button('Notificar Tempo Excedido')],
                  [sg.Button('Finalizar Sistema')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)
