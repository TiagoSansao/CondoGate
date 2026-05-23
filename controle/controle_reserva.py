from excecoes.jah_existente_exception import JahExistenteException
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from entidades.reserva import Reserva
from limite.tela_reserva import TelaReserva
from persistence.reserva_dao import ReservaDAO


class ControladorReserva:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
        self.__reserva_dao = ReservaDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def criar_reserva(self):
        dados_reserva = self.__tela_reserva.pega_dados_reserva()

        if dados_reserva is None:
            return

        try:
            morador = self.__controlador_sistema.controlador_morador.morador_dao.get(dados_reserva['cpf'])
            if morador is None:
                raise NaoEncontradoException('Morador', 'CPF', dados_reserva['cpf'])

            espaco = self.__controlador_sistema.controlador_espaco.espaco_dao.get(dados_reserva['espaco'])
            if espaco is None:
                raise NaoEncontradoException('Espaco', 'nome', dados_reserva['espaco'])

            nova_reserva = Reserva(dados_reserva['data'], espaco, morador)

            reserva_conflitante = self.__reserva_dao.get(nova_reserva.chave)

            if reserva_conflitante:
                raise JahExistenteException('Reserva', 'espaço e data', nova_reserva.chave)

            self.__reserva_dao.add(nova_reserva)
            self.__tela_reserva.mostra_mensagem('Reserva realizada com sucesso!', 'sucesso')
        except (JahExistenteException, NaoEncontradoException) as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')

    def listar(self):
        try:
            lista_reservas = self.__reserva_dao.get_all()
            if not len(lista_reservas) >= 1:
                raise ListaVaziaException('reservas')

            lista_dados = list(map(lambda r: {
                'data': r.data.strftime('%d-%m-%Y'),
                'espaco': r.espaco.nome,
                'morador': r.morador.nome,
                'cpf': r.morador.cpf
            }, lista_reservas))

            self.__tela_reserva.mostrar_reservas(lista_dados)
            return True
        except ListaVaziaException as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')
            return False
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')
            return False

    def cancelar(self):
        dados_reserva = self.__tela_reserva.pega_identificacao_reserva()

        if dados_reserva is None:
            return

        try:
            chave = f'{dados_reserva["espaco"]}|{dados_reserva["data"].isoformat()}'
            reserva = self.__reserva_dao.get(chave)

            if reserva is None:
                raise NaoEncontradoException('Reserva', 'espaço e data', chave)

            self.__reserva_dao.remove(chave)
            self.__tela_reserva.mostra_mensagem('Reserva removida com sucesso!', 'sucesso')
        except NaoEncontradoException as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e), 'erro')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_reserva,
            2: self.listar,
            3: self.cancelar,
            0: self.retornar
        }

        while True:
            opcao_selecionada = self.__tela_reserva.tela_opcoes()
            lista_opcoes[int(opcao_selecionada)]()