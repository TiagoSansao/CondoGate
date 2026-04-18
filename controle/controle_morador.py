from limite.tela_morador import TelaMorador
from entidades.morador import Morador
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from persistence.morador_dao import MoradorDAO


class ControladorMorador():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_morador = TelaMorador()
        self.__morador_dao = MoradorDAO()

    @property
    def morador_dao(self):
        return self.__morador_dao

    def adicionar(self):
        dados_morador = self.__tela_morador.pega_dados_morador()

        if dados_morador is None:
            return

        try:
            if self.__morador_dao.get(dados_morador["cpf"]):
                raise JahExistenteException("Morador", "CPF", dados_morador["cpf"])

            novo_morador = Morador(dados_morador["nome"], dados_morador["cpf"], dados_morador["numero_celular"],
                                   dados_morador["numero_apartamento"], dados_morador["bloco"].upper())
            self.__morador_dao.add(novo_morador)
            self.__tela_morador.mostra_mensagem("Morador adicionado com sucesso!")
        except JahExistenteException as e:
            self.__tela_morador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_morador.mostra_mensagem(str(e))

    def remover(self):
        if not self.listar():
            return

        cpf = self.__tela_morador.pega_cpf()

        if cpf is None:
            return

        try:
            self.__morador_dao.remove(cpf)
            self.__tela_morador.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_morador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_morador.mostra_mensagem(str(e))

    def listar(self):
        try:
            lista_moradores = self.__morador_dao.get_all()
            if not len(lista_moradores) >= 1:
                raise ListaVaziaException('moradores')

            lista_dados = list(map(lambda m: {
                "nome": m.nome,
                "cpf": m.cpf,
                "numero_celular": m.numero_celular,
                "residencia": m.pegar_residencia()
            }, lista_moradores))

            self.__tela_morador.mostrar_moradores(lista_dados)
            return True
        except ListaVaziaException as e:
            self.__tela_morador.mostra_mensagem(str(e))
            return False
        except Exception as e:
            self.__tela_morador.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return

        dados_morador = self.__tela_morador.pega_dados_morador()

        if dados_morador is None:
            return

        try:
            morador = self.__morador_dao.get(dados_morador["cpf"])

            if not morador:
                raise NaoEncontradoException("Morador", "CPF", dados_morador["cpf"])

            morador.nome = dados_morador["nome"]
            morador.numero_celular = dados_morador["numero_celular"]
            morador.mudar_residencia(dados_morador["numero_apartamento"], dados_morador["bloco"].upper())
            self.__morador_dao.update(morador)
            self.__tela_morador.mostra_mensagem("Alterado com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_morador.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_morador.mostra_mensagem(str(e))

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_morador.tela_opcoes()]()
