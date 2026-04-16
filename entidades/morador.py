class Morador(Pessoa):
    def __init__(cpf: str, nome: str, numero_celular: str): 
        super().__init__(nome, cpf)
        self.__numero_celular = numero_celular

        