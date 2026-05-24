from limite.tela_vaga import TelaVaga
from entidades.vaga import Vaga
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from persistence.vaga_dao import VagaDAO

class ControladorVaga:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vaga = TelaVaga()
        self.__vaga_dao = VagaDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def vaga_dao(self):
        return self.__vaga_dao
    
    def criar_vaga(self):
        dados_vaga = self.__tela_vaga.pega_dados_vagas()
        if dados_vaga is None:
            return
        try:
            if self.__vaga_dao.get(dados_vaga["id"]):
                raise JahExistenteException("Vaga", "id", dados_vaga["id"])

            nova_vaga = Vaga(dados_vaga["id"])
            self.__vaga_dao.add(nova_vaga)
            self.__tela_vaga.mostra_mensagem("Vaga adicionada com sucesso!")

        except JahExistenteException as e:
            self.__tela_vaga.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_vaga.mostra_mensagem(str(e))

    def listar(self):
        try:
            lista_vagas = self.__vaga_dao.get_all()
            if not len(lista_vagas) >= 1:
                raise ListaVaziaException('vagas')
            
            lista_dados = list(map(lambda m: {
                "id": m.id,
                "status": m.status
            }, lista_vagas))

            self.__tela_vaga.mostrar_vagas(lista_dados)
            return True
        
        except ListaVaziaException as e:
            self.__tela_vaga.mostra_mensagem(str(e))
            return False

        except Exception as e:
            self.__tela_vaga.mostra_mensagem(str(e))
            return False
    
    def remover(self):
        if not self.listar():
            return

        id =  self.__tela_vaga.pega_id()
        if id is None:
            return
        try:
            vaga = self.__vaga_dao.get(id)
            if vaga.status == True:
                self.__tela_vaga.mostra_mensagem("Vaga Ocupada no momento")
                return
            self.__vaga_dao.remove(id)
            self.__tela_vaga.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_vaga.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_vaga.mostra_mensagem(str(e))
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_vaga,
            2: self.listar,
            3: self.remover,
            0: self.retornar
        }
        while True:
            opcao_selecionada = self.__tela_vaga.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()