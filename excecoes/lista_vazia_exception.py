class ListaVaziaException(Exception):

    def __init__(self, nome_lista):
        self.mensagem = f'\nNenhum registro de {nome_lista} encontrado.'
        super().__init__(self.mensagem)
