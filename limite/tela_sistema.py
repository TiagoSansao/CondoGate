from limite.abstract_tela import AbstractTela
import FreeSimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Gerenciar Moradores': 1,
            'Gerenciar Vagas': 2,
            'Gerenciar Espaços': 3,
            'Finalizar sistema': 0,
            None: 0,
            'Cancelar': 0,
        }
        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[sg.Text('Bem vindo ao CondoGate', font=("Helvetica", 25))],
                  [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
                  [sg.Button('Gerenciar Moradores')],
                  [sg.Button('Gerenciar Vagas')],
                  [sg.Button('Gerenciar Espaços')],
                  [sg.Button('Finalizar sistema')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)
