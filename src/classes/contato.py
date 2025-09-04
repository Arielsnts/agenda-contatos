class Contato:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = self.__formatarNumero(numero)

    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setNumero(self, numero):
        self.__numero = self.__formatarNumero(numero)

    def __formatarNumero(self, numero): 
        if not numero.isdigit() or len(numero) != 11 or numero[0] != "9":
            raise ValueError("Erro: Número móvel inválido. Deve ter 11 dígitos e começar com 9 após o DDD.")
        
        return f"({numero[0:2]}) {numero[2]} {numero[3:7]}-{numero[7:]}" 

    def imprimir(self):
        print("Nome:", self.__nome)
        print ("Número:", self.__numero)
