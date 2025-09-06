from classes.contato import Contato 

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoPessoal(Contato):
    def __init__(self, nome, numero, relacao):
        super().__init__(nome, numero)
        self.__relacao = self.__validarRelacao(relacao)

    # --- OBTER RELAÇÃO: Retorna o tipo de relação pessoal
    def getRelacao(self):
        return self.__relacao
    
    # --- DEFINIR RELAÇÃO: Altera o tipo de relação pessoal com validação
    def setRelacao(self, relacao):
        self.__relacao = self.__validarRelacao(relacao)

    # --- MÉTODO PRIVADO: Valida a relação pessoal
    def __validarRelacao(self, relacao):
        if not relacao or not relacao.strip():
            raise ValueError("Erro: Relação não pode estar vazia.")
        
        relacao = relacao.strip()
        
        # Verifica comprimento mínimo
        if len(relacao) < 2:
            raise ValueError("Erro: Relação deve ter pelo menos 2 caracteres.")
        
        # Capitaliza a primeira letra
        return relacao.capitalize()

    # --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos pessoais
    # --- IMPRIMIR: Mostra todos os dados incluindo a relação pessoal
    def imprimir(self):
        super().imprimir()
        print("Relação:", self.__relacao)