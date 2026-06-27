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

    def pega_tempo_limite(self, tempo_atual=10):
        sg.theme(self.ESTILO_JANELA)

        layout = [
            [sg.Text('Configurar Tempo Limite de Visita', font=("Helvetica", 16))],
            [sg.Text('Tempo limite (minutos):'), sg.InputText(default_text=str(tempo_atual), key='tempo', size=(10, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Configurar Tempo Limite').Layout(layout)
        button, values = window.Read()
        window.Close()

        if button in (None, 'Cancelar'):
            return None

        try:
            tempo = int(values['tempo'])
            if tempo <= 0:
                raise ValueError
            return {'tempo': tempo}
        except (ValueError, TypeError):
            sg.popup('Tempo limite deve ser um numero inteiro positivo.', title='Erro')
            return None

    def notificar_visitas_excedidas(self, visitas_info):
        msg = 'As seguintes visitas excederam o tempo limite:\n\n'
        for info in visitas_info:
            msg += f"- {info['nome']} (CPF: {info['cpf']}) - {info['tempo_excedido']} min excedidos\n"
        sg.popup(msg, title='Tempo de Visita Excedido', keep_on_top=True)

    def mostra_mensagem(self, msg, tipo="info"):
        sg.popup(msg, title=tipo.capitalize())

    def close(self):
        if self.__window:
            self.__window.Close()