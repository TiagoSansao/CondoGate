

from limite.tela_espaco import TelaEspaco
from entidades.espaco import Espaco
from entidades.bloco import Bloco
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from persistence.espaco_dao import EspacoDAO


class ControladorEspaco:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_espaco = TelaEspaco()
        self.__espaco_dao = EspacoDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def espaco_dao(self):
        return self.__espaco_dao

    def criar_espaco(self):
        dados_espaco = self.__tela_espaco.pega_dados_espaco()

        if dados_espaco is None:
            return

        try:
            if self.__espaco_dao.get(dados_espaco["nome"]):
                raise JahExistenteException("Espaco", "nome", dados_espaco["nome"])

            novo_espaco = Espaco(
                dados_espaco["nome"],
                dados_espaco["capacidade_maxima"],
                Bloco(dados_espaco["bloco"].upper())
            )
            self.__espaco_dao.add(novo_espaco)
            self.__tela_espaco.mostra_mensagem("Espaco adicionado com sucesso!")
        except JahExistenteException as e:
            self.__tela_espaco.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_espaco.mostra_mensagem(str(e))

    def listar(self):
        try:
            lista_espacos = self.__espaco_dao.get_all()
            if not len(lista_espacos) >= 1:
                raise ListaVaziaException('espacos')

            lista_dados = list(map(lambda e: {
                "nome": e.nome,
                "capacidade_maxima": e.capacidade_maxima,
                "bloco": e.bloco.value
            }, lista_espacos))

            self.__tela_espaco.mostrar_espacos(lista_dados)
            return True

        except ListaVaziaException as e:
            self.__tela_espaco.mostra_mensagem(str(e))
            return False

        except Exception as e:
            self.__tela_espaco.mostra_mensagem(str(e))
            return False

    def remover(self):
        if not self.listar():
            return

        nome = self.__tela_espaco.pega_nome()
        if nome is None:
            return

        try:
            self.__espaco_dao.remove(nome)
            self.__tela_espaco.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_espaco.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_espaco.mostra_mensagem(str(e))

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_espaco,
            2: self.listar,
            3: self.remover,
            0: self.retornar
        }

        while True:
            opcao_selecionada = self.__tela_espaco.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()