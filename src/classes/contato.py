# --- CLASSE BASE: utiliza o conceito de herança sendo a base para mais duas classes que reaproveitam seus atributos e métodos

class Contato:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = self.__formatarNumero(numero)

    # --- OBTER NOME: Retorna o nome do contato
    def getNome(self):
        return self.__nome
    
    # --- OBTER NÚMERO: Retorna o número formatado
    def getNumero(self):
        return self.__numero
    
    # --- DEFINIR NOME: Altera o nome do contato
    def setNome(self, nome):
        self.__nome = nome
    
    # --- DEFINIR NÚMERO: Altera e formata o número
    def setNumero(self, numero):
        self.__numero = self.__formatarNumero(numero)

    # --- MÉTODO PRIVADO: aplica o conceito de encapsulamento elaborado no design de classes
    # --- FORMATAR NÚMERO: Valida e formata o número para o padrão (XX) 9 XXXX-XXXX
    def __formatarNumero(self, numero):
        if not numero.isdigit() or len(numero) != 11:
            raise ValueError("Erro: O número deve conter exatamente 11 dígitos.")
        
        if numero[2] != "9":
            raise ValueError("Erro: O número deve começar com 9 após o DDD.")
        
        return f"({numero[0:2]}) {numero[2]} {numero[3:7]}-{numero[7:]}"
    
    # --- IMPRIMIR: Mostra os dados básicos do contato
    def imprimir(self):
        print("Nome:", self.__nome)
        print("Número:", self.__numero)
