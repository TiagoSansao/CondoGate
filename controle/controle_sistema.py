from controle.controle_morador import ControladorMorador
from controle.controle_reserva import ControladorReserva
from controle.controle_vaga import ControladorVaga
from controle.controle_espaco import ControladorEspaco
from controle.controle_visita import ControladorVisita
from controle.controle_visitante import ControladorVisitante
from controle.agendador_visitas import AgendadorVisitas
from controle.controle_painel import ControladorPainel
from limite.tela_sistema import TelaSistema
from queue import Empty, Queue


class ControladorSistema():
    __instance = None

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_visita = ControladorVisita(self)
        self.__controlador_morador = ControladorMorador(self)
        self.__controlador_vaga = ControladorVaga(self)
        self.__controlador_espaco = ControladorEspaco(self)
        self.__controlador_reserva = ControladorReserva(self)
        self.__controlador_visitante = ControladorVisitante(self)
        self.__controlador_painel = ControladorPainel(self)
        self.__fila_notificacoes_visitas = Queue()
        self.__agendador_visitas = AgendadorVisitas(
            self.__controlador_visita.listar_visitas_excedidas,
            self.__enfileirar_visitas_excedidas
        )

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_visita(self):
        return self.__controlador_visita

    @property
    def controlador_morador(self):
        return self.__controlador_morador
    
    @property
    def controlador_vaga(self):
        return self.__controlador_vaga

    @property
    def controlador_espaco(self):
        return self.__controlador_espaco

    @property
    def controlador_reserva(self):
        return self.__controlador_reserva

    @property
    def controlador_visitante(self):
        return self.__controlador_visitante

    @property
    def controlador_painel(self):
        return self.__controlador_painel

    def inicializar_sistema(self):
        self.__agendador_visitas.iniciar()
        self.abre_tela()

    def __enfileirar_visitas_excedidas(self, visitas_excedidas):
        self.__fila_notificacoes_visitas.put(visitas_excedidas)

    def __processar_notificacoes_pendentes(self):
        while True:
            try:
                notificacao = self.__fila_notificacoes_visitas.get_nowait()
            except Empty:
                break

            self.__controlador_visita.notificar_visitas_excedidas(notificacao)

    def abre_tela_morador(self):
        self.controlador_morador.abre_tela()

    def abre_tela_vaga(self):
        self.controlador_vaga.abre_tela()

    def abre_tela_espaco(self):
        self.controlador_espaco.abre_tela()

    def abre_tela_reserva(self):
        self.controlador_reserva.abre_tela()

    def abre_tela_visita(self):
        self.controlador_visita.abre_tela()

    def abre_tela_notificacao(self):
        self.controlador_visita.configurar_notificacao()

    def abre_tela_visitante(self):
        self.controlador_visitante.abre_tela()

    def abre_tela_painel(self):
        self.controlador_painel.abre_tela()

    def abre_tela_gerenciamento(self):
        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes_gerenciamento(
                on_idle=self.__processar_notificacoes_pendentes
            )
            self.__processar_notificacoes_pendentes()

            if int(opcao_selecionada) == 0:
                return

            lista_opcoes = {
                1: self.abre_tela_morador,
                2: self.abre_tela_visitante,
                3: self.abre_tela_vaga,
                4: self.abre_tela_espaco,
            }

            funcao_selecionada = lista_opcoes.get(int(opcao_selecionada))
            if funcao_selecionada:
                funcao_selecionada()

    def encerrar_sistema(self):
        self.__agendador_visitas.parar()
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.abre_tela_visita,
            2: self.abre_tela_painel,
            3: self.abre_tela_gerenciamento,
            4: self.abre_tela_reserva,
            5: self.abre_tela_notificacao,
            0: self.encerrar_sistema
        }

        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes(
                on_idle=self.__processar_notificacoes_pendentes
            )
            self.__processar_notificacoes_pendentes()
            funcao_selecionada = lista_opcoes.get(int(opcao_selecionada))
            if funcao_selecionada:
                funcao_selecionada()
