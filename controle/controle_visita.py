from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from entidades.visita import Visita, StatusVisita
from limite.tela_visita import TelaVisita
from persistence.visita_dao import VisitaDAO
from datetime import datetime


class ControladorVisita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_visita = TelaVisita()
        self.__visita_dao = VisitaDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def registrar_visita(self):
        dados_visita = self.__tela_visita.pega_dados_visita()

        if dados_visita is None:
            return

        if dados_visita.get('acao') == 'novo_visitante':
            self.registrar_novo_visitante()
            return

        cpf = dados_visita.get('cpf')
        id_vaga = dados_visita.get('vaga')

        try:
            visitante = self.__controlador_sistema.controlador_visitante.visitante_dao.get(cpf)
            if visitante is None:
                raise NaoEncontradoException('Visitante', 'CPF', cpf)

            visitas_gerais = self.__visita_dao.get_all()
            visita_ativa = None
            for v in visitas_gerais:
                if v.visitante.cpf == cpf and v.status == StatusVisita.ATIVA:
                    visita_ativa = v
                    break

            if visita_ativa:
                visita_ativa.registrar_saida()
                
                self.__visita_dao.update(visita_ativa) 
                
                self.__tela_visita.mostra_mensagem('Saída registrada com sucesso! Campo de vaga desconsiderado.', 'sucesso')
            else:
                vaga_obj = None
                if id_vaga:
                    try:
                        id_vaga = int(id_vaga)
                    except ValueError:
                        raise NaoEncontradoException('Vaga', 'ID', id_vaga)
                    
                    vaga_obj = self.__controlador_sistema.controlador_vaga.vaga_dao.get(id_vaga)
                    if vaga_obj is None:
                        raise NaoEncontradoException('Vaga', 'ID', id_vaga)
                    
                    vaga_obj.status = True

                nova_visita = Visita(visitante, datetime.now(), vaga_obj)
                self.__visita_dao.add(nova_visita)
                
                self.__tela_visita.mostra_mensagem('Entrada registrada com sucesso!', 'sucesso')

        except NaoEncontradoException as e:
            self.__tela_visita.mostra_mensagem(str(e), 'erro')
            if 'Visitante' in str(e):
                self.__tela_visita.mostra_mensagem('Dica: Utilize a opção "Registrar Novo Visitante" antes de tentar novamente.', 'info')
        except Exception as e:
            self.__tela_visita.mostra_mensagem(f"Ocorreu um erro: {str(e)}", 'erro')

    def registrar_novo_visitante(self):
        self.__controlador_sistema.controlador_visitante.incluir()

    def abre_tela(self):
        self.registrar_visita()