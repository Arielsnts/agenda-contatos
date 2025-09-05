from classes.contato import Contato

# --- CLASSE DERIVADA (SUBCLASSE): Herda de Contato e especializa o comportamento
class ContatoProfissional(Contato):
    def __init__(self, nome, numero, email):
        super().__init__(nome, numero)
        self.__email = email

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

# --- SOBRESCRITA: implementa polimorfismo, fornecendo uma representação específica para contatos profissionais
    def imprimir(self):
        super().imprimir()
        print("Email: ", self.__email)