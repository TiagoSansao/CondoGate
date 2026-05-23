
class Vaga:
    def __init__(self, id):
        self.__id = id
        self.__status = False
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
    