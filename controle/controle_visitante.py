from excecoes.jah_existente_exception import JahExistenteException
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from entidades.visitante import Visitante
from limite.tela_visitante import TelaVisitante
from persistence.visitante_dao import VisitanteDAO


class ControladorVisitante:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_visitante = TelaVisitante()
        self.__visitante_dao = VisitanteDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
        
    @property
    def visitante_dao(self):
        return self.__visitante_dao

    def incluir(self):
        dados_visitante = self.__tela_visitante.pega_dados_visitante()

        if dados_visitante is None:
            return

        cpf_visitante = dados_visitante['cpf']
        
        try:
            if self.__visitante_dao.get(cpf_visitante):
                raise JahExistenteException('Visitante', 'CPF', cpf_visitante)

            cpf_morador = dados_visitante['cpf_morador']
            morador = self.__controlador_sistema.controlador_morador.morador_dao.get(cpf_morador)
            
            if morador is None:
                raise NaoEncontradoException('Morador responsável', 'CPF', cpf_morador)

            novo_visitante = Visitante(dados_visitante['nome'], cpf_visitante, morador)
            self.__visitante_dao.add(novo_visitante)
            
            self.__tela_visitante.mostra_mensagem('Visitante cadastrado com sucesso!', 'sucesso')
            
        except (JahExistenteException, NaoEncontradoException) as e:
            self.__tela_visitante.mostra_mensagem(str(e), 'erro')
        except Exception as e:
            self.__tela_visitante.mostra_mensagem(f"Ocorreu um erro: {str(e)}", 'erro')

    def abre_tela(self):
        pass