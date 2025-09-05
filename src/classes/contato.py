# --- CLASSE BASE: utiliza o conceito de herança sendo a base para mais duas classes que reaproveitam seus atributos e métodos

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

# --- MÉTODO PRIVADO: aplica o conceito de encapsulamento elaborado no design de classes
    def __formatarNumero(self, numero):
        if not numero.isdigit() or len(numero) != 11:
            raise ValueError("Erro: O número deve conter exatamente 11 dígitos.")
        
        if numero[2] != "9":
            raise ValueError("Erro: O número deve começar com 9 após o DDD.")
        
        return f"({numero[0:2]}) {numero[2]} {numero[3:7]}-{numero[7:]}"
    
    def imprimir(self):
        print("Nome:", self.__nome)
        print("Número:", self.__numero)
