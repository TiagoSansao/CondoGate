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

    def listar(self):
        try:
            lista_visitantes = self.__visitante_dao.get_all()
            if not len(lista_visitantes) >= 1:
                raise ListaVaziaException('visiatntes')
            
            lista_dados = list(map(lambda m: {
                "nome": m.nome,
                "cpf": m.cpf,
                "nome_morador": m.morador_responsavel.nome,
                "cpf_morador": m.morador_responsavel.cpf
            }, lista_visitantes))

            self.__tela_visitante.mostrar_visitantes(lista_dados)
            return True
        
        except ListaVaziaException as e:
            self.__tela_visitante.mostra_mensagem(str(e))
            return False
        
        except Exception as e:
            self.__tela_visitante.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return

        cpf_atual = self.__tela_visitante.pega_cpf()
        if cpf_atual is None:
            return

        dados_visitante = self.__tela_visitante.pega_dados_visitante()
        if dados_visitante is None:
            return

        try:
            visitante = self.__visitante_dao.get(cpf_atual)
            if not visitante:
                raise NaoEncontradoException('Visitante', 'CPF', cpf_atual)

            novo_cpf = dados_visitante['cpf']
            if novo_cpf != cpf_atual and self.__visitante_dao.get(novo_cpf):
                raise JahExistenteException('Visitante', 'CPF', novo_cpf)

            cpf_morador = dados_visitante['cpf_morador']
            morador = self.__controlador_sistema.controlador_morador.morador_dao.get(cpf_morador)
            if morador is None:
                raise NaoEncontradoException('Morador responsável', 'CPF', cpf_morador)

            visitante.nome = dados_visitante['nome']
            visitante.cpf = novo_cpf
            visitante.morador_responsavel = morador

            if novo_cpf != cpf_atual:
                self.__visitante_dao.remove(cpf_atual)
                self.__visitante_dao.add(visitante)
            else:
                self.__visitante_dao.update(visitante)

            self.__tela_visitante.mostra_mensagem('Visitante alterado com sucesso!', 'sucesso')
        except (NaoEncontradoException, JahExistenteException) as e:
            self.__tela_visitante.mostra_mensagem(str(e), 'erro')
        except Exception as e:
            self.__tela_visitante.mostra_mensagem(f"Ocorreu um erro: {str(e)}", 'erro')

    def remover(self):
        if not self.listar():
            return
        
        cpf = self.__tela_visitante.pega_cpf()

        if cpf is None:
            return
        
        try:
            visitante = self.__visitante_dao.get(cpf)
            if not visitante:
                raise NaoEncontradoException
            self.__visitante_dao.remove(cpf)
            self.__tela_visitante.mostra_mensagem("Removido com sucesso. ")
        
        except NaoEncontradoException as e:
            self.__tela_visitante.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_visitante.mostra_mensagem(str(e))

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir,
            2: self.listar,
            3: self.alterar,
            4: self.remover,
            0: self.retornar
        }
        while True:
            opcao_selecionada = self.__tela_visitante.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()