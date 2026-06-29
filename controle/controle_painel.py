from limite.tela_painel import TelaPainel
from limite.tela_visita import TelaVisita

class ControladorPainel:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_painel = TelaPainel()
        self.__tela_visita = TelaVisita()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_painel(self):
        return self.__tela_painel

    @property
    def tela_visita(self):
        return self.__tela_visita
    
    def visitas(self):
        visitas_ativas = self.__controlador_sistema.controlador_visita.listar_visitas_ativas()
        self.__tela_visita.mostrar_visitas(visitas_ativas)

    def relatorio_visitas(self):
        self.__controlador_sistema.controlador_visita.gerar_relatorio_visitas()

    def vagas (self):
        self.__controlador_sistema.controlador_vaga.listar()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.visitas,
            2: self.vagas,
            3: self.relatorio_visitas,
            0: self.retornar
        }
        while True:
            opcao_selecionada = self.__tela_painel.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()