from classes.contato import Contato 

class ContatoPessoal(Contato):
    def __init__(self, nome, numero, relacao):
        super().__init__(nome, numero)
        self.__relacao = relacao

    def getRelacao(self):
        return self.__relacao
    
    def setRelacao(self, relacao):
        self.__relacao = relacao

    def imprimir(self):
        super().imprimir()
        print("Relação: ", self.__relacao, "\n")