from controle.controle_morador import ControladorMorador
from controle.controle_vaga import ControladorVaga
from limite.tela_sistema import TelaSistema


class ControladorSistema():
    __instance = None

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_morador = ControladorMorador(self)
        self.__controlador_vaga = ControladorVaga(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_morador(self):
        return self.__controlador_morador
    
    @property
    def controlador_vaga(self):
        return self.__controlador_vaga

    def inicializar_sistema(self):
        self.abre_tela()

    def abre_tela_morador(self):
        self.controlador_morador.abre_tela()

    def abre_tela_vaga(self):
        self.controlador_vaga.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            2: self.abre_tela_vaga,
            1: self.abre_tela_morador,
            0: self.encerrar_sistema
        }

        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()
