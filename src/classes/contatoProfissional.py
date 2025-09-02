from contato import Contato

class ContatoProfissional(Contato):
    def __init__(self, nome, numero, DDD, email, empresa, cargo):
        super().__init__(nome, numero, DDD, email)
        self.__empresa = empresa 
        self.__cargo = cargo



    def getEmpresa (self):
        return self.__empresa
    
    def getCargo (self):
        return self.__cargo
    
    def setEmpresa(self, empresa):
        self.__empresa = empresa

    def setCargo(self, cargo):
        self.__cargo = cargo

    def imprime(self):
        super().imprime()
        print("Empresa: ", self.__empresa)
        print("Cargo: ", self.__cargo)
        print(3 * "-")