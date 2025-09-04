class Contato:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.setNumero(numero)  # chama o setter que valida e formata

    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setNumero(self, numero):
        # chama método interno que só retorna o número formatado
        self.__numero = self._formatarNumero(numero)

    def _formatarNumero(self, numero):
        if not numero.isdigit() or len(numero) != 11:
            raise ValueError("Erro geral: O número deve conter exatamente 11 dígitos e apenas números.")
        
        if numero[2] != "9":
            raise ValueError("Erro celular: O número móvel deve começar com 9 após o DDD.")
        
        return f"({numero[0:2]}) {numero[2]} {numero[3:7]}-{numero[7:]}"
    
    def imprimir(self):
        print("Nome:", self.__nome)
        print("Número:", self.__numero)
