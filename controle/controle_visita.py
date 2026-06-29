from excecoes.nao_encontrado_exception import NaoEncontradoException
from entidades.visita import Visita, StatusVisita
from limite.tela_visita import TelaVisita
from persistence.visita_dao import VisitaDAO
from persistence.relatorio_dao import RelatorioDAO
from datetime import datetime
import pickle

TEMPO_LIMITE_FILE = 'pickle_files/tempo_limite.pkl'
TEMPO_LIMITE_DEFAULT = 10


class ControladorVisita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_visita = TelaVisita()
        self.__visita_dao = VisitaDAO()
        self.__relatorio_dao = RelatorioDAO()
        self.__tempo_limite_minutos = self.__carregar_tempo_limite()

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
                self.__relatorio_dao.update(visita_ativa)
                
                if visita_ativa.vaga:
                    self.__controlador_sistema.controlador_vaga.vaga_dao.update(visita_ativa.vaga)
                
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
                    
                    if vaga_obj.status:
                        raise Exception('Vaga já está ocupada')
                    
                    vaga_obj.status = True
                    self.__controlador_sistema.controlador_vaga.vaga_dao.update(vaga_obj)

                nova_visita = Visita(visitante, datetime.now(), vaga_obj)
                self.__visita_dao.add(nova_visita)
                self.__relatorio_dao.add(nova_visita)
                self.__tela_visita.mostra_mensagem('Entrada registrada com sucesso!', 'sucesso')

        except NaoEncontradoException as e:
            self.__tela_visita.mostra_mensagem(str(e), 'erro')
            if 'Visitante' in str(e):
                self.__tela_visita.mostra_mensagem('Dica: Utilize a opção "Registrar Novo Visitante" antes de tentar novamente.', 'info')
        except Exception as e:
            self.__tela_visita.mostra_mensagem(f"Ocorreu um erro: {str(e)}", 'erro')

    def registrar_novo_visitante(self):
        self.__controlador_sistema.controlador_visitante.incluir()

    def __carregar_tempo_limite(self):
        try:
            with open(TEMPO_LIMITE_FILE, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return TEMPO_LIMITE_DEFAULT

    def __salvar_tempo_limite(self):
        with open(TEMPO_LIMITE_FILE, 'wb') as f:
            pickle.dump(self.__tempo_limite_minutos, f)

    def configurar_notificacao(self):
        dados = self.__tela_visita.pega_tempo_limite(self.__tempo_limite_minutos)

        if dados is None:
            return

        self.__tempo_limite_minutos = dados['tempo']
        self.__salvar_tempo_limite()
        self.__tela_visita.mostra_mensagem(
            f'Tempo limite atualizado para {self.__tempo_limite_minutos} minutos.',
            'sucesso'
        )

    def listar_visitas_ativas(self):
        visitas = self.__visita_dao.get_all()
        return [visita for visita in visitas if visita.status == StatusVisita.ATIVA]

    def listar_visitas_excedidas(self):
        visitas = self.__visita_dao.get_all()
        agora = datetime.now()
        visitas_excedidas = []

        for v in visitas:
            if v.status == StatusVisita.ATIVA:
                duracao = (agora - v.entrada).total_seconds() / 60
                if duracao > self.__tempo_limite_minutos:
                    excedido = int(duracao - self.__tempo_limite_minutos)
                    visitas_excedidas.append({
                        'nome': v.visitante.nome,
                        'cpf': v.visitante.cpf,
                        'tempo_excedido': excedido
                    })

        return visitas_excedidas

    def gerar_relatorio_visitas(self):
        visitas = self.__relatorio_dao.get_all()
        relatorio = []

        for visita in visitas:
            relatorio.append({
                'nome': visita.visitante.nome,
                'cpf': visita.visitante.cpf,
                'entrada': visita.entrada,
                'status': 'Em andamento' if visita.status == StatusVisita.ATIVA else 'Finalizada',
                'saida': visita.saida
            })

        self.__tela_visita.mostrar_relatorio_visitas(relatorio)

    def notificar_visitas_excedidas(self, visitas_excedidas):
        if visitas_excedidas:
            self.__tela_visita.notificar_visitas_excedidas(visitas_excedidas)

    def abre_tela(self):
        self.registrar_visita()
