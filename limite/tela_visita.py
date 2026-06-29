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
            [sg.Text('Registrar Visita', font=("Helvetica", 22, 'bold'), justification='center', expand_x=True, pad=(0, 10))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Text('CPF (visitante):', size=(18, 1), font=("Helvetica", 11)),
             sg.InputText(key='cpf', size=(25, 1), font=("Helvetica", 11))],
            [sg.Text('Vaga (opcional):', size=(18, 1), font=("Helvetica", 11)),
             sg.InputText(key='vaga', size=(25, 1), font=("Helvetica", 11))],
            [sg.HorizontalSeparator(pad=(0, 8))],
            [sg.Button('OK', size=(14, 1), font=("Helvetica", 11), pad=(5, 3)),
             sg.Button('Registrar Visitante', size=(20, 1), font=("Helvetica", 11), pad=(5, 3)),
             sg.Button('Cancelar', size=(14, 1), font=("Helvetica", 11), pad=(5, 3))],
        ]
        self.__window = sg.Window('Portaria', layout, element_justification='center', margins=(30, 20))
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

    def mostrar(self, dados):
        if dados is None:
            return ""

        if isinstance(dados, dict):
            status = dados.get('status')
            visitante = dados.get('visitante')
            nome = dados.get('nome')
            cpf = dados.get('cpf')
            vaga = dados.get('vaga')
            entrada = dados.get('entrada')
        else:
            status = getattr(dados, 'status', None)
            visitante = getattr(dados, 'visitante', None)
            nome = getattr(visitante, 'nome', None) if visitante else None
            cpf = getattr(visitante, 'cpf', None) if visitante else None
            vaga = getattr(dados, 'vaga', None)
            entrada = getattr(dados, 'entrada', None)

        if status is not None:
            if hasattr(status, 'name'):
                status_nome = status.name
            else:
                status_nome = str(status)

            if status_nome != 'ATIVA' and status_nome != 'StatusVisita.ATIVA':
                return ""

        nome = nome or 'Não informado'
        cpf = cpf or 'Não informado'

        if vaga is None:
            vaga_ocupada = 'Nenhuma'
        elif isinstance(vaga, dict):
            vaga_ocupada = vaga.get('id', vaga.get('numero', 'Não informada'))
        else:
            vaga_ocupada = getattr(vaga, 'id', getattr(vaga, 'numero', 'Não informada'))

        if entrada is None:
            horario_entrada = 'Não informado'
        elif isinstance(entrada, str):
            horario_entrada = entrada
        else:
            horario_entrada = entrada.strftime('%d/%m/%Y %H:%M:%S')

        return (
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n"
            f"Vaga ocupada: {vaga_ocupada}\n"
            f"Horário de entrada: {horario_entrada}\n\n"
        )

    def mostrar_visitas(self, lista_dados):
        string_lista = ""
        for dados in lista_dados or []:
            string_lista += self.mostrar(dados)

        if not string_lista:
            string_lista = "Nenhuma visita ativa no momento."

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Visitas Ativas ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar_relatorio_visitas(self, lista_dados):
        string_lista = ""

        for dados in lista_dados or []:
            nome = dados.get('nome', 'Não informado')
            cpf = dados.get('cpf', 'Não informado')
            entrada = dados.get('entrada')
            status = dados.get('status', 'Não informado')
            saida = dados.get('saida')

            if entrada is None:
                data_entrada = 'Não informado'
                hora_entrada = 'Não informado'
            else:
                data_entrada = entrada.strftime('%d/%m/%Y')
                hora_entrada = entrada.strftime('%H:%M:%S')

            if saida is None:
                saida_texto = 'Ainda não saiu'
            else:
                saida_texto = saida.strftime('%d/%m/%Y %H:%M:%S')

            string_lista += (
                f"Nome: {nome}\n"
                f"CPF: {cpf}\n"
                f"Data de entrada: {data_entrada}\n"
                f"Hora de entrada: {hora_entrada}\n"
                f"Status: {status}\n"
                f"Saída: {saida_texto}\n"
                "----------------------------------------\n"
            )

        if not string_lista:
            string_lista = "Nenhuma visita registrada no momento."

        sg.popup_scrolled(string_lista,
                          title='Relatório de Visitas',
                          font=("Helvetica", 12),
                          size=(80, 25))

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