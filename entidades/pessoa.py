class Pessoa(): 

    def __init__(self, cpf: str, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf
    
