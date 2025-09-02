from contato import Contato 

class ContatoPessoal(Contato):
    def __init__(self, nome, numero, DDD, email, aniversario):
        super().__init__(nome, numero, DDD, email)
        self.__aniversario = aniversario


    def getAniversario (self):
        return self.__aniversario
    
    def setAniversario (self, data):
        self.__aniversario = data 

    def imprime(self):
        super().imprime()
        print("Aniversário: ", self.__aniversario)
        print(3 * "-")