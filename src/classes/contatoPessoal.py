from classes.contato import Contato 

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoPessoal(Contato):
    def __init__(self, nome, numero, relacao):
        super().__init__(nome, numero)
        self.__relacao = relacao

    # --- OBTER RELAÇÃO: Retorna o tipo de relação pessoal
    def getRelacao(self):
        return self.__relacao
    
    # --- DEFINIR RELAÇÃO: Altera o tipo de relação pessoal
    def setRelacao(self, relacao):
        self.__relacao = relacao

    # --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos pessoais
    # --- IMPRIMIR: Mostra todos os dados incluindo a relação pessoal
    def imprimir(self):
        super().imprimir()
        print("Relação: ", self.__relacao)
        