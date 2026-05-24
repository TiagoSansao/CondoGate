from limite.abstract_tela import AbstractTela
import FreeSimpleGUI as sg

class TelaVisita(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        pass

    def tela_opcoes(self):
        return None

    def pega_dados_visita(self):
        sg.theme(self.ESTILO_JANELA)
        
        layout = [
            [sg.Text('Registrar Visita', font=("Helvetica", 20))],
            [sg.Text('CPF (visitante):'), sg.InputText(key='cpf', size=(25, 1))],
            [sg.Text('Vaga (opcional):'), sg.InputText(key='vaga', size=(25, 1))],
            [sg.Button('OK'), sg.Button('Registrar Visitante'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Portaria').Layout(layout)
        button, values = self.__window.Read()
        self.close()

        if button in (None, 'Cancelar'):
            return None

        if button == 'Registrar Visitante':
            return {'acao': 'novo_visitante'}

        return {
            'acao': 'ok',
            'cpf': values['cpf'],
            'vaga': values['vaga']
        }

    def mostra_mensagem(self, msg, tipo="info"):
        sg.popup(msg, title=tipo.capitalize())

    def close(self):
        if self.__window:
            self.__window.Close()