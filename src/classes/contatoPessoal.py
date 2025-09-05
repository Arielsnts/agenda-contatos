from classes.contato import Contato 

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoPessoal(Contato):
    def __init__(self, nome, numero, relacao):
        super().__init__(nome, numero)
        self.__relacao = relacao

    def getRelacao(self):
        return self.__relacao
    
    def setRelacao(self, relacao):
        self.__relacao = relacao

# --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos pessoais
    def imprimir(self):
        super().imprimir()
        print("Relação: ", self.__relacao)
        