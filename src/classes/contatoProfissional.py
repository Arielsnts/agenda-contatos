from classes.contato import Contato

class ContatoProfissional(Contato):
    def __init__(self, nome, numero, email):
        super().__init__(nome, numero)
        self.__email = email

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

    def imprimir(self):
        super().imprimir()
        print("Email: ", self.__email)